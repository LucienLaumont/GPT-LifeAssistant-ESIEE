import torch
import os
import re
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from api.utils.gpt_download import download_gpt2
from api.utils.preprocessing_answer import clean_incomplete_sentences, clean_generated_text, extract_output

MODEL_DIR = "model_finetuned"
MODEL_SIZE = os.getenv("MODEL_SIZE", "gpt2")  # Par défaut, utilise "gpt2"
device = "cuda" if torch.cuda.is_available() else "cpu"

# Charger le modèle GPT-2
model, tokenizer = download_gpt2(MODEL_DIR, MODEL_SIZE)
model.to(device)  # Déplacer le modèle sur le bon device


# List of generation configurations
generation_configs = [
    {
        "name": "Balanced and Coherent",
        "description": "Ensures outputs are both diverse and contextually relevant.",
        "params": {
            "do_sample": True,  # Enables sampling for variability
            "temperature": 0.7,  # Balances randomness and determinism
            "top_k": 50,  # Considers the top 50 token options
            "max_new_tokens": 150,  # Limits the length of the generated text
            "repetition_penalty": 1.2  # Discourages repetitive phrases
        }
    },
    {
        "name": "Creative Exploration",
        "description": "Encourages imaginative and varied text generation.",
        "params": {
            "do_sample": True,
            "temperature": 0.85,  # Increases randomness for creativity
            "top_p": 0.9,  # Nucleus sampling for broader token selection
            "max_new_tokens": 200,
            "repetition_penalty": 1.1
        }
    },
    {
        "name": "Concise and Focused",
        "description": "Generates brief and to-the-point responses.",
        "params": {
            "do_sample": False,  # Deterministic output
            "temperature": 0.6,  # Lower temperature for focused responses
            "max_new_tokens": 100,
            "repetition_penalty": 1.3
        }
    },
    {
        "name": "Extended and Detailed",
        "description": "Produces longer, in-depth responses suitable for comprehensive topics.",
        "params": {
            "do_sample": True,
            "temperature": 0.75,
            "top_k": 100,
            "max_new_tokens": 300,  # Allows for extended text generation
            "repetition_penalty": 1.15
        }
    },
    {
        "name": "High Precision",
        "description": "Aims for accurate and contextually precise outputs.",
        "params": {
            "do_sample": False,
            "temperature": 0.65,
            "top_p": 0.8,
            "max_new_tokens": 150,
            "repetition_penalty": 1.25
        }
    }
]

META_PROMPT = (
    "Your task is to provide an answer to the following question:\n"
)

def generate_text(prompt: str, config_name: str) -> str:
    """
    Génère du texte en fonction de la configuration spécifiée.
    """
    # Trouver la configuration par nom
    config = next((cfg for cfg in generation_configs if cfg["name"] == config_name), None)

    if config is None:
        raise ValueError(f"Configuration '{config_name}' non trouvée. Options disponibles : {[cfg['name'] for cfg in generation_configs]}")

    # Assigner le token de padding si nécessaire
    tokenizer.pad_token = tokenizer.eos_token

    # Tokenization avec attention_mask
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True, max_length=512)

    # 🔹 Déplacer explicitement les tensors d'entrée sur le bon device
    inputs = {key: value.to(device) for key, value in inputs.items()}

    # 🔹 Générer du texte en s'assurant que le modèle et les inputs sont bien sur le même device
    with torch.no_grad():
        output = model.generate(
            inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            **config["params"],
            pad_token_id=tokenizer.eos_token_id
        )

    # Décoder la sortie générée
    return tokenizer.decode(output[0], skip_special_tokens=True)


router = APIRouter()

class UserInput(BaseModel):
    prompt: str

@router.post("/chat/")
async def chat_with_llm(user_input: UserInput):
    try:
        # 📝 Ajout du meta-prompt avant la question
        full_prompt = META_PROMPT + "Question: " + user_input.prompt + "\nAnswer: "

        # 🎯 Génération du texte avec la configuration spécifiée
        raw_response = generate_text(full_prompt, "Balanced and Coherent")

        # 🧹 Nettoyage de la réponse générée
        cleaned_response = clean_generated_text(raw_response)
        extracted_response = extract_output(cleaned_response)
        final_response = clean_incomplete_sentences(extracted_response)

        return {"response": final_response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

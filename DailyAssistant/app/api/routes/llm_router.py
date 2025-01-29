import torch
import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from api.utils.gpt_download import download_gpt2
from api.utils.preprocessing_answer import clean_incomplete_sentences, remove_redundant_sentences



MODEL_DIR = "model_finetuned"
MODEL_SIZE = os.getenv("MODEL_SIZE", "gpt2")  # Par défaut, utilise "gpt2"
device = "cuda" if torch.cuda.is_available() else "cpu"

# Charger le modèle GPT-2
model, tokenizer = download_gpt2(MODEL_DIR, MODEL_SIZE)

router = APIRouter()

class UserInput(BaseModel):
    prompt: str

@router.post("/chat/")
async def chat_with_llm(user_input: UserInput):
    try:

        input_text = user_input.prompt
        inputs = tokenizer(input_text, return_tensors="pt")
        input_ids = inputs.input_ids
        attention_mask = inputs.attention_mask

        input_ids = input_ids.to(device)
        attention_mask = attention_mask.to(device)
        # Générer la sortie
        output = model.generate(
            input_ids = input_ids,
            attention_mask = attention_mask,
            pad_token_id = tokenizer.pad_token_id,
            max_length = input_ids.shape[1] + 100,
            num_beams = 5,
            temperature = 1,
            top_k = 50,
            do_sample = True
        )
        
        # Décoder la réponse
        response_text = tokenizer.decode(output[0], skip_special_tokens=True)

        # Supprimer l'input de l'output
        response_text = response_text[len(input_text):].strip()

        # Appliquer le nettoyage et la suppression des redondances
        response_text = clean_incomplete_sentences(response_text)
        response_text = remove_redundant_sentences(response_text, similarity_threshold=0.8)

        return {"response": response_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

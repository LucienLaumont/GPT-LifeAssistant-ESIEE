
import os

MODEL_DIR = os.getenv("MODEL_DIR", "model")  # Par défaut, sauvegarde dans "model"
MODEL_SIZE = os.getenv("MODEL_SIZE", "gpt2")  # Par défaut, utilise "gpt2"

# Désactiver certains avertissements TensorFlow et Hugging Face
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

from transformers import GPT2LMHeadModel, GPT2Tokenizer


# Vérifier si le modèle est déjà téléchargé, sinon le récupérer
def download_gpt2(save_dir, model_size):
    """
    Télécharge un modèle GPT-2 si les fichiers nécessaires ne sont pas déjà présents.

    Args:
        model_size (str): Taille du modèle à télécharger (e.g., 'gpt2', 'gpt2-medium').
        save_dir (str): Répertoire où le modèle sera sauvegardé.

    Returns:
        tuple: (model, tokenizer) GPT-2
    """
    config_path = os.path.join(save_dir, "config.json")
    model_path = os.path.join(save_dir, "model.safetensors")
    tokenizer_path = os.path.join(save_dir, "vocab.json")

    # Vérifier si un modèle fine-tuné existe déjà
    if os.path.exists(config_path) and os.path.exists(model_path) and os.path.exists(tokenizer_path):
        print(f"✅ Modèle fine-tuné trouvé dans {save_dir}, chargement...")
        model = GPT2LMHeadModel.from_pretrained(save_dir)
        tokenizer = GPT2Tokenizer.from_pretrained(save_dir)
    else:
        # Télécharger le modèle si aucun modèle fine-tuné n'est présent
        os.makedirs(save_dir, exist_ok=True)
        print(f"📥 Téléchargement du modèle {model_size} ...")
        tokenizer = GPT2Tokenizer.from_pretrained(model_size)
        model = GPT2LMHeadModel.from_pretrained(model_size)
        tokenizer.save_pretrained(save_dir)
        model.save_pretrained(save_dir)
        print(f"✅ Modèle {model_size} téléchargé et sauvegardé dans {save_dir}.")

    return model, tokenizer

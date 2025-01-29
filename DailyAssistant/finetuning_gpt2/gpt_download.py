import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer


def download_gpt2(save_dir, model_size):
    """
    Télécharge un modèle GPT-2 si les fichiers nécessaires ne sont pas déjà présents.
    Si le modèle est déjà téléchargé, il est chargé depuis les fichiers locaux.

    Args:
        model_size (str): Taille du modèle à télécharger (e.g., 'gpt2', 'gpt2-medium').
        save_dir (str): Répertoire où le modèle sera sauvegardé.

    Returns:
        tuple: (model, tokenizer) GPT-2 chargé depuis le disque ou téléchargé.
    """
    # Chemins des fichiers du modèle
    config_path = os.path.join(save_dir, "config.json")
    model_path = os.path.join(save_dir, "model.safetensors")  # Remis en .bin (Hugging Face format)
    tokenizer_path = os.path.join(save_dir, "vocab.json")

    # Vérifier si le modèle est déjà présent
    if os.path.exists(config_path) and os.path.exists(model_path) and os.path.exists(tokenizer_path):
        print(f"✅ Le modèle {model_size} est déjà présent dans {save_dir}, chargement depuis les fichiers locaux...")
        model = GPT2LMHeadModel.from_pretrained(save_dir).to("cuda" if torch.cuda.is_available() else "cpu")
        tokenizer = GPT2Tokenizer.from_pretrained(save_dir)
        return model, tokenizer

    # Créer le répertoire si nécessaire
    os.makedirs(save_dir, exist_ok=True)

    # Télécharger et sauvegarder le modèle et le tokenizer
    print(f"📥 Téléchargement du modèle {model_size} dans {save_dir}...")
    tokenizer = GPT2Tokenizer.from_pretrained(model_size)
    model = GPT2LMHeadModel.from_pretrained(model_size).to("cuda" if torch.cuda.is_available() else "cpu")

    tokenizer.save_pretrained(save_dir)
    model.save_pretrained(save_dir)
    print(f"✅ Modèle {model_size} téléchargé et sauvegardé dans {save_dir}.")

    return model, tokenizer

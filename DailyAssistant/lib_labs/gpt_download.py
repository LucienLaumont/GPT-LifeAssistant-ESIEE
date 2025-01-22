import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

from transformers import GPT2LMHeadModel, GPT2Tokenizer


def download_gpt2(save_dir, model_size):
    """
    Télécharge un modèle GPT-2 si les fichiers nécessaires ne sont pas déjà présents.

    Args:
        model_size (str): Taille du modèle à télécharger (e.g., 'gpt2', 'gpt2-medium').
        save_dir (str): Répertoire où le modèle sera sauvegardé.

    Returns:
        bool: True si le modèle a été téléchargé, False s'il était déjà présent.
    """
    # Vérifier si le répertoire existe et contient les fichiers nécessaires
    config_path = os.path.join(save_dir, "config.json")
    model_path = os.path.join(save_dir, "pytorch_model.bin")
    tokenizer_path = os.path.join(save_dir, "vocab.json")

    if os.path.exists(config_path) and os.path.exists(model_path) and os.path.exists(tokenizer_path):
        print(f"Le modèle {model_size} est déjà présent dans {save_dir}.")
        return False

    # Créer le répertoire si nécessaire
    os.makedirs(save_dir, exist_ok=True)

    # Télécharger et sauvegarder le modèle et le tokenizer
    print(f"Téléchargement du modèle {model_size} dans {save_dir}...")
    tokenizer = GPT2Tokenizer.from_pretrained(model_size)
    model = GPT2LMHeadModel.from_pretrained(model_size)

    tokenizer.save_pretrained(save_dir)
    model.save_pretrained(save_dir)
    print(f"Modèle {model_size} téléchargé et sauvegardé dans {save_dir}.")
    return model, tokenizer

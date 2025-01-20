import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
import sys
from dotenv import load_dotenv

from lib.gpt_download import download_script


load_dotenv()

MODEL_DIR = os.getenv("MODEL_DIR")
MODEL_SIZE = os.getenv("MODEL_SIZE")

def main():
    print(MODEL_SIZE,MODEL_DIR)
    download_script(MODEL_SIZE,MODEL_DIR)
    return True

if __name__ == "__main__":
    main()
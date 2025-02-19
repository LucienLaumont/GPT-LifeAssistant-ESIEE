import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def clean_incomplete_sentences(text):
    """
    Slice the input text into sentences, keeping the formatting 
    (e.g., \n, spaces), and remove incomplete phrases that do not 
    end with a proper punctuation mark.
    """
    # Split the text while keeping the delimiters (e.g., .!?) and formatting
    sentences = re.split(r'(?<=[.!?])(\s+)', text)
    
    cleaned_text = ""
    for i in range(0, len(sentences) - 1, 2):  # Process sentences with their trailing spaces
        sentence = sentences[i]
        trailing_space = sentences[i + 1]
        if re.search(r'[.!?]$', sentence):  # Check if the sentence ends with valid punctuation
            cleaned_text += sentence + trailing_space
    
    # Handle cases where the last part is an incomplete sentence
    if len(sentences) % 2 != 0 and re.search(r'[.!?]$', sentences[-1]):
        cleaned_text += sentences[-1]
    
    return cleaned_text

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def remove_redundant_sentences(text, similarity_threshold=0.8):
    """
    Removes redundant or highly similar sentences from the given text, preserving formatting such as \n and spaces, while keeping key sentences.

    Parameters:
        text (str): The input text containing potentially redundant sentences.
        similarity_threshold (float): The cosine similarity threshold above which
                                       sentences are considered redundant.

    Returns:
        str: Text with redundant sentences removed.
    """
    # Split the text into sentences while preserving the delimiters and formatting
    sentences = re.split(r'(?<=[.!?])\s+', text)

    # Vectorize the sentences using TF-IDF
    vectorizer = TfidfVectorizer().fit_transform(sentences)

    # Compute cosine similarity between all sentence pairs
    similarity_matrix = cosine_similarity(vectorizer)

    # Identify sentences to keep
    sentences_to_keep = []
    for i, sentence in enumerate(sentences):
        # Check if the sentence is similar to any previously kept sentence
        if all(similarity_matrix[i, j] < similarity_threshold for j in sentences_to_keep):
            sentences_to_keep.append(i)

    # Reconstruct the text with only unique sentences
    unique_sentences = [sentences[i] for i in sentences_to_keep]
    return '\n'.join(unique_sentences)

def clean_generated_text(text: str) -> str:
    """
    Cleans and formats the generated text to remove extra newlines, spaces, and stray punctuation.

    Args:
        text (str): Raw generated text.

    Returns:
        str: Formatted and cleaned text.
    """
    # Remove stray dots at the beginning of a line
    text = re.sub(r"\n\s*\.", "\n", text)

    # Ensure proper spacing around punctuation
    text = re.sub(r"\s+\.", ".", text)  # Remove extra spaces before periods
    text = re.sub(r"\.\s*\.", ".", text)  # Fix multiple consecutive periods

    # Normalize newlines and lists (Ensure proper numbering)
    text = re.sub(r"\n\s*(\d+)\.\s*", r"\n\1. ", text)  # Ensure numbered lists are formatted correctly

    # Trim excessive newlines
    text = re.sub(r"\n{2,}", "\n", text).strip()

    return text

# ✅ Fonction pour extraire la réponse après "Answer: "
def extract_output(response_text):
    match = re.search(r"Answer:\s*(.*)", response_text, re.IGNORECASE)
    return match.group(1).strip() if match else response_text.strip()



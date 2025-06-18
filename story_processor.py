from nltk.tokenize import sent_tokenize
import nltk

nltk.download('punkt')

def get_stories(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        prompts = f.read().strip().split("\n\n")
    return prompts

def extract_scenes(script):
    return sent_tokenize(script)
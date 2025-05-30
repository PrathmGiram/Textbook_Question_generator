from transformers import pipeline
import re
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("iarfmoose/t5-base-question-generator")

def chunk_text(text, max_tokens=400):
    words = text.split()
    chunks = []
    current_chunk = []
    current_len = 0

    for word in words:
        token_len = len(tokenizer.tokenize(word))
        if current_len + token_len > max_tokens:
            chunks.append(" ".join(current_chunk))
            current_chunk = []
            current_len = 0
        current_chunk.append(word)
        current_len += token_len

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

# Hugging Face QG model
qg_pipeline = pipeline("text2text-generation", model="iarfmoose/t5-base-question-generator")

def generate_questions(text):
    print("Splitting text into chunks...")
    chunks = chunk_text(text, max_tokens=400)

    all_questions = []

    for i, chunk in enumerate(chunks):
        print(f"Generating questions for chunk {i+1}/{len(chunks)}")
        output = qg_pipeline(chunk, max_new_tokens=256)
        raw_text = output[0]['generated_text']
        for line in raw_text.strip().split('\n'):
            cleaned = clean_question(line)
            if cleaned:
                all_questions.append(cleaned)

    return all_questions



import re

def clean_question(q):
    # Remove excessive punctuation (like many question marks)
    q = re.sub(r'\?{2,}', '?', q)                    # Replace repeated '?' with one
    q = re.sub(r'[\? ]+$', '?', q.strip())           # Strip trailing ? or spaces
    q = re.sub(r'[^A-Za-z0-9\s\.,;:!?\'"-]', '', q)  # Remove odd characters
    q = re.sub(r'\s+', ' ', q).strip()               # Normalize whitespace
    return q


def parse_questions(output):
    raw_text = output[0]['generated_text']
    questions = []
    for line in raw_text.strip().split('\n'):
        if line.strip():
            cleaned = clean_question(line)
            questions.append(cleaned)
    return questions

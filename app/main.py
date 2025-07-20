import os
import json
import fitz  # PyMuPDF
from utils import extract_outline

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

def process_pdf(pdf_path, output_path):
    doc = fitz.open(pdf_path)
    title = doc.metadata.get("title", os.path.basename(pdf_path).replace(".pdf", ""))
    outline = extract_outline(doc)

    output = {
        "title": title,
        "outline": outline
    }

    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(INPUT_DIR, filename)
            json_path = os.path.join(OUTPUT_DIR, filename.replace(".pdf", ".json"))
            process_pdf(pdf_path, json_path)

if __name__ == "__main__":
    main()

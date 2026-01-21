import json
from txt_extractor import extract_text
from classifier import classify_document

def process_file(file_path):
    text = extract_text(file_path)
    result = classify_document(text)

    output = {
        "file": file_path,
        "category": result["category"],
        "value": result["matched_keyword"]
    }

    print(json.dumps(output, indent=4))

if __name__ == "__main__":
    file_path = input("Enter file path: ")
    process_file(file_path)

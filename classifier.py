def classify_document(text):
    text = text.lower()

    categories = {
        "Resume": ["resume", "education", "skills", "experience"],
        "Invoice": ["invoice", "bill", "amount", "gst", "total"],
        "Offer Letter": ["offer", "salary", "joining", "appointment"],
        "Legal Document": ["agreement", "law", "terms", "conditions"],
        "Technical Document": ["algorithm", "system", "architecture", "api"]
    }

    for category, keywords in categories.items():
        for word in keywords:
            if word in text:
                return {
                    "category": category,
                    "matched_keyword": word
                }

    return {
        "category": "Unknown",
        "matched_keyword": None
    }

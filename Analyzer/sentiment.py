from transformers import pipeline

sentiment_model = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")


def analyze_text(text):
    if not text:
        return {"error": "No text provided"}

    label_map = {
        "LABEL_0": "Negative",
        "LABEL_1": "Neutral",
        "LABEL_2": "Positive"
    }
    result = sentiment_model(text)[0]
    label = label_map.get(result['label'], result['label'])
    return {
        "label": label,
        "score": round(result['score'], 4)
    }


Sentiment Analysis Web Application:
This project is a simple web application that performs sentiment analysis on user-provided text using Hugging Face Transformers and a Flask backend.
The application allows users to input text, submit it, and receive both a sentiment label (Positive, Negative, or Neutral) and a confidence score.

features:
Flask backend serving a sentiment analysis model.
Frontend built with HTML, CSS, and JavaScript.
Uses Hugging Face transformers pipeline for sentiment classification.
Returns both sentiment label and confidence score.

Technology Stack:
Python 3.10+
Flask
Hugging Face Transformers
HTML, CSS, JavaScript

Example Outputs:
The app correctly identifies straightforward cases:

"I love Python!" → Positive (97.7%)
"This is terrible." → Negative (96.4%)
"This is neutral." → Neutral (72.0%)

However, it struggles with sarcasm and nuanced statements:

"I just love waiting in line for hours." → Positive (63.6%)
"This class is so exciting, I almost fell asleep." → Positive (99.1%)

This demonstrates the limitations of pre-trained sentiment models when handling sarcasm or context-dependent language.

Limitations:
The model is not fine-tuned for sarcasm or irony.
Predictions may not always reflect human interpretation.
Results should be interpreted with caution in real-world use cases.




"I couldn’t be happier… if I were dead." → Positive (40.9%)

This demonstrates the limitations of pre-trained sentiment models when handling sarcasm or context-dependent language.

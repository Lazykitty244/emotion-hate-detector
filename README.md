# Emotion & Hate Speech Detector

This project is a demo of emotion classification and hate speech detection using Hugging Face Transformers, deployed with Gradio.

## Features

- Emotion detection (joy, sadness, anger, fear, etc.)
- Hate speech classification (HATE vs NON-HATE)
- Live web interface powered by Gradio
- Deployed version: [Hugging Face Space](https://huggingface.co/spaces/Lazykitty244/emotion-hate-detector)

## Models Used

- Emotion: `bhadresh-savani/distilbert-base-uncased-emotion`
- Hate Speech: `Hate-speech-CNERG/dehatebert-mono-english`

## Local Installation

```bash
git clone https://github.com/YourUsername/emotion-hate-detector.git
cd emotion-hate-detector
pip install -r requirements.txt
python app.py

import gradio as gr
from transformers import pipeline

# Load models
emotion_classifier = pipeline(
    "text-classification",
    model="bhadresh-savani/distilbert-base-uncased-emotion"
)
hate_speech_classifier = pipeline(
    "text-classification",
    model="Hate-speech-CNERG/dehatebert-mono-english"
)

def analyze_text(text):
    emotion_result = emotion_classifier(text)
    hate_result = hate_speech_classifier(text)

    emotions = {res['label']: res['score'] for res in emotion_result}
    hate_speech = {res['label']: res['score'] for res in hate_result}

    return emotions, hate_speech


iface = gr.Interface(
    fn=analyze_text,
    inputs=gr.Textbox(lines=4, placeholder="Enter your text here..."),
    outputs=[
        gr.Label(num_top_classes=6, label="Emotion Detection"),
        gr.Label(num_top_classes=3, label="Hate Speech Detection")
    ],
    title="🧠 Emotion & Hate Speech Detector"
)

if __name__ == "__main__":
    iface.launch()

import streamlit as st
from transformers import pipeline

class Emotions:
    def __init__(self):
        self.model = "blanchefort/rubert-base-cased-sentiment"
        self.classifier = pipeline("sentiment-analysis", model=self.model)

    def take_emotion(self, string):
        result = self.classifier(string)
        return result[0]['label'], result[0]['score']

# Создание экземпляра класса Emotions
emotion_analyzer = Emotions()

# Интерфейс Streamlit
st.title('Определение тональности текста на русском языке')

user_input = st.text_area('Введите текст:')
if st.button('Анализировать'):
    sentiment, score = emotion_analyzer.take_emotion(user_input)
    sentiment_translation = {
        "POSITIVE": "Позитивный",
        "NEGATIVE": "Негативный",
        "NEUTRAL": "Нейтральный"
    }
    st.write(f"Тональность текста: {sentiment_translation[sentiment]}")

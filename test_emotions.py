import unittest
from transformers import pipeline
from streamlit_app import Emotions  # Замените 'your_module' на имя вашего модуля

class TestEmotions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.emotion_analyzer = Emotions()

    def test_positive_sentiment(self):
        text = "Это замечательно!"
        sentiment, score = self.emotion_analyzer.take_emotion(text)
        self.assertEqual(sentiment, "POSITIVE")
        self.assertGreater(score, 0.5)

    def test_negative_sentiment(self):
        text = "Это ужасно!"
        sentiment, score = self.emotion_analyzer.take_emotion(text)
        self.assertEqual(sentiment, "NEGATIVE")
        self.assertGreater(score, 0.5)

    def test_neutral_sentiment(self):
        text = "Это книга."
        sentiment, score = self.emotion_analyzer.take_emotion(text)
        self.assertEqual(sentiment, "NEUTRAL")
        self.assertGreater(score, 0.5)

if __name__ == '__main__':
    unittest.main()

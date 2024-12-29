import unittest
from transformers import pipeline
from your_module import Emotions  # Замените 'your_module' на имя вашего модуля

class TestEmotions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.emotion_analyzer = Emotions()

    def test_positive_sentiment(self):
        text = "Это замечательно!"
        sentiment, score = self.emotion_analyzer.take_emotion(text)
        self.assertEqual(sentiment, "positive")
        self.assertGreater(score, 0.5)

    def test_negative_sentiment(self):
        text = "Это ужасно!"
        sentiment, score = self.emotion_analyzer.take_emotion(text)
        self.assertEqual(sentiment, "negative")
        self.assertGreater(score, 0.5)

    def test_neutral_sentiment(self):
        text = "Это книга."
        sentiment, score = self.emotion_analyzer.take_emotion(text)
        self.assertEqual(sentiment, "neutral")
        self.assertGreater(score, 0.5)

if __name__ == '__main__':
    unittest.main()

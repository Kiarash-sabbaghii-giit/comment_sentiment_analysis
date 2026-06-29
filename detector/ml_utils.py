# detector/ml_utils.py
import pickle
import os
from .preprocess import preprocessor


class SentimentAnalyzer:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))

        model_path = os.path.join(base_dir, 'models', 'logistic_model.pkl')
        vectorizer_path = os.path.join(base_dir, 'models', 'count_vectorizer.pkl')

        try:
            with open(model_path, 'rb') as f:
                self.model = pickle.load(f)

            with open(vectorizer_path, 'rb') as f:
                self.vectorizer = pickle.load(f)

            print("✅ Sentiment model loaded successfully!")
        except FileNotFoundError as e:
            print(f"❌ Error: {e}")
            raise

    def predict(self, text):
        """
        0 = happy (مثبت) 😊
        1 = sad (منفی) 😞
        """
        if not text or not isinstance(text, str):
            raise ValueError("Input must be a non-empty string")

        # Preprocess
        cleaned_text = preprocessor.clean_preprocess_complete(text)

        # Vectorize
        text_vec = self.vectorizer.transform([cleaned_text])

        # Predict
        prediction = self.model.predict(text_vec)[0]  # 0 یا 1

        # Get Probability
        try:
            probability = self.model.predict_proba(text_vec)[0]
            # probability[0] = احتمال کلاس 0 (happy)
            # probability[1] = احتمال کلاس 1 (sad)
        except AttributeError:
            probability = [0.5, 0.5]

        # ===== Map labels =====
        # 0 = happy, 1 = sad
        if prediction == 0:
            label = 'happy'
            label_fa = 'مثبت'
            emoji = '😊'
        else:  # prediction == 1
            label = 'sad'
            label_fa = 'منفی'
            emoji = '😞'

        # ===== Probabilities =====
        happy_prob = probability[0] * 100  # احتمال کلاس 0
        sad_prob = probability[1] * 100  # احتمال کلاس 1

        # ===== Return =====
        return {
            'label': label,  # 'happy' یا 'sad'
            'label_fa': label_fa,  # 'مثبت' یا 'منفی'
            'emoji': emoji,  # 😊 یا 😞
            'confidence': max(happy_prob, sad_prob),
            'happy_probability': happy_prob,  # ← این رو حتماً برگردون
            'sad_probability': sad_prob,  # ← این رو حتماً برگردون
            'original_text': text,
            'cleaned_text': cleaned_text,
            'prediction': int(prediction)  # 0 یا 1
        }


# ایجاد نمونه
analyzer = SentimentAnalyzer()
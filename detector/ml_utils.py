import pickle
import os


class SpamDetector:
    def __init__(self):
        # مسیر فایل‌های مدل
        base_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(base_dir, 'models', 'logistic_model.pkl')
        vectorizer_path = os.path.join(base_dir, 'models', 'count_vectorizer.pkl')

        # بارگذاری مدل
        try:
            with open(model_path, 'rb') as f:
                self.model = pickle.load(f)

            with open(vectorizer_path, 'rb') as f:
                self.vectorizer = pickle.load(f)

            print("✅ مدل با موفقیت بارگذاری شد!")
        except FileNotFoundError as e:
            print(f"❌ خطا: فایل مدل پیدا نشد! {e}")
            raise

    def predict(self, text):
        """پیش‌بینی اسپم یا هام بودن متن"""
        # تبدیل متن به بردار
        text_vec = self.vectorizer.transform([text])

        # پیش‌بینی
        prediction = self.model.predict(text_vec)[0]
        probability = self.model.predict_proba(text_vec)[0]

        return {
            'label': 'spam' if prediction == 1 else 'ham',
            'confidence': max(probability) * 100,
            'spam_probability': probability[1] * 100,
            'ham_probability': probability[0] * 100
        }


# ایجاد یک نمونه از کلاس برای استفاده در views
detector = SpamDetector()
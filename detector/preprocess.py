# detector/preprocess.py
import re
import string
import unicodedata


class CommentPreprocessor:
    def __init__(self):
        # لیست stopwords دستی فارسی (بدون نیاز به hazm)
        self.stopwords = set([
            'و', 'در', 'به', 'از', 'که', 'این', 'با', 'برای', 'را', 'رو',
            'است', 'نیز', 'شود', 'می', 'بود', 'ها', 'های', 'ام', 'ات',
            'اش', 'ای', 'تا', 'بر', 'برای', 'چون', 'مثل', 'همان', 'هم',
            'هر', 'یک', 'دو', 'سه', 'چهار', 'پنج', 'شش', 'هفت', 'هشت',
            'نه', 'ده', 'بیشتر', 'کمتر', 'چیزی', 'چیز', 'کسی', 'کس',
            'همه', 'همیشه', 'بعضی', 'چند', 'چقدر', 'کجا', 'کی', 'چطور',
            'چه', 'چی', 'کدام', 'چنین', 'چنان', 'همین', 'همان', 'آن',
            'این', 'آنها', 'ما', 'شما', 'من', 'تو', 'او', 'ایشان',
            'خود', 'خودم', 'خودت', 'خودش', 'خودمان', 'خودتان', 'خودشان',
            'بهتر', 'بهترین', 'بیشتر', 'بیشترین', 'کم', 'کمتر', 'کمترین',
            'خیلی', 'بسیار', 'کاملا', 'تقریبا', 'حدود', 'بعد', 'قبل',
            'زیر', 'روی', 'کنار', 'پشت', 'جلوی', 'بالای', 'پایین'
        ])

        # لیست کلمات رایج Finglish
        self.finglish_keywords = [
            'salam', 'chetori', 'khubi', 'mersi', 'lotf', 'mamnun',
            'khob', 'bale', 'na', 'are', 'man', 'to', 'shanbe', 'jome',
            'khosh', 'hal', 'daram', 'mikham', 'migi', 'cheshm'
        ]

        # دیکشنری تبدیل Finglish به فارسی
        self.finglish_map = {
            's': 'س', 'S': 'س', 'a': 'ا', 'A': 'آ', 'l': 'ل', 'L': 'ل',
            'm': 'م', 'M': 'م', 'n': 'ن', 'N': 'ن', 'k': 'ک', 'K': 'ک',
            'h': 'ه', 'H': 'ه', 'i': 'ی', 'I': 'ی', 'c': 'چ', 'C': 'چ',
            'b': 'ب', 'B': 'ب', 'd': 'د', 'D': 'د', 'e': 'ه', 'E': 'ه',
            'o': 'و', 'O': 'و', 't': 'ت', 'T': 'ت', 'r': 'ر', 'R': 'ر',
            'y': 'ی', 'Y': 'ی', 'p': 'پ', 'P': 'پ', 'g': 'گ', 'G': 'گ',
            'z': 'ز', 'Z': 'ز', 'f': 'ف', 'F': 'ف', 'v': 'و', 'V': 'و',
            'u': 'و', 'U': 'و', 'x': 'خ', 'X': 'خ', 'j': 'ج', 'J': 'ج',
            'w': 'و', 'W': 'و', 'q': 'ق', 'Q': 'ق'
        }

        # دیکشنری ترجمه انگلیسی به فارسی
        self.english_to_persian = {
            'hello': 'سلام', 'hi': 'سلام', 'good': 'خوب', 'bad': 'بد',
            'yes': 'بله', 'no': 'نه', 'thank': 'متشکرم', 'thanks': 'متشکرم',
            'love': 'عشق', 'happy': 'خوشحال', 'sad': 'ناراحت',
            'goodbye': 'خداحافظ', 'ok': 'باشه', 'okay': 'باشه',
            'nice': 'خوب', 'great': 'عالی', 'perfect': 'عالی',
            'awesome': 'عالی', 'amazing': 'عالی', 'wow': 'وای',
            'oh': 'آه', 'yeah': 'آره', 'yep': 'آره', 'nope': 'نه',
            'sorry': 'متاسفم', 'please': 'لطفا', 'spam': 'اسپم',
            'free': 'رایگان', 'money': 'پول', 'win': 'برنده شدن',
            'winner': 'برنده', 'prize': 'جایزه', 'click': 'کلیک',
            'link': 'لینک', 'subscribe': 'عضویت', 'offer': 'پیشنهاد'
        }

    def normalize_persian(self, text):
        """نرمالسازی کاراکترهای فارسی"""
        if not isinstance(text, str):
            return ""

        arabic_to_persian = {
            'ي': 'ی', 'ك': 'ک', 'دِ': 'ده', 'بِ': 'به', 'زِ': 'زه',
            'ذِ': 'ذه', 'شِ': 'شه', 'سِ': 'سه', 'ى': 'ی', 'ة': 'ه',
            'ﻷ': 'لا', 'ﻹ': 'لا', 'ﻵ': 'لا', 'ئ': 'ی', 'أ': 'ا',
            'إ': 'ا', 'آ': 'ا'
        }
        for ar, pe in arabic_to_persian.items():
            text = text.replace(ar, pe)

        return text

    def remove_emojis(self, text):
        """حذف ایموجیها"""
        emoji_pattern = re.compile(
            "["
            "\U0001F600-\U0001F64F"  # emoticons
            "\U0001F300-\U0001F5FF"  # symbols & pictographs
            "\U0001F680-\U0001F6FF"  # transport & map symbols
            "\U0001F700-\U0001F77F"  # alchemical symbols
            "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
            "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
            "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
            "\U0001FA00-\U0001FA6F"  # Chess Symbols
            "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
            "\U00002702-\U000027B0"  # Dingbats
            "\U000024C2-\U0001F251"  # Enclosed characters
            "]+",
            flags=re.UNICODE
        )
        return emoji_pattern.sub(r'', text)

    def remove_punctuations(self, text):
        """حذف علائم نگارشی فارسی و انگلیسی"""
        persian_punctuations = '،؛؟!؟»«%٪×÷'
        english_punctuations = string.punctuation
        all_punctuations = persian_punctuations + english_punctuations

        translator = str.maketrans('', '', all_punctuations)
        return text.translate(translator)

    def remove_numbers(self, text):
        """حذف اعداد فارسی و انگلیسی"""
        persian_numbers = '۰۱۲۳۴۵۶۷۸۹'
        english_numbers = '0123456789'
        all_numbers = persian_numbers + english_numbers

        translator = str.maketrans('', '', all_numbers)
        return text.translate(translator)

    def remove_extra_spaces(self, text):
        """حذف فاصلههای اضافی"""
        text = re.sub(r'\s+', ' ', text)
        return text.strip()

    def remove_single_characters(self, text):
        """حذف کلمات تک حرفی"""
        return ' '.join([word for word in text.split() if len(word) > 1])

    def remove_stopwords(self, text):
        """حذف کلمات بیمعنی فارسی"""
        return ' '.join([word for word in text.split() if word not in self.stopwords])

    def remove_english_letters(self, text):
        """حذف حروف انگلیسی"""
        return re.sub(r'[a-zA-Z]', '', text)

    def normalize_unicode(self, text):
        """نرمالسازی یونیکد"""
        return unicodedata.normalize('NFKC', text)

    def is_finglish(self, text):
        """تشخیص فینگلیش"""
        if not isinstance(text, str):
            return False

        text = text.strip()
        if len(text) == 0:
            return False

        persian_chars = len(re.findall(r'[\u0600-\u06FF]', text))
        english_chars = len(re.findall(r'[a-zA-Z]', text))

        # اگر حروف فارسی نداره ولی انگلیسی داره
        if persian_chars == 0 and english_chars > 0:
            text_lower = text.lower()
            for word in self.finglish_keywords:
                if word in text_lower:
                    return True

            # بررسی ساختار فینگلیش
            has_vowels = len(re.findall(r'[aeiouAEIOU]', text)) > 0
            has_common = len(re.findall(r'[sckhmnlrtypbgvz]', text.lower())) > 0

            return has_vowels and has_common

        return False

    def is_english(self, text):
        """تشخیص زبان انگلیسی خالص"""
        if not isinstance(text, str):
            return False

        text = text.strip()
        if len(text) == 0:
            return False

        persian_chars = len(re.findall(r'[\u0600-\u06FF]', text))
        english_chars = len(re.findall(r'[a-zA-Z]', text))

        return persian_chars == 0 and english_chars > 0

    def convert_finglish_to_persian(self, text):
        """تبدیل فینگلیش به فارسی"""
        if not isinstance(text, str):
            return ""

        # جایگزینی حروف
        for eng, per in self.finglish_map.items():
            text = text.replace(eng, per)

        return text

    def translate_english_to_persian(self, text):
        """ترجمه ساده کلمات انگلیسی به فارسی"""
        if not isinstance(text, str):
            return ""

        words = text.split()
        translated = []
        for word in words:
            word_lower = word.lower().strip('.,!?')
            if word_lower in self.english_to_persian:
                translated.append(self.english_to_persian[word_lower])
            elif word_lower:
                translated.append(word)

        return ' '.join(translated)

    def clean_urls(self, text):
        """حذف یا جایگزینی لینکها"""
        text = re.sub(r'http\S+|www\S+|https\S+', '[LINK]', text, flags=re.MULTILINE)
        return text

    def clean_emails(self, text):
        """حذف ایمیلها"""
        text = re.sub(r'\S+@\S+', '[EMAIL]', text)
        return text

    def clean_phones(self, text):
        """حذف شماره تلفنها"""
        text = re.sub(r'(\+98|0)?9\d{9}', '[PHONE]', text)
        return text

    def clean_preprocess_complete(self, text):
        """
        تابع اصلی - همه مراحل preprocessing رو یکجا انجام میده
        """
        if not isinstance(text, str):
            return ""

        # مرحله 1: نرمالسازی یونیکد
        text = self.normalize_unicode(text)

        # مرحله 2: تشخیص و ترجمه انگلیسی
        if self.is_english(text):
            text = self.translate_english_to_persian(text)

        # مرحله 3: تشخیص و تبدیل فینگلیش
        if self.is_finglish(text):
            text = self.convert_finglish_to_persian(text)

        # مرحله 4: نرمالسازی فارسی
        text = self.normalize_persian(text)

        # مرحله 5: حذف ایموجیها
        text = self.remove_emojis(text)

        # مرحله 6: پاکسازی لینکها، ایمیلها، تلفنها
        text = self.clean_urls(text)
        text = self.clean_emails(text)
        text = self.clean_phones(text)

        # مرحله 7: حذف علائم نگارشی
        text = self.remove_punctuations(text)

        # مرحله 8: حذف اعداد
        text = self.remove_numbers(text)

        # مرحله 9: حذف حروف انگلیسی (اگه باقی مونده)
        text = self.remove_english_letters(text)

        # مرحله 10: حذف فاصلههای اضافی
        text = self.remove_extra_spaces(text)

        # مرحله 11: حذف کلمات تک حرفی
        text = self.remove_single_characters(text)

        # مرحله 12: حذف کلمات بیمعنی (stopwords)
        text = self.remove_stopwords(text)

        # مرحله 13: پاکسازی نهایی
        text = self.remove_extra_spaces(text)

        return text


# ایجاد نمونه از کلاس
preprocessor = CommentPreprocessor()
print("✅ Preprocessor loaded successfully! (Using manual stopwords)")
🇮🇷 Persian Sentiment Analysis (Machine Learning + Django)

A complete Persian Sentiment Analysis project built with Python, Scikit-learn, and Django.

The project is divided into two main phases:

1. Machine Learning Pipeline (Jupyter Notebook)
2. Deployment as a Django Web Application

The model is trained on 2,400 Persian SnappFood reviews and classifies each review into one of two sentiment classes:

Label| Sentiment
0| Positive (Happy 😊)
1| Negative (Sad 😞)

The web application supports Persian text, performs the same preprocessing used during training, predicts sentiment, and provides confidence scores for both classes.

---

🎥 Demo

«Demo Video: (Coming Soon)»

[ Add your demo video here ]

---

✨ Features

Machine Learning

- Data cleaning
  
  - Remove duplicate records
  - Remove empty rows

- Persian text preprocessing
  
  - Normalization
  - Emoji removal
  - URL removal
  - Finglish removal
  - Stopword removal

- Feature Extraction
  
  - CountVectorizer
  - TF-IDF Vectorizer

- Machine Learning Models
  
  - Logistic Regression ✅ (Best Model)
  - K-Nearest Neighbors (KNN)
  - Decision Tree
  - Random Forest

- Evaluation Metrics
  
  - Accuracy
  - Precision
  - Recall
  - F1-Score

- Export trained model using Pickle

---

Django Application

- Load trained model and vectorizer
- Apply identical preprocessing pipeline
- Single text prediction
- Batch prediction
- Positive & Negative probability scores
- Local prediction history
- CSV export
- Responsive UI
- Smooth animations
- Dark theme

---

🧠 Machine Learning Workflow

                    SnappFood Reviews
                            │
                            ▼
                    Data Cleaning
          (Duplicates + Empty Records)
                            │
                            ▼
                Persian Preprocessing
      ┌──────────────────────────────────┐
      │ • Normalization                  │
      │ • Remove Emojis                  │
      │ • Remove URLs                    │
      │ • Remove Finglish                │
      │ • Remove Stopwords               │
      └──────────────────────────────────┘
                            │
                            ▼
                 Feature Extraction
             ┌──────────────┬──────────────┐
             │              │
             ▼              ▼
      CountVectorizer      TF-IDF
             │              │
             └──────┬───────┘
                    ▼
             Train ML Models
     ┌────────────────────────────────┐
     │ Logistic Regression            │
     │ KNN                            │
     │ Decision Tree                  │
     │ Random Forest                  │
     └────────────────────────────────┘
                    │
                    ▼
              Model Evaluation
                    │
                    ▼
         Export Pickle Files (.pkl)
                    │
                    ▼
             Django Web Application
                    │
                    ▼
             Real-time Predictions

---

📊 Model Comparison

Model| Accuracy| Precision| Recall| F1-Score
Logistic Regression| 82%| —| —| —
KNN| —| —| —| —
Decision Tree| —| —| —| —
Random Forest| —| —| —| —

«Replace the remaining values with your evaluation results.»

---

📂 Project Structure

Persian-Sentiment-Analysis/
│
├── notebooks/
│   ├── sentiment_analysis.ipynb
│   └── dataset.csv
│
├── models/
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── django_app/
│   ├── manage.py
│   ├── app/
│   ├── templates/
│   ├── static/
│   └── requirements.txt
│
├── screenshots/
│
├── README.md
└── LICENSE

---

🚀 Quick Start

Clone the Repository

git clone https://github.com/yourusername/Persian-Sentiment-Analysis.git

cd Persian-Sentiment-Analysis

---

Install Requirements

pip install -r requirements.txt

---

Run Django

python manage.py migrate

python manage.py runserver

Open your browser:

http://127.0.0.1:8000

---

🖼️ Application Screenshots

Home Page

[ Screenshot Here ]

---

Prediction Result

[ Screenshot Here ]

---

Batch Prediction

[ Screenshot Here ]

---

Prediction History

[ Screenshot Here ]

---

🧪 Dataset

- Source: SnappFood User Reviews
- Language: Persian
- Records: 2,400
- Binary Sentiment Classification

Label| Meaning
0| Positive
1| Negative

---

🛠 Technologies

- Python
- Scikit-learn
- Pandas
- NumPy
- Hazm
- Pickle
- Django
- HTML
- CSS
- JavaScript

---

📈 Future Improvements

- Deep Learning models (LSTM / BiLSTM)
- Transformer-based models (ParsBERT / BERT)
- REST API with Django REST Framework
- Docker support
- User authentication
- PostgreSQL integration
- Deployment on cloud platforms
- Real-time analytics dashboard
- Explainable AI (feature importance and prediction interpretation)

---

📜 License

This project is licensed under the MIT License.

---

👨💻 Author

Kiarash

If you found this project helpful, consider giving it a ⭐ on GitHub.

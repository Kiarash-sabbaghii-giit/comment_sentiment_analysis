<p align="center">
  <img src="assets/banner.png" alt="Persian Sentiment Analysis Banner">
</p>

<h1 align="center">🇮🇷 Persian Sentiment Analysis</h1>

<p align="center">
  <strong>Machine Learning + Django Web Application for Persian Sentiment Classification</strong>
</p>

<p align="center">
A complete end-to-end sentiment analysis project that trains multiple Machine Learning models on Persian SnappFood reviews and deploys the best-performing model as a modern Django web application.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)
![Django](https://img.shields.io/badge/Django-Framework-green?logo=django)
![License](https://img.shields.io/badge/License-MIT-blue)

</p>

---

# 🎥 Demo

<div align="center">

### 🚀 See the Application in Action

A quick walkthrough of the complete workflow, including:

✅ Real-time sentiment prediction  
✅ Batch prediction  
✅ Probability visualization  
✅ Prediction history  
✅ CSV export  
✅ Responsive dark-themed UI

<br>

<img src="demo/demo.gif" alt="Application Demo" width="100%">

</div>

---

# 📖 About the Project

This project demonstrates a complete **Persian Sentiment Analysis** pipeline, starting from data preprocessing and Machine Learning experiments to deploying the trained model as a modern Django web application.

The model was trained using **2,400 Persian SnappFood reviews** and performs binary sentiment classification.

| Label | Sentiment |
|:-----:|-----------|
| **0** | Positive (Happy 😊) |
| **1** | Negative (Sad 😞) |

The application fully supports **Persian text** and applies the same preprocessing pipeline used during training before making predictions.

---

# ✨ Features

## 🤖 Machine Learning

- Data Cleaning
  - Remove duplicate records
  - Remove empty records

- Persian Text Preprocessing
  - Text normalization
  - Emoji removal
  - URL removal
  - Finglish removal
  - Stopword removal

- Feature Extraction
  - CountVectorizer
  - TF-IDF Vectorizer

- Machine Learning Models
  - Logistic Regression ✅
  - K-Nearest Neighbors (KNN)
  - Decision Tree
  - Random Forest

- Evaluation Metrics
  - Accuracy
  - Precision
  - Recall
  - F1-Score

- Export trained model and vectorizer using Pickle

---

## 🌐 Django Web Application

- Load trained model and vectorizer
- Apply identical preprocessing pipeline
- Single prediction mode
- Batch prediction mode
- Positive & Negative confidence scores
- Local prediction history
- CSV export
- Responsive design
- Smooth animations
- Dark mode interface

---

# 🔄 Project Workflow

```text
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
```

---

# 📊 Model Comparison

| Model | Accuracy | Precision | Recall | F1-Score |
|--------|:--------:|:---------:|:------:|:--------:|
| Logistic Regression | **82%** | — | — | — |
| K-Nearest Neighbors | — | — | — | — |
| Decision Tree | — | — | — | — |
| Random Forest | — | — | — | — |

> Replace the remaining values with your evaluation results.

---

# 📁 Project Structure

```text
Persian-Sentiment-Analysis/
│
├── assets/
│   ├── banner.png
│   ├── home.png
│   ├── prediction.png
│   ├── batch.png
│   └── history.png
│
├── demo/
│   └── demo.gif
│
├── notebooks/
│   └── sentiment_analysis.ipynb
│
├── models/
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── django_app/
│
├── requirements.txt
│
└── README.md
```

---

# 🚀 Quick Start

### Clone the Repository

```bash
git clone https://github.com/yourusername/Persian-Sentiment-Analysis.git

cd Persian-Sentiment-Analysis
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Django

```bash
python manage.py migrate

python manage.py runserver
```

Open your browser:

```
http://127.0.0.1:8000
```

---

# 🖼️ Application Screenshots

## 🏠 Home Page

![Home](assets/home.png)

---

## 🔍 Prediction Result

![Prediction](assets/prediction.png)

---

## 📂 Batch Prediction

![Batch](assets/batch.png)

---

## 📜 Prediction History

![History](assets/history.png)

---

# 📊 Dataset

| Property | Value |
|----------|-------|
| Dataset | SnappFood Reviews |
| Language | Persian |
| Samples | 2,400 |
| Classes | Binary Sentiment |

---

# 🛠️ Technologies

- Python
- Scikit-learn
- Pandas
- NumPy
- Hazm
- Pickle
- Django
- HTML5
- CSS3
- JavaScript

---

# 🚀 Future Improvements

- Deep Learning (LSTM / BiLSTM)
- Transformer Models (ParsBERT / BERT)
- REST API with Django REST Framework
- Docker Support
- PostgreSQL Integration
- User Authentication
- Cloud Deployment
- Explainable AI (XAI)
- Interactive Analytics Dashboard

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨💻 Author

**Kiarash**

If you found this project useful, consider giving it a ⭐ on GitHub!

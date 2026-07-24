# 🤖 AI Sentiment Analyzer

A Machine Learning-powered web application that analyzes the sentiment of movie reviews and classifies them as **Positive** or **Negative**.

Built using **Python**, **Scikit-learn**, **FastAPI**, **HTML**, **CSS**, and **JavaScript**.

---

## 🚀 Live Demo

*(Add your Render link here after deployment)*

---

## ✨ Features

- Predicts Positive or Negative sentiment
- Machine Learning model trained on movie reviews
- TF-IDF text vectorization
- Text preprocessing (lowercasing, punctuation removal, stopword removal)
- FastAPI backend
- Clean and responsive user interface
- Loading spinner during prediction

---

## 🛠 Tech Stack

### Backend
- Python
- FastAPI
- Scikit-learn
- Joblib
- NLTK

### Frontend
- HTML
- CSS
- JavaScript

### Machine Learning
- TF-IDF Vectorizer
- Logistic Regression

---

## 📂 Project Structure

```
sentiment-analysis-api/
│
├── data/
│   └── api/
│       └── main.py
│
├── model/
│   ├── sentiment_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── notebook/
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

```bash
git clone <your-repository-url>

cd sentiment-analysis-api

python -m venv .venv

.\.venv\Scripts\activate

pip install -r requirements.txt
```

---

## ▶️ Run the application

```bash
python -m uvicorn data.api.main:app --reload
```

Open:

```
http://127.0.0.1:8000
```

---

## 🧠 Model Workflow

1. User enters a movie review
2. Text preprocessing
3. TF-IDF vectorization
4. Sentiment prediction
5. Display result in the web application

---

## 📈 Future Improvements

- Confidence score
- Multi-language sentiment analysis
- Transformer-based models (BERT)
- Docker support
- Cloud deployment

---

## 👨‍💻 Author

**Habeeb Urooj**

LinkedIn:
(Add LinkedIn URL)

GitHub:
(Add GitHub URL)
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import re
import string
from nltk.corpus import stopwords

app = FastAPI(title="Sentiment Analysis API")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

model = joblib.load("model/sentiment_model.pkl")
vectorizer = joblib.load("model/tfidf_vectorizer.pkl")

class Review(BaseModel):       
    review: str
#Create a function to clean the text data
stop_words = set(stopwords.words('english'))
def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r"<.*?>", "", text)  # Remove HTML tags
    text = text.translate(str.maketrans("", "", string.punctuation))  # Remove punctuation
    text = re.sub(r"\d+", "", text)  # Remove numbers
    text = re.sub(r"\s+", " ", text).strip()  # Remove extra whitespace 
    
    #remove stop words
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)    
    

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.post("/predict")
def predict(review: Review):
    text = clean_text(review.review)
    vector = vectorizer.transform([text])

    prediction = model.predict(vector)[0]

    return {
        "review": text,
        "prediction": prediction
    }
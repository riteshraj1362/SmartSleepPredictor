# Smart Sleep Predictor

A machine learning project that predicts a person's sleep condition based on lifestyle and health parameters.

## 🔧 Tech Stack

* Python
* Scikit-Learn
* Pandas
* Streamlit
* Joblib

## 📌 How to Run Locally

```
pip install -r requirements.txt
streamlit run app.py
```

## 🎯 Features

* Predicts sleep condition based on Age, BMI, Stress Level, and Sleep Duration
* Fully interactive web app
* Easy to deploy and extend

## 🚀 Files in this Project

* **Sleep_Health_and_Lifestyle_Predication_with_94_Ac.ipynb** – model training + EDA
* **app.py** – Streamlit web app
* **sleep_model.pkl** – saved ML model
* **requirements.txt** – dependencies for deployment

## 🧠 Model Overview

The model uses lifestyle and health parameters to predict sleep condition.
Features include:

* Age
* Stress Level
* BMI
* Sleep Duration

## 📦 Deployment (Streamlit Cloud)

1. Push code to GitHub
2. Go to Streamlit Cloud
3. Select this repo
4. Choose `app.py`
5. Deploy

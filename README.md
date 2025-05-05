# 🌾 Smart Crop Recommendation System

This project is a machine learning-based web application that recommends the most suitable crop to cultivate based on soil and weather conditions. Built using Flask and scikit-learn.

---

## 🚀 Features

- Predicts the best crop based on:
  - Nitrogen (N)
  - Phosphorus (P)
  - Potassium (K)
  - Temperature
  - Humidity
  - pH
  - Rainfall
- Simple user-friendly web interface using HTML
- Trains a model using Random Forest (or loads a pre-trained one)

---

## 📁 Project Structure
smart-crop-recommendation/
│
├── app.py # Flask app with ML logic
├── crop_recommendation.csv # Dataset
├── model.pkl # Saved model (auto-created)
├── index.html # Web UI
└── requirements.txt # Python dependencies

---

## ⚙️ How to Run

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
python app.py
http://127.0.0.1:5000/
📊 Dataset
Source: Kaggle or AICTE Internship-provided data

Format: CSV with columns — N, P, K, temperature, humidity, ph, rainfall, label

🛠 Technologies Used
Python

Flask

scikit-learn

HTML/CSS

👨‍💻 Author
Name: Kavya Ulleru

Internship: AICTE Azure Internship 2025

📄 License
This project is for academic and learning purposes.
# crop-recommendation

Demonstration of project (📹 YouTube Link):
https://youtu.be/Ut-2uPALV2A?si=6lFJPKhsicB8Yv_u
# 🫀 Heart Disease Risk Prediction 

An intelligent Machine Learning web application that predicts heart disease risk levels and provides real-time healthcare resources, including live health news and nearby hospital locations.

## 🔍 Project Highlights

- ✅ **Heart Disease Risk Classifier**  
  Trained a **Random Forest** model on 1200+ real patient records to predict whether an individual is at risk of heart disease.

- 📰 **Live Health News Integration**  
  Integrated the **News API** to display the latest 10+ health-related news articles dynamically.

- 🏥 **Hospital Locator**  
  Mapped 100+ nearby hospitals using the **OpenCage Geocoding API** based on user location.

- ⚙️ **Optimized RESTful Architecture**  
  Designed modular Flask-based API endpoints with up to **25% improvement in response time**.

---

## 🛠️ Tech Stack

| Component       | Tech Used                                |
|----------------|--------------------------------------------|
| Backend         | Python, Flask, REST API                   |
| Machine Learning| Random Forest (scikit-learn)              |
| Frontend        | HTML5, CSS3                               |
| APIs Used       | News API, OpenCage Geocoding API          |
| Deployment      | Localhost / (optionally Heroku, Render)   |

---

## 📁 Directory Structure
```bash
Heart-Disease-Prediction/
├── app.py                        # Flask backend application
├── model/
│   └── rf_model.pkl              # Trained Random Forest model
├── templates/
│   └── index.html                # Frontend template for user input & results
├── static/
│   ├── css/
│   │   └── style.css             # Custom styles
│   └── images/                   # Screenshots or UI assets
├── utils/
│   ├── news_api.py               # News API integration script
│   └── map_api.py                # OpenCage API script for hospital mapping
├── data/
│   └── heart1.csv                # Cleaned dataset for model training
├── Heart_disease_prediction.ipynb # Notebook for training & visualizations
├── requirements.txt             # Project dependencies
└── README.md                    
```
## 🚀 How to Run

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/umayashaswi/Heart-Disease-Prediction.git
cd Heart-Disease-Prediction
```
### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
🔐 Also, set up your API keys for News API and OpenCage.
```
### 3️⃣ Run the Flask App
```bash
python app.py
```
## 💡 Features
🔍 Predicts heart disease risk with high accuracy

🌐 Displays real-time health news

📍 Finds hospitals near user location

📊 Clean and responsive UI

⚡ Fast API response via RESTful architecture


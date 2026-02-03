# 🩺 Diabetes Prediction System

A Machine Learning–based web application that predicts the likelihood of diabetes with a **confidence score** and **medical-safe decision logic**.

The system uses a trained ML model and provides user-friendly predictions through a **Streamlit web app**.

---

## 🚀 Features

- Predicts diabetes risk based on medical input parameters
- Confidence score shown with every prediction
- Special **uncertain range handling (0.4 – 0.7 threshold)**:
  - Advises users to consult a doctor for better diagnosis
- Clean and interactive Streamlit UI
- Model trained and evaluated using proper ML practices

---

## 🧠 Machine Learning Details

- **Model Used:** Logistic Regression  
- **Threshold:** 0.4 (to reduce false negatives – medical safety)
- **Evaluation Metrics:**
  - Accuracy
  - Recall (priority metric)
  - F1-Score

> Logistic Regression was selected because it achieved the **highest recall**, making it safer for medical prediction tasks.

---

## 📊 Input Features

The model takes the following inputs:

1. Pregnancies  
2. Glucose  
3. Blood Pressure  
4. Skin Thickness  
5. Insulin  
6. BMI  
7. Diabetes Pedigree Function  
8. Age  

---

## 🖥️ Web Application (Streamlit)

Users can:
- Enter medical details
- Get prediction result:
  - **Not Diabetic (Low Risk)**
  - **Uncertain Result – Consult Doctor**
  - **Likely Diabetic (High Risk)**
- View confidence percentage

---

## 🛠️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Joblib
- Git & GitHub

---

## ▶️ How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/princekr-rajput/diabetes_prediction.git
cd diabetes_prediction
```

2️⃣ Create virtual environment 
```bash
python -m venv venv
```

3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

4️⃣ Run the application
```bash
 streamlit run app.py
```

📁 Project Structure
```bash
diabetes_prediction/
├── app.py
├── diabetes.ipynb
├── diabetes_model.pkl
├── diabetes_scaler.pkl
├── requirements.txt
└── README.md
```

⚠️ Disclaimer

This project is developed for educational purposes only.
It is not a substitute for professional medical advice.
Always consult a qualified healthcare provider for diagnosis.

👤 Author

Prince Kumar Rajput
GitHub: https://github.com/princekr-rajput

⭐ If you find this project helpful, please consider starring the repository.

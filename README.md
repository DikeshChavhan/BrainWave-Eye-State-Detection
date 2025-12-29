# 🧠 BrainWave — EEG Eye-State Detection  
🔗 **Live Streamlit App:** https://brainwave-eye-state-detection-project-dikeshchavhan123.streamlit.app/

---

## 📌 Project Overview
This project predicts whether a person’s **eyes are Open (0) or Closed (1)** using EEG (Electroencephalogram) signal features.  
It applies **Machine Learning and Signal Processing techniques** to classify eye-state based on brain-wave activity.

The project includes:
- Data preprocessing & feature scaling  
- Random Forest classification model  
- Streamlit web application for real-time predictions  
- CSV upload mode & manual EEG input mode  

---

## 🎯 Use-Case Applications
- ⚙️ Brain-Computer Interface (BCI)  
- 🧑‍⚕️ Biomedical & Cognitive Studies  
- 🚗 Drowsiness / Fatigue Monitoring  
- 🧠 Neuro-signal pattern analysis  

---

## 📂 Repository Structure

BrainWave-Eye-State-Detection/
├── app.py # Streamlit web app
├── eeg_eye_rf_model.pkl # Trained Random Forest model
├── scaler.pkl # Feature scaling object
├── notebook.ipynb # Model training notebook (optional)
├── requirements.txt # Dependencies
└── README.md # Project documentation

---

## 🚀 How to Run the Project Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR-USERNAME/BrainWave-Eye-State-Detection.git
cd BrainWave-Eye-State-Detection
```

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit App
streamlit run app.py


The app will open in your browser at:

http://localhost:8501

---
🧠 Model Details

Algorithm: Random Forest Classifier

Features: 14 EEG channels

Target:

  0 → Eyes Open

  1 → Eyes Closed

Feature scaling is performed using StandardScaler, and both the trained model and scaler are stored as .pkl files.

---

🖥️ Streamlit App Features

📂 Upload EEG CSV for batch prediction

✍️ Manual EEG value entry mode

📊 Prediction summary visualization

⚡ Fast & lightweight inference

---

🛠 Technologies Used

Python

Scikit-Learn

Pandas / NumPy

Streamlit

Joblib

Matplotlib

---

🙌 Author
Dikesh Chavhan

---

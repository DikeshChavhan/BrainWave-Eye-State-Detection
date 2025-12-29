import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

st.set_page_config(page_title="EEG Eye-State Detection", layout="wide")

st.title("🧠 EEG Eye-State Detection App")
st.write("Predict whether eyes are **Open (0)** or **Closed (1)** using EEG signal features.")

# Load model + scaler
@st.cache_resource
def load_model():
    model = joblib.load("eeg_eye_rf_model.pkl")
    scaler = joblib.load("scaler.pkl")
    return model, scaler

model, scaler = load_model()

st.sidebar.header("Input Options")
mode = st.sidebar.radio("Choose Input Mode", ["Upload CSV", "Manual Entry"])

# ─────────────────────────────
# Upload CSV Mode
# ─────────────────────────────
if mode == "Upload CSV":
    file = st.sidebar.file_uploader("Upload EEG CSV", type=["csv"])

    if file:
        df = pd.read_csv(file)

        st.subheader("📂 Uploaded Data")
        st.dataframe(df.head())

        X = scaler.transform(df)
        preds = model.predict(X)

        df["Prediction"] = preds

        st.subheader("📊 Predictions")
        st.dataframe(df)

        st.bar_chart(df["Prediction"].value_counts())

        st.success("Prediction completed successfully ✔️")

# ─────────────────────────────
# Manual Input Mode
# ─────────────────────────────
else:
    st.subheader("📝 Manual EEG Input")

    features = []
    cols = st.columns(2)

    for i in range(14):
        with cols[i % 2]:
            value = st.number_input(f"EEG Channel {i+1}", value=0.0)
            features.append(value)

    if st.button("Predict Eye State"):
        X = scaler.transform([features])
        pred = model.predict(X)[0]

        if pred == 0:
            st.success("👁 Eyes Open")
        else:
            st.error("😴 Eyes Closed / Drowsy State Detected")

        st.info("Prediction completed ✔️")

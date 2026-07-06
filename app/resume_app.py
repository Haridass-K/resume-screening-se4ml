import streamlit as st
import joblib
import re
import string

from commands import create_database, save_prediction
from queries import view_history

MODEL_PATH = "models/resume_screening_model.pkl"


# -----------------------------
# Resume Cleaning Function
# -----------------------------
def clean_resume(text):
    text = str(text)
    text = re.sub(r"http\S+|www\S+", " ", text)
    text = re.sub(r"\S+@\S+", " ", text)
    text = re.sub(r"\d+", " ", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\s+", " ", text)
    return text.lower().strip()


# -----------------------------
# Streamlit Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Resume Screening System",
    page_icon="📄",
    layout="wide"
)

st.title("AI-Powered Resume Screening and Job Role Prediction System")

st.write(
    "This application predicts the most suitable job category "
    "based on resume content using Machine Learning."
)


# -----------------------------
# Initialize Database
# -----------------------------
create_database()


# -----------------------------
# Load ML Model
# -----------------------------
model = joblib.load(MODEL_PATH)


# -----------------------------
# Sidebar Navigation
# -----------------------------
menu = st.sidebar.radio(
    "Navigation",
    [
        "Predict Job Category",
        "Prediction History"
    ]
)


# =====================================================
# Prediction Page
# =====================================================

if menu == "Predict Job Category":

    st.header("Resume Screening")

    resume_text = st.text_area(
        "Paste Resume Text",
        height=300,
        placeholder="Paste candidate resume here..."
    )

    if st.button("Predict Job Category"):

        if resume_text.strip() == "":
            st.warning("Please enter resume text.")

        else:

            cleaned_text = clean_resume(resume_text)

            prediction = model.predict([cleaned_text])[0]

            confidence = 0.0

            if hasattr(model, "predict_proba"):
                confidence = (
                    model.predict_proba([cleaned_text]).max() * 100
                )

            st.success(
                f"Predicted Job Category : {prediction}"
            )

            if confidence > 0:
                st.metric(
                    "Prediction Confidence",
                    f"{confidence:.2f}%"
                )

            save_prediction(
                resume_text,
                prediction,
                confidence
            )

            st.info(
                "Prediction saved successfully."
            )


# =====================================================
# Prediction History Page
# =====================================================

elif menu == "Prediction History":

    st.header("Prediction History")

    history = view_history()

    if len(history) == 0:

        st.info(
            "No prediction history available."
        )

    else:

        st.table(
            {
                "ID": [row[0] for row in history],
                "Predicted Category": [row[1] for row in history],
                "Confidence (%)": [round(row[2], 2) for row in history],
                "Prediction Time": [row[3] for row in history],
            }
        )
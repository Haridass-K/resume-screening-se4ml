# AI-Powered Resume Screening and Job Role Prediction System

## Course
AIMLCZG546 - Software Engineering for Machine Learning  
Assignment I

## Project Overview
This project implements a machine learning based Resume Screening and Job Role Prediction System. The application classifies resume text into suitable job categories using Natural Language Processing and supervised machine learning.

## Dataset
The project uses a resume dataset containing resume text and job category labels.

## Technologies Used
- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorizer
- Random Forest Classifier
- Streamlit
- SQLite
- Joblib
- Jupyter Notebook

## Architectural Patterns Implemented
1. Pipe-and-Filter Architecture  
2. Command Query Responsibility Segregation (CQRS)

## Application Features
- Resume text input
- Job category prediction
- Prediction confidence score
- SQLite prediction history
- Streamlit user interface

## How to Run

```bash
conda activate resume-screening
streamlit run app/resume_app.py
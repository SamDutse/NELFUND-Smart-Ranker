import pandas as pd
import streamlit as st
import cloudpickle

from joblib import load

# Load the trained pipeline
try:
    pipeline = load("student_loan_pipeline.joblib")
    st.success("Model loaded successfully!")
except Exception as e:
    st.error(f"Error loading model: {e}")
    pipeline = None

# Streamlit app title
st.title("Student Loan Priority Predictor")
st.sidebar.header("Input Features")

# Sidebar for user inputs
attendance_rate = st.sidebar.slider("Attendance Rate (%)", 0, 100, 75)
grades = st.sidebar.slider("Grades (0-100)", 0, 100, 65)
distance_to_school = st.sidebar.slider("Distance to School (km)", 0, 50, 10)
socioeconomic_status = st.sidebar.selectbox("Socioeconomic Status", ["Low", "Middle", "High"])
parent_education_level = st.sidebar.selectbox(
    "Parent Education Level", ["No High School", "High School", "Bachelor's", "Postgraduate"]
)
school_resources = st.sidebar.selectbox("School Resources", ["Low", "Medium", "High"])
behavioral_issues = st.sidebar.selectbox("Behavioral Issues", ["No", "Yes"])

# Create a DataFrame from user inputs
user_data = pd.DataFrame({
    "Attendance_Rate": [attendance_rate],
    "Grades": [grades],
    "Distance_to_School": [distance_to_school],
    "Socioeconomic_Status": [socioeconomic_status],
    "Parent_Education_Level": [parent_education_level],
    "School_Resources": [school_resources],
    "Behavioral_Issues": [behavioral_issues],
})

# Display user inputs
st.subheader("User Input Data")
st.write(user_data)

# Predict high-priority status if the pipeline is loaded
if st.button("Predict Loan Priority"):
    if pipeline:
        try:
            prediction = pipeline.predict(user_data)
            prediction_proba = pipeline.predict_proba(user_data)
            priority_status = "High Priority" if prediction[0] == 1 else "Low Priority"
            st.subheader("Prediction Result")
            st.write(f"Loan Priority Status: **{priority_status}**")
            st.write(f"Confidence: {max(prediction_proba[0]) * 100:.2f}%")
        except Exception as e:
            st.error(f"Error making prediction: {e}")
    else:
        st.error("Pipeline not loaded. Please check the model file.")

# Footer
st.markdown("This application predicts the priority ranking for student loan applicants based on their socioeconomic data.")

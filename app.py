import pandas as pd
import joblib
import streamlit as st

# Load the trained pipeline
# pipeline = joblib.load("student_loan_pipeline.pkl")
import cloudpickle
with open("student_loan_pipeline.pkl", "rb") as file:
    pipeline = cloudpickle.load(file)


# Streamlit app title
st.title("Student Loan Priority Predictor")

# Sidebar for user inputs
st.sidebar.header("Input Features")
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

# Predict high-priority status
if st.button("Predict Loan Priority"):
    prediction = pipeline.predict(user_data)
    prediction_proba = pipeline.predict_proba(user_data)
    priority_status = "High Priority" if prediction[0] == 1 else "Low Priority"
    st.subheader("Prediction Result")
    st.write(f"Loan Priority Status: **{priority_status}**")
    st.write(f"Confidence: {max(prediction_proba[0]) * 100:.2f}%")

# Footer
st.markdown("This application predicts the priority ranking for student loan applicants based on their socioeconomic data.")

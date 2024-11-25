import pandas as pd
import joblib
import streamlit as st

# Load the trained pipeline
pipeline = joblib.load("student_loan_pipeline_with_probs.pkl")

# Streamlit app
st.title("Student Loan Approval Predictor with Probabilities")

# User inputs
st.sidebar.header("Input Features")
student_age = st.sidebar.slider("Student Age", 18, 35, 25)
year_of_study = st.sidebar.slider("Year of Study", 1, 5, 3)
gpa = st.sidebar.slider("GPA (0-5.0)", 2.0, 5.0, 3.5)
household_income = st.sidebar.slider("Household Income (NGN)", 50000, 1000000, 250000)
dependents = st.sidebar.slider("Dependent Family Members", 0, 6, 2)
gender = st.sidebar.selectbox("Gender", ["Male", "Female", "Other"])
school_name = st.sidebar.selectbox(
    "School Name", ["University_A", "University_B", "Polytechnic_C", "College_D"]
)
program_of_study = st.sidebar.selectbox(
    "Program of Study", ["Engineering", "Medicine", "Business", "Humanities", "Social Sciences"]
)
socioeconomic_status = st.sidebar.selectbox("Socioeconomic Status", ["Low", "Middle", "High"])
employment_status = st.sidebar.selectbox("Employment Status", ["Unemployed", "Part-time", "Full-time"])
extra_curricular = st.sidebar.selectbox("Extra-Curricular Involvement", ["High", "Medium", "Low"])
previous_loan = st.sidebar.selectbox("Previous Loan Status", ["Yes", "No"])
academic_rating = st.sidebar.selectbox(
    "Academic Performance Rating", ["Excellent", "Good", "Average", "Poor"]
)
special_needs = st.sidebar.selectbox("Special Needs", ["Yes", "No"])
campus_residence = st.sidebar.selectbox("Campus Residence", ["Yes", "No"])
parent_education = st.sidebar.selectbox("Parental Education Level", ["Primary", "Secondary", "Tertiary"])
volunteer_work = st.sidebar.selectbox("Volunteer Work", ["High", "Medium", "Low"])

# Create input DataFrame
user_data = pd.DataFrame({
    "Student_Age": [student_age],
    "Year_of_Study": [year_of_study],
    "GPA": [gpa],
    "Household_Income": [household_income],
    "Dependent_Family_Members": [dependents],
    "Gender": [gender],
    "School_Name": [school_name],
    "Program_of_Study": [program_of_study],
    "Socioeconomic_Status": [socioeconomic_status],
    "Employment_Status": [employment_status],
    "Extra_Curricular_Involvement": [extra_curricular],
    "Previous_Loan_Status": [previous_loan],
    "Academic_Performance_Rating": [academic_rating],
    "Special_Needs": [special_needs],
    "Campus_Residence": [campus_residence],
    "Parental_Education_Level": [parent_education],
    "Volunteer_Work": [volunteer_work],
})

# Predict loan approval probabilities
if st.button("Predict Loan Approval Probability"):
    probability = pipeline.predict_proba(user_data)[0, 1]  # Probability for approval
    st.subheader("Prediction Result")
    st.write(f"Loan Approval Probability: **{probability * 100:.2f}%**")

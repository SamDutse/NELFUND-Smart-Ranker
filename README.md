# NELFUND Smart Ranker  
**NELFUND Smart Ranker** is an AI-powered application designed to automate the evaluation and ranking of student loan applications for the Nigeria Education Loan Fund (NELFUND). This system predicts loan eligibility and ranks applicants based on their likelihood of approval, ensuring a fair and efficient allocation of education loans.

---

## Features  
- **Loan Eligibility Prediction:**  
  Uses machine learning to predict whether a student qualifies for a loan.  

- **Ranking System:**  
  Ranks applicants based on their probability of approval, enabling the selection of the most deserving candidates.  

- **Customizable Parameters:**  
  Allows institutions to set thresholds or limits for loan approvals.  

- **Interactive User Interface:**  
  Deployed with Streamlit, enabling easy access and use for administrators and decision-makers.  

---

## Dataset  
The model was trained on a synthetic dataset representing loan application details. Key features include:  
- **Student Attributes:** Age, Gender, Academic Performance, GPA, Year of Study, etc.  
- **Financial Information:** Household Income, Loan Amount Requested, Socioeconomic Status.  
- **Other Factors:** Extra-curricular involvement, Previous Loan Status, Parental Education Level, Volunteer Work.  

---

## Technology Stack  
- **Programming Language:** Python  
- **Machine Learning Libraries:** Scikit-learn, Pandas, NumPy  
- **Web Framework:** Streamlit  
- **Model Deployment:** Pickle for saving the trained pipeline  

---

## Installation  
1. Clone this repository:  
   ```bash
   git clone https://github.com/yourusername/nelfund-smart-ranker.git
   cd nelfund-smart-ranker
   ```  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  

3. Run the application:  
   ```bash
   streamlit run app.py
   ```  

---

## How It Works  
1. **Model Training:**  
   - Preprocesses the dataset using pipelines (numeric and categorical transformations).  
   - Trains a machine learning model (Random Forest) for classification.  

2. **Deployment:**  
   - The trained model is saved and integrated into a Streamlit app.  
   - The app allows administrators to input applicant details and view predictions.  

3. **Rank Generation:**  
   - Sorts applicants by eligibility probability and generates a ranked list.  
   - Selects the top X candidates based on available funding or institutional policies.  

---

## Usage  
- **Step 1:** Open the Streamlit app.  
- **Step 2:** Enter the required applicant details in the form provided.  
- **Step 3:** Predict eligibility and view the probability score.  
- **Step 4:** Generate a ranked list of applicants based on their scores.  

---

## Contribution  
Feel free to fork this repository and submit pull requests to enhance the functionality or improve the system.  

---

## License  
This project is licensed under the [Bluehouse Technologies Ltd License](https://www.bluehouseng.com/).

---

## Acknowledgments  
Special thanks to the Nigeria Education Loan Fund (NELFUND) initiative for inspiring this project.  

---  

**Start using the NELFUND Smart Ranker today to revolutionize student loan allocation!**  

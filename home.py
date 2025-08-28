import streamlit as st

# Customizing the page
st.set_page_config(page_title="Home", page_icon=":material/home:")

# Main Title
st.markdown("<h1 style='text-align: center; color: black;'>Mulitple Linear Regression</h1>", unsafe_allow_html=True)
# Text explaining the function of the program
st.write("In this program we are going to preprocess a data about Students' performance, do some exploratory data analysis and train a linear regression model on it.")
st.write("Also, we are going to help the user\student to predict the performance based on attributes he\she inputs into the program.")
st.divider()
# Explaining the data set
st.header("Features:")
st.write("**Hours Studied:** The total number of hours spent studying by each student.")
st.write("**Previous Scores:** The scores obtained by students in previous tests.")
st.write("**Extracurricular Activities:** Whether the student participates in extracurricular activities (Yes or No).")
st.write("**Sleep Hours:** The average number of hours of sleep the student had per day.")
st.write("**Sample Question Papers Practiced:** The number of sample question papers the student practiced.")
st.header("Target Variable:")
st.write("**Performance Index:** A measure of the overall performance of each student. The performance index represents the student's " \
"academic performance and has been rounded to the nearest integer. The index ranges from 10 to 100, with higher values indicating better performance.")
st.divider()

# To control the buttons' positions
col1, col2, col3, col4, col5=st.columns(5)
with col3:
    prep_eda = st.button("Preprocessing and EDA", type="primary")
# Once the button pressed move to the next page
if prep_eda:
    st.switch_page("pages/preprocess_eda.py")
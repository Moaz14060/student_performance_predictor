import streamlit as st
import numpy as np

# Customizing the page
st.set_page_config(page_title="Predictions", page_icon=":material/online_prediction:")

if 'shared_variable2' not in st.session_state:
    st.session_state["shared_variable2"] = None

# To make the model visible in this page
lr_model = st.session_state['shared_variable2']

# Main Title
st.markdown("<h1 style='text-align: center; color: black;'>Predicting Outcomes</h1>", unsafe_allow_html=True)

# Slider for determining the studied hours
hours_studied = st.slider("Select how many hours you studied:", 0, 12, 6)

# Slider for picking the previous score
previous_score = st.slider("Select your previous score:", 0, 100, 50)

# Radio button for seeing if the student does extracurricular activities or not
extracurricular_activities=st.radio("Do you do Extracurricular Activities ?", ["**Yes**", "**No**"])
# To loop over them in a for loop
radio_values=["Yes", "No"]
# To change the string of the radio options to numbers the model can understand
extracurricular_activities = 1 if extracurricular_activities == "**Yes**" else 0

# Slider for determining how many hours the user or student sleeps
sleep_hours = st.slider("How many hours do you sleep on average ?", 4, 12, 7)

# Slider for determining how many papers the student practiced
sample_question_papers_practiced = st.slider("How many sample question papers you practiced ?", 0, 10, 5)

# To control the buttons' positions
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    back = st.button("Go Back", type="secondary", icon=":material/arrow_back:")
with col5:
    home = st.button("Home", type="secondary", icon=":material/home:")
with col3:
    predict=st.button("Predict", type="primary")
# Predict the target value (performance_index) based on the user's inputs
if predict: 
    value = np.ceil(lr_model.predict([[hours_studied, previous_score, extracurricular_activities, sleep_hours, sample_question_papers_practiced]]))
    st.success(f"The predicted performance out of 100: {int(value[0])}")
    # Recomendation System
    if (value < 50) & (sleep_hours <= 6):
        st.warning("Try getting more sleep", icon=":material/sleep_score:")
    if (value < 50) & (sample_question_papers_practiced <= 5):
        st.warning("Try solving more sample question papers", icon=":material/book:")
    if (value < 50) & (hours_studied <= 5):
        st.warning("Try studying for a longer time", icon=":material/schedule:")
# when the student press the button he/she returns to the home page
if home:
    st.switch_page("home.py")
# To go back a page
if back:
    st.switch_page("pages/model.py")








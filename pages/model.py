import streamlit as st

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Customizing the page
st.set_page_config(page_title="Model", page_icon=":material/model_training:")

# Main Title
st.markdown("<h1 style='text-align: center; color: black;'>Model Training</h1>", unsafe_allow_html=True)

# The data frame as shared variable with other pages
df = st.session_state['shared_variable'] 

st.header("Features:")
# Showing the "features" without the target column 
features=df.drop(columns= "performance_index", axis=1)
st.dataframe(features)
st.divider()

st.header("Target Column:")
# Showing the "target" column
target=df.drop(columns= ["hours_studied", "previous_scores", "extracurricular_activities", "sleep_hours", 
                                 "sample_question_papers_practiced"], axis=1)
st.dataframe(target)
st.divider()

# Selecting all the features except the last one
x=df.iloc[:, :-1].values
# Selecting the last feature
y=df.iloc[:, -1].values

# Splitting the data
x_train, x_test, y_train, y_test=train_test_split(x, y, random_state=42, test_size=0.25)

# Finding the parameters
lr_model=LinearRegression().fit(x_train, y_train)
st.session_state['shared_variable2'] = lr_model
# Subtitle
st.header("Parameters")
# Showing the parameters
st.write(f"Intercept (Theta0): {lr_model.intercept_}")
st.write(f"Coefficients (Theta1, Theta2, etc....): {lr_model.coef_}")
st.divider()

# Subtitle
st.header("Evaluation of model")
# Evaluating the training model
r2_train = lr_model.score(x_train, y_train)
st.write("R^2 of Training Model:","{:.0%}".format(r2_train))

# Predicting the test values
y_pred=lr_model.predict(x_test)
# Evaluating the tested model
score=r2_score(y_test, y_pred)
st.write("R^2 of Tested Model:", "{:.0%}".format(score))

# To control the buttons' positions    
col1, col2, col3, col4, col5=st.columns(5)
with col1:
    back= st.button("Go Back", type="secondary", icon=":material/arrow_back:")
with col5:
    home = st.button("Home", type="secondary", icon=":material/home:")
with col3:
    predic = st.button("Make Predictions", type="primary")
# Once the button pressed move to the next page
if predic:
    st.switch_page("pages/prediction.py")
# Once the button pressed move to the previous page  
if back:
    st.switch_page("pages/preprocess_eda.py")
# Once the button pressed move to the home page  
if home:
    st.switch_page("home.py")
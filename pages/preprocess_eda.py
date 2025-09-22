import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Customizing the page
st.set_page_config(page_title="Preprocessing and EDA")

# Main Title
st.markdown("<h1 style='text-align: center; color: black;'>Preprocessing and EDA</h1>", unsafe_allow_html=True)

# A customized pallete with a specific font
my_colors=sns.set_palette("icefire", n_colors=10)
sns.set_theme(style="dark", palette=my_colors, font="Verdana")

# Subtitle
st.header("Data Frame")
st.write("The data of the students' attributes: ")
# Reading the data
df=pd.read_csv("student_performance_predictor/dataset/Student_Performance.csv")

# Showing it as a dataframe in streamlit
st.dataframe(df)
st.divider()

# Subtitle 
st.header("Checking for Null Values")

@st.cache_data
def preprocess_eda(df: pd.DataFrame):
    from utils import check_na
    st.dataframe(check_na(df))
    st.divider()

    # To change the names of the columns
    col_map={"Hours Studied": "hours_studied", "Previous Scores": "previous_scores",
            "Extracurricular Activities": "extracurricular_activities", "Sleep Hours": "sleep_hours",
            "Sample Question Papers Practiced": "sample_question_papers_practiced",
            "Performance Index": "performance_index"}
    df.rename(col_map, inplace=True, axis=1)

    st.header("Renaming Columns")
    # To show what did we change in the columns
    st.write("For easier Processing:")
    col_names=pd.DataFrame({"From": ["Hours Studied", "Previous Scores", "Extracurricular Activities", "Sleep Hours", 
                                    "Sample Question Papers Practiced", "Performance Index"]
                        ,"To": list(df.columns)})
    st.dataframe(col_names)
    st.divider()

    # Encoding categroical values
    df.replace({"extracurricular_activities": {"Yes": 1, "No": 0}}, inplace=True)

    # Checking for duplications
    st.header("Checking for duplications")
    st.write("**Duplicated#** records before dropping them: ", df.duplicated().sum())
    df.drop_duplicates(inplace=True)
    st.write("**Duplicated#** records after dropping them: ", df.duplicated().sum())
    st.divider()

    st.header("Checking for Outliers")
    from utils import boxplot_check
    # Seprating the numerical features from categorical features
    numer_col=numer_col=["hours_studied", "previous_scores", "sleep_hours", "sample_question_papers_practiced", "performance_index"]
    # Checking for outliers
    boxplot_check(df=df, numerical_col=numer_col, color="yellow", figsize=(18, 8))
    st.divider()

    # Visualizing numerical features using histogram
    st.header("Numerical Features' Distribution")
    from utils import numerical_visualization
    numerical_visualization(df=df, numerical_col=numer_col, edgecolor="red")
    st.divider()

    # Visualizing categroical features using countplot
    st.header("Categorical Features' Distribution")
    fig=plt.figure()
    sns.countplot(data=df, x="extracurricular_activities", edgecolor="red")
    plt.xticks(labels=["No", "Yes"], ticks=[0, 1])
    plt.title("Distribution Of Extracurricular Activities")
    plt.suptitle("Categorical Features' Distribution")
    st.pyplot(fig)
    st.divider()
    return df

df = preprocess_eda(df)
# So we can access the data frame from other pages
st.session_state['shared_variable'] = df

st.header("Trying to Find Relations Between Features and Target")
# The choices for the select box
choices=("None", "Performance Index & Previous Score", "Extracurricular Activities & Performance Index", 
         "Sleep Hours & Performance Index", "Sample Question Papers Practiced & Performance Index")
# The select box
select= st.selectbox("Select between these options:", choices)

# To determine which figure to display
if select == "Sample Question Papers Practiced & Performance Index":
    fig = plt.figure()
    sns.barplot(data=df, x="sample_question_papers_practiced", y="performance_index", edgecolor="red")
    plt.title("The Affects of practicing questions on Performance Index")
    st.write(fig)

elif select == "Performance Index & Previous Score":
    fig = plt.figure()
    sns.scatterplot(data=df, x="performance_index", y="previous_scores", hue="hours_studied")
    plt.title("How Previous Scores of the Students Affect the Performance Index")
    st.write(fig)

elif select == "Extracurricular Activities & Performance Index":
    fig = plt.figure()
    sns.barplot(data=df, x="extracurricular_activities", y="performance_index", edgecolor="red")
    plt.title("Does Doing Extracurricular Activities Affect Performance Index")
    plt.xticks(labels=["No", "Yes"], ticks=[0, 1])
    st.write(fig)

elif select == "Sleep Hours & Performance Index":
    fig = plt.figure()
    sns.barplot(data=df, x="sleep_hours", y="performance_index", edgecolor="red")
    plt.title("The Affects of Sleep on Performance Index")
    st.write(fig)

else:
    st.write("You Haven't Selected Anything Yet!")

# To control the buttons' positions
col1, col2, col3, col4, col5=st.columns(5)
with col1:
    back = st.button("Go Back", type="secondary", icon=":material/arrow_back:")
with col3:
    model = st.button("Model", type="primary")
# Once the button pressed move to the next page
if model:
    st.switch_page("pages/model.py")
if back:

    st.switch_page("home.py")

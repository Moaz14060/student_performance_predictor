## Quick Summary of the App:
Creating a streamlit application that can predict students' performance on an exam based on attributes the user enters with a recommendation system to help the student improve their performance.
## Files:
- ### Code Files:
  - **requiremetents.txt**: Contains the neccessary liberaries to download and install.
  - **utitls.py**: Contains the neccessary functions to embed in our code.
- ### dataset:
  - The data frame
- ### .streamlit:
  - To remove the side bar of the app and control other cofigurations.
## The Application Contains **4 Pages**:
  - *1st Page:* **Home** page, which contains the introduction to the app and explains it's purpose and the dataset.
  - *2nd Page:* **Preprocessing and EDA** page, which contains what we did to improve the data and the exploration of the data using visaulaizations.
  - *3rd Page:* **Model** page, which contains the model **(Linear Regression)** that will be trained on the data and showing important values like **(Parameters, Evaluation of model in training and testing)**.
  - *4th Page:* **Prediction** page, which lets the user to choose from a set of values then the model predicts it. If the predeicted value is below a threshold the app gives a recommendation based on the givin values.
#### If you want to see the app you can go to **https://studentperformancepredictor-ckwshba7gwv2peesfem7rj.streamlit.app/**
## Run the app
```bash
# Install dependencies
pip install -r requirements.txt  

# Run the app (replace with your path (your directory/home.py) if not in the same directory)
streamlit run home.py

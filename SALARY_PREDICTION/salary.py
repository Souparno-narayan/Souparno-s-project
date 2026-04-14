import streamlit as st
import pickle
import os
# Ensure the file path is correct   
print (os.getcwd())

with open(r"C:\Users\Souparno Srimany\Downloads\SALARY_PREDICTION (1).pkl", "rb") as f:
  model = pickle.load(f)
    

st.title("SALARY PREDICTION APP")
st.header("PREDICT YOUR SALARY")
st.write("This app predicts the salary based on your job profile.")
st.write("Enter the years of experience below:")

st.markdown("Predicting Salary based on job profile using dicision tree model")
level=st.number_input("Enter your level of job", min_value=1.0, max_value=10.0,step=0.1)

if st.button("Predict your salary"):
    prediction = model.predict([[level]])
    st.success(f"Predicted salary is : {prediction[0]:,.2f}") 
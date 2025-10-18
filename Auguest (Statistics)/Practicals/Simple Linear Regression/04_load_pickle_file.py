import streamlit as st 
import pickle
import numpy as np 


model=pickle.load(open(r'D:\NareshIT_PrakashSenapati\Prakash Sir-Notes\Auguest (Statistics)\Practicals\linear_reg_model.pkl', 'rb'))

st.title("Salary Prediction App")

st.write("This app predicts the salary based on years of experience using a simple linear regression")

year_experience = st.number_input("Enter years of experince: ", min_value =0.0, max_value=50.0, step=0.5)

if st.button("Predic Salary"):
    experience_input = np.array([[year_experience]])#Convert the input into 2d array
    prediction = model.predict(experience_input)
    
    st.success(f"The predicted salary for {year_experience} years of experice is: ${prediction[0]:,.2f}")
    
    
st.write("The model was trained")    
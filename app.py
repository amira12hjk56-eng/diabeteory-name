import streamlit as st
import pandas as pd
import joblib

# تحميل الموديل
model = joblib.load('diabetes_model.pkl')

st.title("نظام التنبؤ بالسكري")
age = st.number_input("العمر", min_value=1)

if st.button("النتيجة"):
    # هنا لازم السطرين دول يكونوا داخلين لجوه (مسافة Tab أو 4 مسافات)
    prediction = model.predict([[age, 0, 0, 0, 0, 0, 0, 0]])
    st.write(f"النتيجة: {prediction}")
   
   

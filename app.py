import streamlit as st
import pandas as pd
import joblib
import numpy as np

# تحميل الموديل
model = joblib.load('diabetes_model.pkl')

st.title("🏥 نظام التنبؤ بمخاطر السكري")

# مدخلات البيانات بناءً على ملف الإكسيل بتاعك
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", value=25)
    gender = st.selectbox("Gender", options=["Male", "Female"])
    bmi = st.number_input("BMI", value=25.0)
    bp = st.number_input("Blood Pressure", value=120)
    glucose = st.number_input("Fasting Glucose", value=100)
    insulin = st.number_input("Insulin Level", value=10.0)

with col2:
    hba1c = st.number_input("HbA1c Level", value=5.5)
    chol = st.number_input("Cholesterol", value=200)
    trig = st.number_input("Triglycerides", value=150)
    activity = st.selectbox("Physical Activity", options=["Low", "Moderate", "High"])
    calories = st.number_input("Daily Calories", value=2000)
    sugar = st.number_input("Sugar Intake", value=50.0)

with col3:
    sleep = st.number_input("Sleep Hours", value=7.0)
    stress = st.number_input("Stress Level", value=5)
    family = st.selectbox("Family History", options=["Yes", "No"])
    waist = st.number_input("Waist Circumference", value=90.0)

# تحويل الكلمات لأرقام عشان الموديل يفهمها
gender_num = 1 if gender == "Male" else 0
activity_map = {"Low": 0, "Moderate": 1, "High": 2}
family_num = 1 if family == "Yes" else 0

if st.button("تحليل النتيجة"):
    # ترتيب الـ 17 عمود بالظبط زي الإكسيل
    features = np.array([[
        age, gender_num, bmi, bp, glucose, insulin, hba1c, chol, trig,
        activity_map[activity], calories, sugar, sleep, stress, family_num, waist, 0
    ]])
    
    # ملحوظة: لو الموديل لسه مطلع Error، جربي تمسحي الـ "0" الأخيرة اللي في المصفوفة فوق
    
    prediction = model.predict(features)
    
    st.markdown("---")
    if prediction[0] == 1 or "High" in str(prediction[0]):
        st.error("⚠️ النتيجة: احتمالية إصابة عالية")
    else:
        st.success("✅ النتيجة: احتمالية إصابة منخفضة")

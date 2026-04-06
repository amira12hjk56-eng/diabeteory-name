import streamlit as st
import joblib
import pandas as pd

# تحميل الموديل والـ Encoder
model = joblib.load('diabetes_model.pkl')
le = joblib.load('label_encoder.pkl')

st.title("نظام التنبؤ بمخاطر السكري 🩺")
st.write("برجاء إدخال البيانات التالية لتقييم الحالة:")

# عمل خانات لإدخال البيانات (الـ 17 عمود اللي اتدرب عليهم الموديل)
age = st.number_input("العمر", min_value=1, max_value=100, value=25)
gender = st.selectbox("النوع", options=['Male', 'Female'])
bmi = st.number_input("مؤشر كتلة الجسم (BMI)", value=25.0)
blood_pressure = st.number_input("ضغط الدم", value=120)
glucose = st.number_input("مستوى الجلوكوز", value=100)
insulin = st.number_input("مستوى الإنسولين", value=15)
hba1c = st.number_input("مستوى HbA1c", value=5.5)
chol = st.number_input("الكوليسترول", value=180)
trig = st.number_input("الدهون الثلاثية", value=130)
activity = st.selectbox("مستوى النشاط البدني", options=[0, 1, 2, 3])
calories = st.number_input("السعرات اليومية", value=2000)
sugar = st.number_input("كمية السكر اليومية", value=30)
sleep = st.number_input("ساعات النوم", value=7)
stress = st.number_input("مستوى التوتر (1-10)", value=5)
family = st.selectbox("تاريخ العائلة مع السكري", options=['Yes', 'No'])
waist = st.number_input("محيط الخصر (سم)", value=85)
score = st.number_input("درجة خطر سابقة (إن وجد)", value=50)

# زرار التوقع
if st.button("توقع النتيجة"):
    # تجهيز البيانات للتوقع
    gender_enc = 1 if gender == 'Male' else 0
    family_enc = 1 if family == 'Yes' else 0
    
    input_data = [[age, gender_enc, bmi, blood_pressure, glucose, insulin, hba1c, 
                   chol, trig, activity, calories, sugar, sleep, stress, family_enc, waist, score]]
    
    prediction = model.predict(input_data)
    
    st.subheader(f"النتيجة المتوقعة هي: {prediction[0]}")
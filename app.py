import streamlit as st
import joblib
import pandas as pd

# 1. تحميل الموديل والـ Encoder
# تأكدي إن الملفات دي موجودة معاكي في نفس الفولدر على GitHub
model = joblib.load('diabetes_model.pkl')

# 2. قاموس الترجمة (عشان النتيجة تظهر بالعربي)
# زودنا حرف الـ s في الآخر عشان يطابق داتا الموديل
result_map = {
    'Normal': 'طبيعي (سليم) ✅',
    'Prediabetics': 'مرحلة ما قبل السكري ⚠️',
    'Diabetics': 'مصاب بالسكري 🩺'
}

# 3. تصميم واجهة الموقع
st.set_page_config(page_title="توقع السكري", layout="centered")

st.title("نظام التنبؤ بمخاطر السكري 🩺")
st.write("هذا النظام يستخدم الذكاء الاصطناعي لتحليل الحالة الصحية وتوقع احتمالية الإصابة.")
st.markdown("---")

# تقسيم الخانات لصفوف عشان الشكل يكون منظم
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("العمر", min_value=1, max_value=100, value=25)
    gender = st.selectbox("النوع", options=['Male', 'Female'], format_func=lambda x: 'ذكر' if x == 'Male' else 'أنثى')
    bmi = st.number_input("مؤشر كتلة الجسم (BMI)", value=25.0)
    blood_pressure = st.number_input("ضغط الدم", value=120)
    glucose = st.number_input("مستوى الجلوكوز", value=100)
    insulin = st.number_input("مستوى الإنسولين", value=15)
    hba1c = st.number_input("مستوى HbA1c", value=5.5)
    chol = st.number_input("الكوليسترول", value=180)

with col2:
    trig = st.number_input("الدهون الثلاثية", value=130)
    activity = st.selectbox("مستوى النشاط البدني (0-3)", options=[0, 1, 2, 3])
    calories = st.number_input("السعرات اليومية", value=2000)
    sugar = st.number_input("كمية السكر اليومية", value=30)
    sleep = st.number_input("ساعات النوم", value=7)
    stress = st.number_input("مستوى التوتر (1-10)", value=5)
    family = st.selectbox("تاريخ العائلة مع السكري", options=['Yes', 'No'], format_func=lambda x: 'نعم' if x == 'Yes' else 'لا')
    waist = st.number_input("محيط الخصر (سم)", value=85)
    score = st.number_input("درجة خطر سابقة (إن وجد)", value=50)

import streamlit as st
import joblib

# 1. تحميل الموديل
model = joblib.load('diabetes_model.pkl')

# 2. قاموس الترجمة الشامل (عشان نغطي كل الاحتمالات)
result_map = {
    'Normal': 'طبيعي (سليم) ✅',
    'Prediabetes': 'مرحلة ما قبل السكري ⚠️',
    'Prediabetics': 'مرحلة ما قبل السكري ⚠️',
    'Diabetic': 'مصاب بالسكري 🩺',
    'Diabetics': 'مصاب بالسكري 🩺'
}

# 3. واجهة الموقع
st.title("نظام التنبؤ بمخاطر السكري 🩺")
st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    age = st.number_input("العمر", min_value=1, value=25)
    gender = st.selectbox("النوع", options=['Male', 'Female'], format_func=lambda x: 'ذكر' if x == 'Male' else 'أنثى')
    bmi = st.number_input("مؤشر كتلة الجسم (BMI)", value=25.0)
    blood_pressure = st.number_input("ضغط الدم", value=120)
    glucose = st.number_input("مستوى الجلوكوز", value=100)
    insulin = st.number_input("مستوى الإنسولين", value=15)
    hba1c = st.number_input("مستوى HbA1c", value=5.5)
    chol = st.number_input("الكوليسترول", value=180)

with col2:
    trig = st.number_input("الدهون الثلاثية", value=130)
    activity = st.selectbox("مستوى النشاط البدني (0-3)", options=[0, 1, 2, 3])
    calories = st.number_input("السعرات اليومية", value=2000)
    sugar = st.number_input("كمية السكر اليومية", value=30)
    sleep = st.number_input("ساعات النوم", value=7)
    stress = st.number_input("مستوى التوتر (1-10)", value=5)
    family = st.selectbox("تاريخ العائلة مع السكري", options=['Yes', 'No'], format_func=lambda x: 'نعم' if x == 'Yes' else 'لا')
    waist = st.number_input("محيط الخصر (سم)", value=85)
    score = st.number_input("درجة خطر سابقة", value=50)

if st.button("توقع النتيجة الآن"):
    gender_enc = 1 if gender == 'Male' else 0
    family_enc = 1 if family == 'Yes' else 0
    
    input_data = [[age, gender_enc, bmi, blood_pressure, glucose, insulin, hba1c, 
                   chol, trig, activity, calories, sugar, sleep, stress, family_enc, waist, score]]
    
    prediction = model.predict(input_data)[0]
    
    # هنا السر: بنجرب نترجم الكلمة، ولو معرفناش بنعرضها زي ما هي
    arabic_result = result_map.get(prediction, prediction)
    
    st.info("تم تحليل البيانات:")
    st.subheader(f"النتيجة المتوقعة هي: {arabic_result}")
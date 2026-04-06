import streamlit as st
import joblib

# 1. تحميل الموديل
model = joblib.load('diabetes_model.pkl')

# 2. قاموس الترجمة
result_map = {
    'Normal': 'طبيعي (سليم) ✅',
    'Prediabetics': 'مرحلة ما قبل السكري ⚠️',
    'Diabetics': 'مصاب بالسكري 🩺'
}

st.title("نظام التنبؤ بمخاطر السكري 🩺")

# 3. إدخال البيانات (مرة واحدة فقط لكل عنصر)
age = st.number_input("العمر", min_value=1, value=25)
gender = st.selectbox("النوع", options=['Male', 'Female'], format_func=lambda x: 'ذكر' if x == 'Male' else 'أنثى')
bmi = st.number_input("مؤشر كتلة الجسم (BMI)", value=25.0)
glucose = st.number_input("مستوى الجلوكوز", value=100)
hba1c = st.number_input("مستوى HbA1c", value=5.5)
family = st.selectbox("تاريخ العائلة مع السكري", options=['Yes', 'No'], format_func=lambda x: 'نعم' if x == 'Yes' else 'لا')

# تكملة بقية الأعمدة الـ 17 عشان الموديل ميوقفش
blood_pressure, insulin, chol, trig, activity, calories, sugar, sleep, stress, waist, score = 120, 15, 180, 130, 1, 2000, 30, 7, 5, 85, 50

if st.button("توقع النتيجة"):
    g_enc = 1 if gender == 'Male' else 0
    f_enc = 1 if family == 'Yes' else 0
    
    data = [[age, g_enc, bmi, blood_pressure, glucose, insulin, hba1c, chol, trig, activity, calories, sugar, sleep, stress, f_enc, waist, score]]
    
    pred = model.predict(data)[0]
    res = result_map.get(pred, pred)
    st.success(f"النتيجة: {res}")
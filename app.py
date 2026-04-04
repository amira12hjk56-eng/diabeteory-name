import streamlit as st
import pandas as pd
import joblib
import numpy as np

# 1. تحميل الموديل
model = joblib.load('diabetes_model.pkl')

st.set_page_config(page_title="Diabetes Prediction", layout="centered")
st.title("🏥 نظام التنبؤ بمخاطر السكري")
st.write("برجاء إدخال البيانات الـ 7 المطلوبة للحصول على التنبؤ:")

# 2. خانات الإدخال (الـ 7 اللي الموديل متعود عليهم)
age = st.number_input("العمر (Age)", value=25)
gender = st.selectbox("الجنس (Gender)", options=["Male", "Female"])
bmi = st.number_input("مؤشر كتلة الجسم (BMI)", value=25.0)
bp = st.number_input("ضغط الدم (Blood Pressure)", value=120)
glucose = st.number_input("سكر صائم (Fasting Glucose)", value=100)
hba1c = st.number_input("معدل التراكمي (HbA1c)", value=5.5)
activity = st.selectbox("النشاط البدني (Physical Activity)", options=["Low", "Moderate", "High"])

# تحويل الاختيارات لأرقام (نفس اللي عملتيه في الكولاب)
gender_num = 1 if gender == "Male" else 0
# في الكولاب إنتِ استخدمتي LabelEncoder، غالباً الترتيب: High=0, Low=1, Moderate=2 أو حسب الحروف
activity_map = {"High": 0, "Low": 1, "Moderate": 2}

if st.button("تحليل النتيجة الآن"):
    # 3. تجميع البيانات في مصفوفة (7 قيم بالظبط)
    features = np.array([[
        age, gender_num, bmi, bp, glucose, hba1c, activity_map[activity]
    ]])
    
    # 4. التنبؤ
    prediction = model.predict(features)
    
    st.markdown("---")
    # عرض النتيجة (الموديل بيطلع كلمات: High Risk, Low Risk, Prediabetes)
    result = prediction[0]
    if result == "High Risk":
        st.error(f"⚠️ النتيجة: {result}")
    elif result == "Prediabetes":
        st.warning(f"🟠 النتيجة: {result}")
    else:
        st.success(f"✅ النتيجة: {result}")

st.info("مشروع تخرج - أميرة مصطفى 2026")

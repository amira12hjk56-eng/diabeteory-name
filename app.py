
 import streamlit as st
import pandas as pd
import joblib
import numpy as np

# تحميل الموديل
model = joblib.load('diabetes_model.pkl')

st.set_page_config(page_title="Diabetes Prediction System", layout="wide")
st.title("🏥 نظام التنبؤ بمخاطر السكري")

st.write("يرجى إدخال البيانات التالية كاملة للحصول على التنبؤ:")

# تقسيم الخانات لـ 3 أعمدة عشان الشكل يبقى منظم ومريح
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("العمر (Age)", value=25)
    gender = st.selectbox("الجنس (Gender)", options=["Male", "Female"])
    bmi = st.number_input("مؤشر كتلة الجسم (BMI)", value=25.0)
    bp = st.number_input("ضغط الدم (Blood Pressure)", value=120)
    glucose = st.number_input("سكر صائم (Fasting Glucose)", value=100)

with col2:
    insulin = st.number_input("الأنسولين (Insulin)", value=10.0)
    hba1c = st.number_input("معدل التراكمي (HbA1c)", value=5.5)
    chol = st.number_input("الكوليسترول (Cholesterol)", value=200)
    trig = st.number_input("الدهون الثلاثية (Triglycerides)", value=150)
    activity = st.selectbox("النشاط البدني", options=["Low", "Moderate", "High"])

with col3:
    calories = st.number_input("السعرات اليومية", value=2000)
    sugar = st.number_input("استهلاك السكر", value=50.0)
    sleep = st.number_input("ساعات النوم", value=7.0)
    stress = st.number_input("مستوى التوتر", value=5)
    family = st.selectbox("تاريخ عائلي للمرض", options=["Yes", "No"])
    waist = st.number_input("محيط الخصر (Waist)", value=90.0)

# تحويل الاختيارات لأرقام بيفهمها الموديل
gender_num = 1 if gender == "Male" else 0
family_num = 1 if family == "Yes" else 0
activity_map = {"Low": 0, "Moderate": 1, "High": 2}

if st.button("تحليل النتيجة الآن"):
    # تجميع الـ 16 متغير بالترتيب المظبوط اللي في الإكسيل
    features = np.array([[
        age, gender_num, bmi, bp, glucose, insulin, hba1c, chol, trig,
        activity_map[activity], calories, sugar, sleep, stress, family_num, waist
    ]])
    
    # التنبؤ
    prediction = model.predict(features)
    
    st.markdown("---")
    if prediction[0] == 1 or "High" in str(prediction[0]):
        st.error("⚠️ النتيجة: احتمالية إصابة عالية. يرجى استشارة الطبيب.")
    else:
        st.success("✅ النتيجة: احتمالية إصابة منخفضة. حافظ على صحتك!")

st.info("هذا النظام مخصص لأغراض تعليمية ضمن مشروع تخرج - أميرة مصطفى")   

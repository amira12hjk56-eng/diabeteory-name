import streamlit as st
import pandas as pd
import joblib
import numpy as np

# تحميل الموديل
model = joblib.load('diabetes_model.pkl')

st.set_page_config(page_title="Diabetes Prediction System", layout="wide")

st.title("🏥 نظام التنبؤ بمخاطر السكري")
st.write("برجاء إدخال البيانات التالية للحصول على تحليل دقيق:")

# تقسيم الشاشة لصفين عشان الشكل يبقى منظم
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("العمر (Age)", min_value=1, max_value=120, value=25)
    gender = st.selectbox("الجنس (Gender)", options=["Male", "Female"])
    bmi = st.number_input("مؤشر كتلة الجسم (BMI)", value=25.0)
    blood_pressure = st.number_input("ضغط الدم (Blood Pressure)", value=120)

with col2:
    fasting_glucose = st.number_input("سكر صائم (Fasting Glucose)", value=100)
    hba1c = st.number_input("معدل التراكمي (HbA1c)", value=5.5)
    cholesterol = st.number_input("الكوليسترول (Cholesterol)", value=200)
    insulin = st.number_input("الأنسولين (Insulin)", value=10.0)

# تحويل الجنس لأرقام (عشان الموديل بيفهم أرقام بس)
gender_val = 1 if gender == "Male" else 0

if st.button("تحليل النتيجة الآن"):
    # تجهيز المصفوفة (لازم يكون فيها كل الـ 18 عمود لو الموديل اتدرب عليهم)
    # هنا هنحط القيم اللي دخلناها والباقي هنحطه بمتوسطات مؤقتة عشان الكود ميوقفش
    # ملحوظة: لو الموديل مطلع Error، قوليلي عشان نظبط عدد الأصفار بالظبط
    
    input_data = np.array([[age, gender_val, bmi, blood_pressure, fasting_glucose, 
                            insulin, hba1c, cholesterol, 150, 1, 2000, 50, 7, 5, 0, 90, 50]]) 
    
    # التنبؤ
    prediction = model.predict(input_data)
    
    st.markdown("---")
    if prediction[0] == 1 or prediction[0] == "High Risk":
        st.error("⚠️ النتيجة: هناك احتمالية إصابة عالية. ينصح بمراجعة الطبيب.")
    else:
        st.success("✅ النتيجة: احتمالية الإصابة منخفضة. استمر في نمط حياتك الصحي!")

st.info("هذا النظام مخصص لأغراض تعليمية ضمن مشروع تخرج.")

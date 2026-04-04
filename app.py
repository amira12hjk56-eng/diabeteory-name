import streamlit as st
import pandas as pd
import joblib
import numpy as np

# 1. تحميل الموديل
model = joblib.load('diabetes_model.pkl')

# إعدادات الصفحة
st.set_page_config(page_title="Diabetes Prediction System", layout="wide")

# --- القائمة الجانبية (Sidebar) ---
st.sidebar.title("🔍 تفاصيل المشروع")
st.sidebar.info(
    """
    **اسم المشروع:** نظام التنبؤ بالسكري الذكي  
    **إعداد الطالبة:** أميرة مصطفى  
    **دقة النموذج:** 90.08%  
    **الخوارزمية:** تم استخدام تقنيات التعلم الآلي للتنبؤ بناءً على السجلات الطبية.
    """
)

# --- محتوى الصفحة الرئيسي ---
st.title("🏥 نظام التنبؤ بمخاطر السكري")
st.markdown("### أدخلي البيانات الحيوية للحصول على تقييم فوري")

# إضافة صورة تعبيرية (اختياري لو عندك لينك صورة)
# st.image("https://example.com/diabetes-image.jpg", width=700)

# تقسيم المدخلات لعمودين لشكل أرتب
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("العمر (Age)", value=25, help="أدخل العمر بالسنوات")
    gender = st.selectbox("الجنس (Gender)", options=["Male", "Female"])
    bmi = st.number_input("مؤشر كتلة الجسم (BMI)", value=25.0)
    bp = st.number_input("ضغط الدم (Blood Pressure)", value=120)

with col2:
    glucose = st.number_input("سكر صائم (Fasting Glucose)", value=100)
    hba1c = st.number_input("معدل التراكمي (HbA1c)", value=5.5)
    activity = st.selectbox("النشاط البدني (Physical Activity)", options=["High", "Low", "Moderate"])

# تحويل الاختيارات لأرقام
gender_num = 1 if gender == "Male" else 0
activity_map = {"High": 0, "Low": 1, "Moderate": 2}

st.markdown("---")

if st.button("🚀 تحليل النتيجة الآن"):
    # تجميع البيانات
    features = np.array([[age, gender_num, bmi, bp, glucose, hba1c, activity_map[activity]]])
    
    # التنبؤ
    prediction = model.predict(features)
    result = str(prediction[0])
    
    # عرض النتيجة بشكل شيك
    st.subheader("النتيجة النهائية:")
    if "High" in result:
        st.error(f"🚨 الحالة: {result}")
        st.write("ينصح بزيارة الطبيب فوراً وعمل تحاليل إضافية.")
    elif "Pre" in result:
        st.warning(f"⚠️ الحالة: {result}")
        st.write("أنت في مرحلة ما قبل السكري، يرجى الانتباه للنظام الغذائي.")
    else:
        st.success(f"✅ الحالة: {result}")
        st.write("نتائجك جيدة جداً! استمر في الحفاظ على نمط حياة صحي.")

# تذييل الصفحة
st.markdown("<br><hr><center>مشروع تخرج - كلية الحاسبات والمعلومات © 2026</center>", unsafe_allow_html=True)

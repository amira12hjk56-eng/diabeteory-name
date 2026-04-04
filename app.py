import streamlit as st
import pandas as pd
import joblib
import numpy as np

# 1. تحميل الموديل
try:
    model = joblib.load('diabetes_model.pkl')
except:
    st.error("ملف الموديل مش موجود أو فيه مشكلة في التحميل")

st.title("نظام التنبؤ بالسكري")
st.write("أدخلي البيانات المطلوبة للحصول على النتيجة")

# 2. إدخال البيانات
age = st.number_input("العمر", min_value=1, max_value=120, value=30)

if st.button("النتيجة"):
    # 3. تحضير البيانات (العمر + 15 صفر لباقي الخصائص عشان نكمل الـ 16 عمود)
    features = [age] + [0] * 15
    final_input = np.array([features])
    
    # 4. التنبؤ
    prediction = model.predict(final_input)
    
    # 5. عرض النتيجة
    st.markdown("---")
    if prediction[0] == 1:
        st.error("⚠️ النتيجة: احتمالية إصابة عالية. يرجى استشارة طبيب.")
    else:
        st.success("✅ النتيجة: احتمالية إصابة منخفضة. حافظي على صحتك.")

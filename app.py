import streamlit as st
import pandas as pd
import joblib
import numpy as np

# تحميل الموديل
model = joblib.load('diabetes_model.pkl')

st.title("نظام التنبؤ بالسكري")
age = st.number_input("العمر", min_value=1.0, step=1.0, value=30.0)

if st.button("النتيجة"):
    # تجهيز 16 قيمة وحولناهم لأرقام عشرية (Float)
    # الموديل غالباً محتاج البيانات تكون float64
    input_data = np.array([[age] + [0.0]*15], dtype=np.float64)
    
    # التنبؤ باستخدام المصفوفة مباشرة
    prediction = model.predict(input_data)
    
    st.markdown("---")
    if prediction[0] == 1:
        st.error("⚠️ النتيجة: احتمالية إصابة عالية")
    else:
        st.success("✅ النتيجة: احتمالية إصابة منخفضة")

import streamlit as st
import pandas as pd
import joblib
import numpy as np

# تحميل الموديل
model = joblib.load('diabetes_model.pkl')

st.title("نظام التنبؤ بالسكري")
age = st.number_input("العمر", min_value=1, value=30)

if st.button("النتيجة"):
    # تجهيز 16 قيمة (العمر + 15 صفر)
    input_values = [age] + [0]*15
    
    # تحويلهم لمصفوفة NumPy (ده بيخلي الموديل يتجاهل أسامي الأعمدة)
    final_input = np.array([input_values])
    
    # التنبؤ
    prediction = model.predict(final_input)
    
    if prediction[0] == 1:
        st.error("النتيجة: احتمالية إصابة عالية")
    else:
        st.success("النتيجة: احتمالية إصابة منخفضة")

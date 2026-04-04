import streamlit as st
import pandas as pd
import joblib

# تحميل الموديل
model = joblib.load('diabetes_model.pkl')

st.title("نظام التنبؤ بالسكري")
age = st.number_input("العمر", min_value=1)

if st.button("النتيجة"):
    # تحويل المدخلات لـ DataFrame بأسماء أعمدة (عشان الموديل ميزعلش)
    # ملاحظة: استبدلت الـ 0 بقيم افتراضية لباقي الـ 8 خصائص
    columns = ['Age', 'Gender', 'Polyuria', 'Polydipsia', 'sudden weight loss', 'weakness', 'Polyphagia', 'Genital thrush']
    input_data = pd.DataFrame([[age, 0, 0, 0, 0, 0, 0, 0]], columns=columns)
    
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.error("النتيجة: احتمالية إصابة عالية (يرجى مراجعة طبيب)")
    else:
        st.success("النتيجة: احتمالية إصابة منخفضة")
   
   

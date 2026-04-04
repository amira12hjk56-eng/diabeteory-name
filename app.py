import streamlit as st
import pandas as pd
import joblib

# تحميل الموديل
model = joblib.load('diabetes_model.pkl')

st.title("نظام التنبؤ بالسكري")
age = st.number_input("العمر", min_value=1, value=30)

if st.button("النتيجة"):
    # قائمة الـ 16 عمود اللي الموديل مستنيها بالظبط
    columns = [
        'Age', 'Gender', 'Polyuria', 'Polydipsia', 'sudden weight loss',
        'weakness', 'Polyphagia', 'Genital thrush', 'visual blurring',
        'Itching', 'Irritability', 'delayed healing', 'partial paresis',
        'muscle stiffness', 'Alopecia', 'Obesity'
    ]
    
    # هنبعت العمر والباقي كله أصفار (قيم افتراضية) عشان الموديل يرضى يشتغل
    data = [[age] + [0]*15]
    input_data = pd.DataFrame(data, columns=columns)
    
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.error("النتيجة: احتمالية إصابة عالية")
    else:
        st.success("النتيجة: احتمالية إصابة منخفضة")

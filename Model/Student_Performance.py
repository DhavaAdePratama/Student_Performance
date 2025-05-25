import streamlit as st
import pandas as pd
import joblib
from data_preprocessing import data_preprocessing
from app import prediction, model

mother_qual_map = {
    "1 - Secondary Education - 12th Year or Equivalent": 1,
    "2 - Higher Education - Bachelor's Degree": 2,
    "3 - Higher Education - Degree": 3,
    "4 - Higher Education - Master's": 4,
    "5 - Higher Education - Doctorate": 5,
    "6 - Frequency of Higher Education": 6,
    "9 - 12th Year - Not Completed": 9,
    "10 - 11th Year - Not Completed": 10,
    "11 - 7th Year (Old)": 11,
    "12 - Other - 11th Year": 12,
    "14 - 10th Year of Schooling": 14,
    "18 - General Commerce Course": 18,
    "19 - Basic Education 3rd Cycle (9th-11th Year)": 19,
    "22 - Technical-Professional Course": 22,
    "26 - 7th Year of Schooling": 26,
    "27 - 2nd Cycle of General HS Course": 27,
    "29 - 9th Year - Not Completed": 29,
    "30 - 8th Year of Schooling": 30,
    "34 - Unknown": 34,
    "35 - Can't Read or Write": 35,
    "36 - Can Read Without 4th Year of Schooling": 36,
    "37 - Basic Education 1st Cycle (4th/5th Year)": 37,
    "38 - Basic Education 2nd Cycle (6th-8th Year)": 38,
    "39 - Technological Specialization Course": 39,
    "40 - Higher Education - Degree (1st Cycle)": 40,
    "41 - Specialized Higher Studies Course": 41,
    "42 - Professional Higher Technical Course": 42,
    "43 - Higher Education - Master (2nd Cycle)": 43,
    "44 - Higher Education - Doctorate (3rd Cycle)": 44
}



father_qual_map = {
    1:  "Secondary Education - 12th Year or Equivalent",
    2:  "Higher Education - Bachelor's Degree",
    3:  "Higher Education - Degree",
    4:  "Higher Education - Master's",
    5:  "Higher Education - Doctorate",
    6:  "Frequency of Higher Education",
    9:  "12th Year - Not Completed",
    10: "11th Year - Not Completed",
    11: "7th Year (Old)",
    12: "Other - 11th Year",
    13: "2nd Year Complementary HS Course",
    14: "10th Year of Schooling",
    18: "General Commerce Course",
    19: "Basic Education 3rd Cycle (9th-11th Year)",
    20: "Complementary High School Course",
    22: "Technical-Professional Course",
    25: "Complementary HS Course - Not Concluded",
    26: "7th Year of Schooling",
    27: "2nd Cycle of General HS Course",
    29: "9th Year - Not Completed",
    30: "8th Year of Schooling",
    31: "General Course of Administration & Commerce",
    33: "Supplementary Accounting & Administration",
    34: "Unknown",
    35: "Can't Read or Write",
    36: "Can Read Without 4th Year of Schooling",
    37: "Basic Education 1st Cycle (4th/5th Year)",
    38: "Basic Education 2nd Cycle (6th-8th Year)",
    39: "Technological Specialization Course",
    40: "Higher Education - Degree (1st Cycle)",
    41: "Specialized Higher Studies Course",
    42: "Professional Higher Technical Course",
    43: "Higher Education - Master (2nd Cycle)",
    44: "Higher Education - Doctorate (3rd Cycle)"
}

application_mode_mapping = {
    "1 - 1st phase - general contingent": 1,
    "2 - Ordinance No. 612/93": 2,
    "5 - 1st phase - special contingent (Azores Island)": 5,
    "7 - Holders of other higher courses": 7,
    "10 - Ordinance No. 854-B/99": 10,
    "15 - International student (bachelor)": 15,
    "16 - 1st phase - special contingent (Madeira Island)": 16,
    "17 - 2nd phase - general contingent": 17,
    "18 - 3rd phase - general contingent": 18,
    "26 - Ordinance No. 533-A/99, item b2) (Different Plan)": 26,
    "27 - Ordinance No. 533-A/99, item b3 (Other Institution)": 27,
    "39 - Over 23 years old": 39,
    "42 - Transfer": 42,
    "43 - Change of course": 43,
    "44 - Technological specialization diploma holders": 44,
    "51 - Change of institution/course": 51,
    "53 - Short cycle diploma holders": 53,
    "57 - Change of institution/course (International)": 57
}

Tuition_fees_up_to_date_map = {
    "0 - NO ": 0,
    "1 - YES":1
}

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Judul Aplikasi
st.title("🎓 Prediksi Status Mahasiswa")
st.markdown("Masukkan data mahasiswa untuk memprediksi status akademik mereka.")

# Form Input
data = {}

col1, col2, col3 = st.columns(3)

with col1:
    data["Application_mode"] = st.selectbox("Application Mode", list(application_mode_mapping.keys()))
    data["Mothers_qualification"] = st.selectbox("Ibu - Kualifikasi",list(mother_qual_map.keys( )))

with col2:
    data["Fathers_qualification"] = st.selectbox("Ayah - Kualifikasi", list(father_qual_map.keys()))
    data["Tuition_fees_up_to_date"] = st.selectbox("Tunggakan Uang Kuliah?", list(Tuition_fees_up_to_date_map.keys()))

with col3:
    data["Age_at_enrollment"] = st.number_input("Usia Saat Masuk", value=18)

# Kolom akademik semester 1
st.markdown("#### 📘 Semester 1")
col1, col2, col3 = st.columns(3)
with col1:
    data["Curricular_units_1st_sem_enrolled"] = st.number_input("Mata Kuliah Diambil (1)", value=6)
with col2:
    data["Curricular_units_1st_sem_approved"] = st.number_input("Lulus (1)", value=5)
with col3:
    data["Curricular_units_1st_sem_grade"] = st.number_input("Rata-rata Nilai (1)", value=13.5)

data["Curricular_units_1st_sem_evaluations"] = st.number_input("Evaluasi Semester 1", value=5)

# Kolom akademik semester 2
st.markdown("#### 📙 Semester 2")
col1, col2, col3 = st.columns(3)
with col1:
    data["Curricular_units_2nd_sem_enrolled"] = st.number_input("Mata Kuliah Diambil (2)", value=6)
with col2:
    data["Curricular_units_2nd_sem_approved"] = st.number_input("Lulus (2)", value=5)
with col3:
    data["Curricular_units_2nd_sem_grade"] = st.number_input("Rata-rata Nilai (2)", value=14.0)

data["Curricular_units_2nd_sem_evaluations"] = st.number_input("Evaluasi Semester 2", value=4)

# ========== TRANSFORMASI ==========
# Ubah ke dataframe
df = pd.DataFrame([data])

# ========== PREDIKSI ==========
if st.button("🔍 Prediksi Status"):
    pred = model.predict(df)[0]
    proba = model.predict_proba(df)[0]

    st.subheader("🎯 Hasil Prediksi")
    if pred == 'Graduate':
        st.success("Status: **Lulus** 🎓")
    elif pred == 'Dropout':
        st.error("Status: **Putus Kuliah** 💔")
    else:
        st.warning("Status: **Masih Kuliah** 📘")

    fig, ax = plt.subplots()
    ax.bar(model.classes_, proba, color=["green", "orange", "red"])
    ax.set_ylabel("Probabilitas")
    ax.set_title("Probabilitas Prediksi Status Mahasiswa")
    st.pyplot(fig)

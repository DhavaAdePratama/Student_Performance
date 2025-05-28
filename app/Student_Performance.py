import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
from data_preprocessing import data_preprocessing
from app import prediction, model

# ===== MAPPING DICTIONARIES =====
mother_qual_map = {
    "Secondary Education - 12th Year or Equivalent": 1,
    "Higher Education - Bachelor's Degree": 2,
    "Higher Education - Degree": 3,
    "Higher Education - Master's": 4,
    "Higher Education - Doctorate": 5,
    "Frequency of Higher Education": 6,
    "12th Year - Not Completed": 9,
    "11th Year - Not Completed": 10,
    "7th Year (Old)": 11,
    "Other - 11th Year": 12,
    "10th Year of Schooling": 14,
    "General Commerce Course": 18,
    "Basic Education 3rd Cycle (9th-11th Year)": 19,
    "Technical-Professional Course": 22,
    "7th Year of Schooling": 26,
    "2nd Cycle of General HS Course": 27,
    "9th Year - Not Completed": 29,
    "8th Year of Schooling": 30,
    "Unknown": 34,
    "Can't Read or Write": 35,
    "Can Read Without 4th Year of Schooling": 36,
    "Basic Education 1st Cycle (4th/5th Year)": 37,
    "Basic Education 2nd Cycle (6th-8th Year)": 38,
    "Technological Specialization Course": 39,
    "Higher Education - Degree (1st Cycle)": 40,
    "Specialized Higher Studies Course": 41,
    "Professional Higher Technical Course": 42,
    "Higher Education - Master (2nd Cycle)": 43,
    "Higher Education - Doctorate (3rd Cycle)": 44
}

father_qual_map = {

    "Secondary Education - 12th Year or Equivalent": 1,
    "Higher Education - Bachelor's Degree": 2,
    "Higher Education - Degree": 3,
    "Higher Education - Master's": 4,
    "Higher Education - Doctorate": 5,
    "Frequency of Higher Education": 6,
    "12th Year - Not Completed": 9,
    "11th Year - Not Completed": 10,
    "7th Year (Old)": 11,
    "Other - 11th Year": 12,
    "2nd Year Complementary HS Course": 13,
    "10th Year of Schooling": 14,
    "General Commerce Course": 18,
    "Basic Education 3rd Cycle (9th-11th Year)": 19,
    "Complementary High School Course": 20,
    "Technical-Professional Course": 22,
    "Complementary HS Course - Not Concluded": 25,
    "7th Year of Schooling": 26,
    "2nd Cycle of General HS Course": 27,
    "9th Year - Not Completed": 29,
    "8th Year of Schooling": 30,
    "General Course of Administration & Commerce": 31,
    "Supplementary Accounting & Administration": 33,
    "Unknown": 34,
    "Can't Read or Write": 35,
    "Can Read Without 4th Year of Schooling": 36,
    "Basic Education 1st Cycle (4th/5th Year)": 37,
    "Basic Education 2nd Cycle (6th-8th Year)": 38,
    "Technological Specialization Course": 39,
    "Higher Education - Degree (1st Cycle)": 40,
    "Specialized Higher Studies Course": 41,
    "Professional Higher Technical Course": 42,
    "Higher Education - Master (2nd Cycle)": 43,
    "Higher Education - Doctorate (3rd Cycle)": 44
}


application_mode_mapping = {
    
    "1st phase - general contingent": 1,
    "Ordinance No. 612/93": 2,
    "1st phase - special contingent (Azores Island)": 5,
    "Holders of other higher courses": 7,
    "Ordinance No. 854-B/99": 10,
    "International student (bachelor)": 15,
    "1st phase - special contingent (Madeira Island)": 16,
    "2nd phase - general contingent": 17,
    "3rd phase - general contingent": 18,
    "Ordinance No. 533-A/99, item b2) (Different Plan)": 26,
    "Ordinance No. 533-A/99, item b3 (Other Institution)": 27,
    "Over 23 years old": 39,
    "Transfer": 42,
    "Change of course": 43,
    "Technological specialization diploma holders": 44,
    "Change of institution/course": 51,
    "Short cycle diploma holders": 53,
    "Change of institution/course (International)": 57

}

course_map={
    "Biofuel Production Technologies": 33,
    "Animation and Multimedia Design": 171,
    "Social Service (evening attendance)": 8014,
    "Agronomy": 9003,
    "Communication Design": 9070,
    "Veterinary Nursing": 9085,
    "Informatics Engineering": 9119,
    "Equinculture": 9130,
    "Management": 9147,
    "Social Service": 9238,
    "Tourism": 9254,
    "Nursing": 9500,
    "Oral Hygiene": 9556,
    "Advertising and Marketing Management": 9670,
    "Journalism and Communication": 9773,
    "Basic Education": 9853,
    "Management (evening attendance)": 9991
}

mother_occu_map={
    "Student": 0,
    "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers": 1,
    "Specialists in Intellectual and Scientific Activities": 2,
    "Intermediate Level Technicians and Professions": 3,
    "Administrative staff": 4,
    "Personal Services, Security and Safety Workers and Sellers": 5,
    "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry": 6,
    "Skilled Workers in Industry, Construction and Craftsmen": 7,
    "Installation and Machine Operators and Assembly Workers": 8,
    "Unskilled Workers": 9,
    "Armed Forces Professions": 10,
    "Other Situation": 90,
    "(blank)": 99,
    "Health professionals": 122,
    "Teachers": 123,
    "Specialists in information and communication technologies (ICT)": 125,
    "Intermediate level science and engineering technicians and professions": 131,
    "Technicians and professionals, of intermediate level of health": 132,
    "Intermediate level technicians from legal, social, sports, cultural and similar services": 134,
    "Office workers, secretaries in general and data processing operators": 141,
    "Data, accounting, statistical, financial services and registry-related operators": 143,
    "Other administrative support staff": 144,
    "Personal service workers": 151,
    "Sellers": 152,
    "Personal care workers and the like": 153,
    "Skilled construction workers and the like, except electricians": 171,
    "Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like": 173,
    "Workers in food processing, woodworking, clothing and other industries and crafts": 175,
    "Cleaning workers": 191,
    "Unskilled workers in agriculture, animal production, fisheries and forestry": 192,
    "Unskilled workers in extractive industry, construction, manufacturing and transport": 193,
    "Meal preparation assistants": 194
}

father_occu_map= {
    "Student": 0,
    "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers": 1,
    "Specialists in Intellectual and Scientific Activities": 2,
    "Intermediate Level Technicians and Professions": 3,
    "Administrative staff": 4,
    "Personal Services, Security and Safety Workers and Sellers": 5,
    "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry": 6,
    "Skilled Workers in Industry, Construction and Craftsmen": 7,
    "Installation and Machine Operators and Assembly Workers": 8,
    "Unskilled Workers": 9,
    "Armed Forces Professions": 10,
    "Other Situation": 90,
    "(blank)": 99,
    "Armed Forces Officers": 101,
    "Armed Forces Sergeants": 102,
    "Other Armed Forces personnel": 103,
    "Directors of administrative and commercial services": 112,
    "Hotel, catering, trade and other services directors": 114,
    "Specialists in the physical sciences, mathematics, engineering and related techniques": 121,
    "Health professionals": 122,
    "Teachers": 123,
    "Specialists in finance, accounting, administrative organization, public and commercial relations": 124,
    "Intermediate level science and engineering technicians and professions": 131,
    "Technicians and professionals, of intermediate level of health": 132,
    "Intermediate level technicians from legal, social, sports, cultural and similar services": 134,
    "Information and communication technology technicians": 135,
    "Office workers, secretaries in general and data processing operators": 141,
    "Data, accounting, statistical, financial services and registry-related operators": 143,
    "Other administrative support staff": 144,
    "Personal service workers": 151,
    "Sellers": 152,
    "Personal care workers and the like": 153,
    "Protection and security services personnel": 154,
    "Market-oriented farmers and skilled agricultural and animal production workers": 161,
    "Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence": 163,
    "Skilled construction workers and the like, except electricians": 171,
    "Skilled workers in metallurgy, metalworking and similar": 172,
    "Skilled workers in electricity and electronics": 174,
    "Workers in food processing, woodworking, clothing and other industries and crafts": 175,
    "Fixed plant and machine operators": 181,
    "Assembly workers": 182,
    "Vehicle drivers and mobile equipment operators": 183,
    "Unskilled workers in agriculture, animal production, fisheries and forestry": 192,
    "Unskilled workers in extractive industry, construction, manufacturing and transport": 193,
    "Meal preparation assistants": 194,
    "Street vendors (except food) and street service providers": 195
}

nattionality_map= {
    "Portuguese": 1,
    "German": 2,
    "Spanish": 6,
    "Italian": 11,
    "Dutch": 13,
    "English": 14,
    "Lithuanian": 17,
    "Angolan": 21,
    "Cape Verdean": 22,
    "Guinean": 24,
    "Mozambican": 25,
    "Santomean": 26,
    "Turkish": 32,
    "Brazilian": 41,
    "Romanian": 62,
    "Moldova (Republic of)": 100,
    "Mexican": 101,
    "Ukrainian": 103,
    "Russian": 105,
    "Cuban": 108,
    "Colombian": 109
}

Previous_qualification_map= {
    "Secondary education": 1,
    "Higher education - bachelor's degree": 2,
    "Higher education - degree": 3,
    "Higher education - master's": 4,
    "Higher education - doctorate": 5,
    "Frequency of higher education": 6,
    "12th year of schooling - not completed": 9,
    "11th year of schooling - not completed": 10,
    "Other - 11th year of schooling": 12,
    "10th year of schooling": 14,
    "10th year of schooling - not completed": 15,
    "Basic education 3rd cycle (9th/10th/11th year) or equiv.": 19,
    "Basic education 2nd cycle (6th/7th/8th year) or equiv.": 38,
    "Technological specialization course": 39,
    "Higher education - degree (1st cycle)": 40,
    "Professional higher technical course": 42,
    "Higher education - master (2nd cycle)": 43
}




tuition_fees_up_to_date_map = {
    "0 - NO": 0,
    "1 - YES": 1
}

gender_map = {"Male": 0, "Female": 1}
yes_no_map = {"No": 0, "Yes": 1}
marital_status_map = {"Single": 0, "Married": 1, "Divorced": 2, "Widowed": 3}
attendance_map = {"Daytime": 0, "Evening": 1}

# ===== JUDUL APLIKASI =====
st.title("🎓 Prediksi Status Mahasiswa")
st.markdown("Masukkan data mahasiswa untuk memprediksi status akademik mereka.")

# ===== INPUT DATA MAHASISWA =====
data = {}

# ===== INFORMASI UMUM =====
st.header("📋 Informasi Umum")
col1, col2, col3 = st.columns(3)

with col1:
    data["Marital_status"] = marital_status_map[st.selectbox("Status Pernikahan", list(marital_status_map.keys()))]
    data["Application_mode"] = application_mode_mapping[st.selectbox("Mode Pendaftaran", list(application_mode_mapping.keys()))]
    data["Application_order"] = st.number_input("Urutan Pendaftaran", min_value= 0, max_value=9, value=0)
    data["Course"] = course_map[st.selectbox("Program Studi",list(course_map.keys()) )]
    data["Daytime_evening_attendance"] = attendance_map[st.selectbox("Jenis Kuliah", list(attendance_map.keys()))]
    
with col2:
    data["Previous_qualification"] = Previous_qualification_map[st.selectbox("Kualifikasi Sebelumnya", list(Previous_qualification_map.keys()))]
    data["Previous_qualification_grade"] = st.number_input("Nilai Kualifikasi Sebelumnya",  min_value=0, max_value=200, value=0)
    data["Nacionality"] = nattionality_map[(st.selectbox("Kode Kewarganegaraan", list(nattionality_map.keys())))]
    data["Mothers_qualification"] = mother_qual_map[st.selectbox("Ibu - Kualifikasi", list(mother_qual_map.keys()))]
    data["Fathers_qualification"] = father_qual_map[st.selectbox("Ayah - Kualifikasi", list(father_qual_map.keys()))]

with col3:
    data["Mothers_occupation"] = mother_occu_map[st.selectbox("Pekerjaan Ibu", list(mother_occu_map.keys()))]
    data["Fathers_occupation"] = father_occu_map[st.selectbox("Pekerjaan Ayah", list(father_occu_map.keys()))]
    data["Admission_grade"] = st.number_input("Nilai Masuk", min_value=0, max_value=200, value=0)
    data["Displaced"] = yes_no_map[st.selectbox("Mahasiswa Perantauan?", list(yes_no_map.keys()))]
    data["Educational_special_needs"] = yes_no_map[st.selectbox("Kebutuhan Khusus?", list(yes_no_map.keys()))]

# ===== INFORMASI TAMBAHAN =====
col1, col2, col3 = st.columns(3)

with col1:
    data["Debtor"] = yes_no_map[st.selectbox("Memiliki Tunggakan?", list(yes_no_map.keys()))]
    data["Tuition_fees_up_to_date"] = tuition_fees_up_to_date_map[st.selectbox("Tunggakan Uang Kuliah?", list(tuition_fees_up_to_date_map.keys()))]
    
with col2:
    data["Gender"] = gender_map[st.selectbox("Jenis Kelamin", list(gender_map.keys()))]
    data["Scholarship_holder"] = yes_no_map[st.selectbox("Penerima Beasiswa?", list(yes_no_map.keys()))]

with col3:
    data["Age_at_enrollment"] = st.number_input("Usia Saat Masuk", value=18)
    data["International"] = yes_no_map[st.selectbox("Mahasiswa Internasional?", list(yes_no_map.keys()))]

# ===== SEMESTER 1 =====
st.subheader("📘 Semester 1")
col1, col2, col3 = st.columns(3)

with col1:
    data["Curricular_units_1st_sem_credited"] = st.number_input("Mata Kuliah Konversi (1)", value=0)
    data["Curricular_units_1st_sem_enrolled"] = st.number_input("Mata Kuliah Diambil (1)", value=6)

with col2:
    data["Curricular_units_1st_sem_evaluations"] = st.number_input("Evaluasi (1)", value=5)
    data["Curricular_units_1st_sem_approved"] = st.number_input("Lulus (1)", value=5)

with col3:
    data["Curricular_units_1st_sem_grade"] = st.number_input("Rata-rata Nilai (1)", value=13.5)
    data["Curricular_units_1st_sem_without_evaluations"] = st.number_input("Tanpa Evaluasi (1)", value=0)

# ===== SEMESTER 2 =====
st.subheader("📙 Semester 2")
col1, col2, col3 = st.columns(3)

with col1:
    data["Curricular_units_2nd_sem_credited"] = st.number_input("Mata Kuliah Konversi (2)", value=0)
    data["Curricular_units_2nd_sem_enrolled"] = st.number_input("Mata Kuliah Diambil (2)", value=6)

with col2:
    data["Curricular_units_2nd_sem_evaluations"] = st.number_input("Evaluasi (2)", value=4)
    data["Curricular_units_2nd_sem_approved"] = st.number_input("Lulus (2)", value=5)

with col3:
    data["Curricular_units_2nd_sem_grade"] = st.number_input("Rata-rata Nilai (2)", value=14.0)
    data["Curricular_units_2nd_sem_without_evaluations"] = st.number_input("Tanpa Evaluasi (2)", value=0)

# ===== EKONOMI MAKRO =====
st.subheader("📊 Data Ekonomi")
col1, col2, col3 = st.columns(3)

with col1:
    data["Unemployment_rate"] = st.number_input("Tingkat Pengangguran (%)", value=6.0)

with col2:
    data["Inflation_rate"] = st.number_input("Tingkat Inflasi (%)", value=2.5)

with col3:
    data["GDP"] = st.number_input("GDP", value=2.0)

# ===== KONVERSI KE DATAFRAME =====
data_df = pd.DataFrame([data])

# ===== PREDIKSI =====
if st.button("🔍 Prediksi Status"):
    try:
        pred = model.predict(data_df)[0]
        proba = model.predict_proba(data_df)[0]

        st.subheader("🎯 Hasil Prediksi")
        
        # Display prediction result
        if pred == 0:
            st.success("Status:**putus kuliah** 💔")
        elif pred == 1:
            st.error("Status: **masih kuliah** 📘")
        else:
            st.warning("Status: **Lulus** 🎓")

        # Display probability chart
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.bar(model.classes_, proba, color=["#28a745", "#ffc107", "#dc3545"])
        ax.set_ylabel("Probabilitas")
        ax.set_title("Probabilitas Prediksi Status Mahasiswa")
        ax.set_ylim(0, 1)
        
        # Add value labels on bars
        for bar, prob in zip(bars, proba):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                   f'{prob:.3f}', ha='center', va='bottom', fontweight='bold')
        
        plt.tight_layout()
        st.pyplot(fig)
        
        # Display probability values
        st.subheader("📊 Detail Probabilitas")
        prob_df = pd.DataFrame({
            'Status': model.classes_,
            'Probabilitas': proba,
            'Persentase': [f"{p*100:.1f}%" for p in proba]
        })
        st.dataframe(prob_df, use_container_width=True)
        
    except Exception as e:
        st.error(f"❌ Error dalam prediksi: {str(e)}")
        st.info("Pastikan model telah di-load dengan benar dan semua input telah diisi.")
import pickle
import streamlit as st

diabet_model = pickle.load(open('diabetes_model.sav', 'rb'))

st.title('Prediksi Penyakit Diabetes')
st.subheader('Memprediksi kemungkinan penyakit diabetes')
st.text('Masukkan beberapa inputan yang dibutuhkan dibawah ini!')

col1, col2, col3 = st.columns(3)

with col1:
    Umur = st.text_input('Umur')
    KetebalanKulit = st.text_input('Ketebalan kulit (mm)')
    Glukosa = st.text_input('Kadar glukosa')
    
with col2:
    BeratBadan = st.text_input('Berat badan (kg)')
    Insulin = st.text_input('Hormon insulin (mu U/ml)')
    RiwayatDiabetes = st.text_input('Indikator riwayat diabetes keluarga')

with col3:
    Kehamilan = st.text_input('Riwayat kehamilan')
    TekananDarah = st.text_input('Tekanan darah tubuh (mm Hg)')

diab_diagnosis = ''

#prediksi
if st.button('Test Prediksi'):
    diab_prediction = diabet_model.predict([[Kehamilan, Glukosa, TekananDarah, KetebalanKulit, Insulin, BeratBadan, RiwayatDiabetes, Umur]])

    if(diab_prediction[0] == 1):
        diab_diagnosis = 'Pasien terkena diabetes'
    else : 
        diab_diagnosis = 'Pasian terhindar diabetes'
    st.success(diab_diagnosis)
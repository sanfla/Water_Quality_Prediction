import streamlit as st
import pickle
import pandas as pd
import requests
from io import BytesIO

page = st.sidebar.selectbox("Pilih Halaman", ["Pendahuluan", "Perhitungan Prediksi"])

model_url1 = "https://github.com/sanfla/Water_Quality_Prediction/raw/main/model_knn.pkl"
response_1 = requests.get(model_url1)
model_knn = pickle.load(BytesIO(response_1.content))

model_url2 = "https://github.com/sanfla/Water_Quality_Prediction/raw/main/model_dt.pkl"
response_2 = requests.get(model_url2)
model_dt = pickle.load(BytesIO(response_2.content))

if page == "Pendahuluan":

    st.image('https://github.com/sanfla/Water_Quality_Prediction/blob/main/Water_image.png?raw=true', use_column_width=True)

    st.title("Pendahuluan")

    data = pd.read_csv("https://raw.githubusercontent.com/sanfla/Water_Quality_Prediction/main/waterQuality1.csv")
    st.dataframe(data.head(5))

    st.write("""
    Dataset ini berisi berbagai parameter kimia dan biologis yang digunakan untuk menentukan keamanan air, seperti kandungan logam berat 
    (aluminium, arsenic, cadmium, chromium, lead, mercury, radium, uranium), senyawa berbahaya (ammonia, chloramine, nitrates, nitrites), 
    serta keberadaan bakteri dan virus. Aplikasi prediksi kualitas air sangat penting untuk pemantauan air minum, deteksi pencemaran lingkungan, 
    dan pengelolaan sumber daya air.
             
    **Aplikasi prediksi kualitas air berdasarkan data ini sangat penting dalam berbagai aspek**
    """)

    st.image('https://github.com/sanfla/Water_Quality_Prediction/blob/main/Gambar/Gambar2.png?raw=true', use_column_width=True)

    st.write("""
    - **Pemantauan Kualitas Air Minum**: Dengan memanfaatkan dataset ini, model prediktif dapat dibangun untuk mendeteksi apakah air yang dikonsumsi 
    mengandung bahan-bahan berbahaya. Hal ini sangat penting dalam memastikan air minum bebas dari kontaminasi seperti arsenic, lead, dan bacteria, yang 
    dapat menyebabkan masalah kesehatan kronis.
    """)

    st.image('https://github.com/sanfla/Water_Quality_Prediction/blob/main/Gambar/Gambar1.png?raw=true', use_column_width=True)    

    st.write("""
    - **Deteksi Dini Pencemaran Lingkungan**: Beberapa zat seperti mercury, nitrates, dan radium dapat menjadi indikator pencemaran air dari aktivitas industri 
    atau pertanian. Dengan memprediksi konsentrasi zat-zat ini, bisa diambil tindakan cepat untuk mengurangi dampaknya terhadap lingkungan dan kesehatan masyarakat.
    """)

    st.image('https://github.com/sanfla/Water_Quality_Prediction/blob/main/Gambar/Gambar3.png?raw=true', use_column_width=True)

    st.write("""
    - **Pengelolaan Sumber Daya Air**: Informasi dari prediksi ini membantu pengelola air di tingkat lokal maupun nasional dalam merancang kebijakan untuk memastikan 
    air tetap aman digunakan, baik untuk konsumsi manusia maupun untuk kebutuhan industri.

    Dalam aplikasi ini, dua model prediksi digunakan untuk menentukan keamanan air, yaitu K-Nearest Neighbors (KNN) dan Decision Tree. Kedua model 
    ini membantu dalam menganalisis apakah air aman dikonsumsi berdasarkan parameter-parameter yang ada di dataset. Prediksi ini memungkinkan pengambilan 
    keputusan yang lebih cepat dan tepat dalam menjaga kualitas air.
    """)


elif page == "Perhitungan Prediksi":

    st.image('https://github.com/sanfla/Water_Quality_Prediction/blob/main/Water_image.png?raw=true', use_column_width=True)

    st.title("Prediksi Keamanan Air")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        aluminium = st.number_input('Aluminium (mg/L)', min_value=0.0, max_value=100.0)
        ammonia = st.number_input('Ammonia (mg/L)', min_value=0.0, max_value=100.0)
        arsenic = st.number_input('Arsenik (mg/L)', min_value=0.0, max_value=100.0)
        barium = st.number_input('Barium (mg/L)', min_value=0.0, max_value=100.0)
        
    with col2:
        cadmium = st.number_input('Kadmium (mg/L)', min_value=0.0, max_value=100.0)
        chloramine = st.number_input('Chloramine (mg/L)', min_value=0.0, max_value=100.0)
        chromium = st.number_input('Chromium (mg/L)', min_value=0.0, max_value=100.0)
        copper = st.number_input('Tembaga (mg/L)', min_value=0.0, max_value=100.0)

    with col3:
        flouride = st.number_input('Fluoride (mg/L)', min_value=0.0, max_value=100.0)
        bacteria = st.number_input('Bakteri (CFU/mL)', min_value=0.0, max_value=1000.0)
        viruses = st.number_input('Virus (PFU/mL)', min_value=0.0, max_value=1000.0)
        lead = st.number_input('Timbal (mg/L)', min_value=0.0, max_value=100.0)

    with col4:
        nitrates = st.number_input('Nitrate (mg/L)', min_value=0.0, max_value=100.0)
        nitrites = st.number_input('Nitrite (mg/L)', min_value=0.0, max_value=100.0)
        mercury = st.number_input('Mercury (mg/L)', min_value=0.0, max_value=100.0)
        perchlorate = st.number_input('Perchlorate (mg/L)', min_value=0.0, max_value=100.0)

    with col5:
        radium = st.number_input('Radium (mg/L)', min_value=0.0, max_value=100.0)
        selenium = st.number_input('Selenium (mg/L)', min_value=0.0, max_value=100.0)
        silver = st.number_input('Perak (mg/L)', min_value=0.0, max_value=100.0)
        uranium = st.number_input('Uranium (mg/L)', min_value=0.0, max_value=100.0)

    input_data = pd.DataFrame({
        'aluminium': [aluminium],
        'ammonia': [ammonia],
        'arsenic': [arsenic],
        'barium': [barium],
        'cadmium': [cadmium],
        'chloramine': [chloramine],
        'chromium': [chromium],
        'copper': [copper],
        'flouride': [flouride],
        'bacteria': [bacteria],
        'viruses': [viruses],
        'lead': [lead],
        'nitrates': [nitrates],
        'nitrites': [nitrites],
        'mercury': [mercury],
        'perchlorate': [perchlorate],
        'radium': [radium],
        'selenium': [selenium],
        'silver': [silver],
        'uranium': [uranium]
    })

    pilih_model = st.selectbox("Pilih Model Machine Learning", ["K-Nearest Neighbors (KNN)", "Decision Tree"])

    if pilih_model == "K-Nearest Neighbors (KNN)":
        prediction = model_knn.predict(input_data)
    elif pilih_model == "Decision Tree":
        prediction = model_dt.predict(input_data)

    if st.button('Predict'):
        if prediction[0] == 1:
            st.subheader('Model memprediksi bahwa Air **Aman** untuk digunakan.')
        else:
            st.subheader('Model memprediksi bahwa Air **Tidak Aman** untuk digunakan.')

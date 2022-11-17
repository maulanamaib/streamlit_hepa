# import libary 
import streamlit as st
import dataset
import time

# pige title
st.set_page_config(
    page_title="",
    page_icon="https://cdn-icons-png.flaticon.com/128/254/254207.png",
)

    # 0 = tidak ada penyakit jantung
    # 1 = ada penyakit jantung

# hide menu
hide_streamlit_style = """



<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 






# insialisasi web
kolom = st.columns((2, 0.48, 2.7))
home = kolom[1].button('Home')
about = kolom[2].button('About')

# home page
if home==False and about==False or home==True and about==False:
    
    st.write("")
    st.markdown("<h1 style='text-align: center; color: white; margin:0 ; padding:0;'>Prediksi Penyakit Hepa</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: white;'>Harap Diisi Semua Kolom</p>", unsafe_allow_html=True)

    col1, col2,col3 = st.columns(3)
    with col1:
        nama = st.text_input("Masukkan Nama",placeholder='Nama')
    with col2:
        umur = st.number_input("Masukkan Umur",max_value=100)
    with col3:    
        jk = st.selectbox("Jenis Kelamin",('Laki-laki','Perempuan'))

    bp = st.selectbox("Golongan Darah",("A","B","AB","O"))
    col4,col5 =st.columns(2)
    with col4:
        alt = st.number_input("masukkan nilai ALT", min_value=0 ,max_value=100 )
    with col5:
        chol = st.number_input("masukkan nilai AST",min_value=0,max_value=1000)
    #    Centering Butoon 
    columns = st.columns((2, 0.6, 2))
    sumbit = columns[1].button("Submit")
    if sumbit and nama != '' and jk != '' and bp != '' and chol != '' and umur != '':
        # cek jenis kelamin
        #0 = laki-laki
        #1 = perempuan
        if jk == 'Laki-laki':
            jk = 0
        else:
            jk = 1
        # normalisasi data
        data = dataset.normalisasi([umur,jk,bp,chol])
        # prediksi data
        prediksi = dataset.knn(data)
        # cek prediksi
        with st.spinner("Tunggu Sebentar Masih Proses..."):
            if prediksi[-1] == 0:
                time.sleep(1)
                st.success("Hasil Prediksi : "+nama+" Tidak Ada Penyakit Jantung")
            else:
                time.sleep(1)
                st.warning("Hasil Prediksi : "+nama+" Ada Penyakit Jantung")

# about page


        

            






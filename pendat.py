# import libary 
import streamlit as st
import dataset
import time
import webbrowser
# pige title
st.set_page_config(
    page_title="",
    page_icon="https://cdn-icons-png.flaticon.com/128/254/254207.png",
)

    # 0 = tidak ada penyakit hepa
    # 1 = ada penyakit hepa

# hide menu
hide_streamlit_style = """



<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

colum = st.columns((0.1,10,1.5))
url = 'https://github.com/maulanamaib/streamlit_hepa.git'

if colum[1].button('GitHub'):
    webbrowser.open_new_tab(url)

link = 'https://maulanamaib.github.io/datamining/intro.html'

if colum[2].button('Jupyter'):
    webbrowser.open_new_tab(link)
# colum = st.columns((0.1,10,1.5))
# github= colum[1].button("check out this [link]()")
# jupyter = colum[2].button("")


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
        alt = st.number_input("masukkan nilai ALT", min_value=0 ,max_value=1000000000000)
    with col5:
        ast = st.number_input("masukkan nilai AST",min_value=0,max_value=10000000000000)
    # col5, col6, col7, col8 = st.columns(4)
    # with col5:
    #     prot = st.number_input("Masukkan nilai prot")
    # with col6:
    #     alb = st.number_input("MAsukkan nilai alb")
    # with col7:
    #     alp = st.number_input("Masukkan nilai alp")
    # with col8:
    #     bil = st.number_input("Masukkan nilai bil")
    # col9, col10, col11, col12 = st.columns(4)
    # with col9:
    #     che = st.number_input("Masukkan nilai che")
    # with col10:
    #     chol = st.number_input("Masukkan nilali chol")
    # with col11:
    #     crea = st.number_input("Masukkan nilai crea")
    # with col12:
    #     a = st.number_input("masukkan a")
    
    # b = st.number_input("masukkan b")
    #    Centering Butoon 
    columns = st.columns((2, 0.6, 2))
    sumbit = columns[1].button("Submit")
    if sumbit and nama != '' and jk != '' and bp != 0 and umur != 0  and ast != 0 and alt != 0:
        # cek jenis kelamin
        #0 = laki-laki
        #1 = perempuan
        if jk == 'Laki-laki':
            jk = 0
        else:
            jk = 1
        # normalisasi data
        data = dataset.normalisasi([umur,jk,alt,ast])
        # prediksi data
        prediksi = dataset.knn(data)    
        # cek prediksi
        with st.spinner("Tunggu Sebentar Masih Proses..."):
            if prediksi[-1]== 0:
                time.sleep(1)
                st.success("Hasil Prediksi : "+nama+" Sehat! tidak memeliki kemungkinan terkena penyakit hepa")
            else :  
                time.sleep(1)
                st.warning("Hasil Prediksi : "+nama+" Kemungkinan terkena penyakit hepa")


# about page
if about==True and home==False:
    st.markdown("<h1 style='text-align: center; color: white; margin:0 ; padding:0;'>Tentang Sistem ini</h1>", unsafe_allow_html=True)
    st.write('Sistem Predeksi Penyakit hepa adalah sebuah sistem yang bertujuan untuk memprediksi penyakit hepa. Sistem ini dibuat menggunakan bahasa pemrograman python dan library streamlit.')
    st.markdown("<p  color: white;'>Pada sistem ini menggunakan model KNN ( <i>K-nearest neighbors algorithm</i> ) dengan parameter <b>K = 5</b> . Dataset yang digunakan memiliki <b>5 fitur</b> termasuk kelas.</p>", unsafe_allow_html=True)
    st.write('Alasan menggunakan model KNN dengan parameter k = 5 adalah karena memiliki akurasi yang terbesar dari model lainnya pada dataset ini, sehingga diputuskan untuk menggunakan model tersebut.')
    st.write("Disini range umur mempengaruhi prediksi kemungkinan terkenanya penyakit hepa")
    st.markdown("<b>Alanine transminase (ALT), yaitu enzim yang mengubah protein menjadi energi untuk digunakan oleh sel-sel hati<b>",unsafe_allow_html=True)
    st.markdown("<b>Alanine transminase (ALT), yaitu enzim yang mengubah protein menjadi energi untuk digunakan oleh sel-sel hati<b>",unsafe_allow_html=True)

        

            






# import libary 
import streamlit as st
import dataset
import time
import webbrowser
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report, confusion_matrix
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

# colum = st.columns((0.1,10,1.5))
# url = 'https://github.com/maulanamaib/streamlit_hepa.git'

# if colum[1].button('GitHub'):
#     webbrowser.open_new_tab(url)

# link = 'https://maulanamaib.github.io/datamining/intro.html'

# if colum[2].button('Jupyter'):
    # webbrowser.open_new_tab(link)
# colum = st.columns((0.1,10,1.5))
# github= colum[1].button("check out this [link]()")
# jupyter = colum[2].button("")


st.markdown(hide_streamlit_style, unsafe_allow_html=True) 



# insialisasi web
tab1, tab2, tab3 = st.tabs(["Form", "Normalisasi", "Model"])
with tab1:
    kolom = st.columns((0.1, 3, 1, 3, 1.3))   
    
#     col1 = st.markdown(f'''<a href='https://github.com/maulanamaib/streamlit_hepa.git'></a>''',unsafe_allow_html=True)
#     kolom[1].button('GitHub', col1)
    
    link = '[GitHub](http://github.com)'
    kolom[1].markdown =  st.button(link, unsafe_allow_html=True)

    
    home = kolom[2].button('Home')
    about = kolom[3].button('About')

   
#     kolom[4].button('Click Me!', 'https://maulanamaib.github.io/datamining/intro.html')

    col2 = st.markdown(f'''<a href='https://github.com/maulanamaib/streamlit_hepa.git'></a>''',unsafe_allow_html=True)
    kolom[4].button('jupyter', col2)
   


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
            # data = dataset.normalisasi([10,21,1,3])
            # prediksi data
            prediksi = dataset.knn(data)    
            # cek prediksi
            with st.spinner("Tunggu Sebentar Masih Proses..."):
                if prediksi[-1]== 0:
                    # time.sleep(1)
                    st.success("Hasil Prediksi : "+nama+" dengan golongna darah  "+bp+"     Sehat! tidak memeliki kemungkinan terkena penyakit hepa")
            
                else :  
                    time.sleep(1)
                    st.warning("Hasil Prediksi : "+nama+"  dengan golongan darah "+bp+" Kemungkinan terkena penyakit hepa")


    # about page
    if about==True and home==False:
        st.markdown("<h1 style='text-align: center; color: white; margin:0 ; padding:0;'>Tentang Sistem ini</h1>", unsafe_allow_html=True)
        st.write('Sistem Predeksi Penyakit hepa adalah sebuah sistem yang bertujuan untuk memprediksi penyakit hepa. Sistem ini dibuat menggunakan bahasa pemrograman python dan library streamlit.')
        st.markdown("<p  color: white;'>Pada sistem ini menggunakan model KNN ( <i>K-nearest neighbors algorithm</i> ) dengan parameter <b>K = 3</b> . Dataset yang digunakan memiliki <b>5 fitur</b> termasuk kelas.</p>", unsafe_allow_html=True)
        st.write('Alasan menggunakan model KNN dengan parameter k = 3 adalah karena memiliki akurasi yang terbesar dari model lainnya pada dataset ini, sehingga diputuskan untuk menggunakan model tersebut.')
        st.write("Disini range umur mempengaruhi prediksi kemungkinan terkenanya penyakit hepa")
        st.markdown("<b>Alanine transminase (ALT), yaitu enzim yang mengubah protein menjadi energi untuk digunakan oleh sel-sel hati<b>",unsafe_allow_html=True)
        st.markdown("<b>Alanine transminase (ALT), yaitu enzim yang mengubah protein menjadi energi untuk digunakan oleh sel-sel hati<b>",unsafe_allow_html=True)

with tab2:
    code ='''
    import pandas as pd
    import numpy as np
    data = pd.read_csv('https://raw.githubusercontent.com/maulanamaib/streamlit_wine/master/HepatitisCdata.csv')
    data.fillna(0,inplace=True)
    data
    '''
    Class='''
    #Class
    data['Sex'] = pd.Categorical(data["Sex"])
    data["Sex"] = data["Sex"].cat.codes
    data
    '''
    Class1='''
    data['Category'] = pd.Categorical(data["Category"])
    data["Category"] = data["Category"].cat.codes
    data'''

    Class2='''fd = data.drop(data.columns[8:14],axis=1)
    dt = fd.drop(data.columns[4:6],axis=1)
    coba = dt.drop(data.columns[0:1],axis=1)

    y = coba['Category'].values
    dada = coba.drop(data.columns[1],axis=1)
    dada
    len(y)  '''

    Split='''#Split
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test=train_test_split(dada, y, test_size=0.2, random_state=1)
    X_train.shape + X_test.shape
    '''
    SaDa='''#Menyimpan data terbaru
    from pathlib import Path  
    filepath = Path('/content/drive/MyDrive/datamining/tugas/model/datafix2.csv')  
    filepath.parent.mkdir(parents=True, exist_ok=True)  
    dada.to_csv(filepath) '''

    st.code(code, language='python')

    pre='''#Preprocesing
    from sklearn import preprocessing
    le = preprocessing.LabelEncoder()
    le.fit(y)
    y = le.transform(y)
    y'''

    pre2='''y_class = data['Category']
    y = y_class.values.tolist()
    print(y)'''

    drop='''#Drop Target/Class
    col = ['Unnamed: 0','Category']

    X = data.drop(columns=col)
    X'''

    MM='''#Preprocesing Min-Max
    from sklearn.preprocessing import MinMaxScaler

    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(dada)
    nama_fitur = dada.columns.copy()
    scaled_fitur = pd.DataFrame(scaled,columns=nama_fitur)
    scaled_fitur    
    '''
    split2='''from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test=train_test_split(scaled_fitur, y, test_size=0.2, random_state=1)
    X_train.shape + X_test.shape'''

    sv='''#save normalisi
    import joblib
    filename = '/content/drive/MyDrive/datamining/tugas/model/caca.sav'
    joblib.dump(scaler, filename) '''


    data = pd.read_csv('https://raw.githubusercontent.com/maulanamaib/streamlit_wine/master/HepatitisCdata.csv')
    data.fillna(0,inplace=True)
    data

    st.code(Class, language='python')
    #Class
    data['Sex'] = pd.Categorical(data["Sex"])
    data["Sex"] = data["Sex"].cat.codes
    data

    st.code(Class1, language='python')  

    data['Category'] = pd.Categorical(data["Category"])
    data["Category"] = data["Category"].cat.codes
    data

    st.code(Class2, language='python')  

    fd = data.drop(data.columns[8:14],axis=1)
    dt = fd.drop(data.columns[4:6],axis=1)
    coba = dt.drop(data.columns[0:1],axis=1)

    y = coba['Category'].values
    dada = coba.drop(data.columns[1],axis=1)
    dada
    len(y)  

    st.code(Split, language='python')  
    #Split
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test=train_test_split(dada, y, test_size=0.2, random_state=1)
    X_train.shape + X_test.shape

    st.code(SaDa, language='python') 
   #Menyimpan data terbaru
#     from pathlib import Path  
#     filepath = Path('/content/drive/MyDrive/datamining/tugas/model/datafix2.csv')  
#     filepath.parent.mkdir(parents=True, exist_ok=True)  
#     dada.to_csv(filepath) 
      
    st.code(pre, language='python')  
    #Preprocesing
    from sklearn import preprocessing
    le = preprocessing.LabelEncoder()
    le.fit(y)
    y = le.transform(y)
    y

    st.code(pre2, language='python')  
    
    y_class = data['Category']
    y = y_class.values.tolist()
    print(y)

    st.code(drop, language='python') 
    #Drop Target/Class
    col = ['Unnamed: 0','Category']

    X = data.drop(columns=col)
    X

    st.code(MM, language='python') 
    #Preprocesing Min-Max
    from sklearn.preprocessing import MinMaxScaler

    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(dada)
    nama_fitur = dada.columns.copy()
    scaled_fitur = pd.DataFrame(scaled,columns=nama_fitur)
    scaled_fitur    

    st.code(split2  , language='python') 
    #split scaled
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test=train_test_split(scaled_fitur, y, test_size=0.2, random_state=1)
    X_train.shape + X_test.shape

    st.code(sv  , language='python') 
    #save normalisi
#     import joblib
#     filename = '/content/drive/MyDrive/datamining/tugas/model/caca.sav'
#     joblib.dump(scaler, filename) 




with tab3:
    kode='''
#Eksekusi Model
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
#Try running from k=1 through 30 and record testing accuracy
k_range = range(1,31)
scores = {}
scores_list = []
for k in k_range:
        # install model
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train,y_train)
        # save model
        filenameKNN = '/content/drive/MyDrive/datamining/tugas/model/KNNmodel'+str(k)+'.pkl'
        joblib.dump(knn,filenameKNN)
        y_pred=knn.predict(X_test)
        scores[k] = accuracy_score(y_test,y_pred)
        scores_list.append(accuracy_score(y_test,y_pred))
scores
'''
    vis='''
#Visualisasi score
%matplotlib inline
import matplotlib.pyplot as plt

#plot the relationship between K and the testing accuracy
plt.plot(k_range,scores_list)
plt.xlabel('Value of K for KNN')
plt.ylabel('Testing Accuracy')
'''

    sc='''
scores_list.index(max(scores_list))+1 , max(scores_list)'''

    kkk='''
knn = KNeighborsClassifier(n_neighbors=scores_list.index(max(scores_list))+1)
knn.fit(X_train,y_train)
y_pred_knn =knn.predict(X_test)

cm = confusion_matrix(y_test,y_pred_knn)
precision = round(precision_score(y_test,y_pred_knn, average="macro")*100,2)
acc = round(accuracy_score(y_test,y_pred_knn)*100,2)
recall = round(recall_score(y_test,y_pred_knn, average="macro")*100,2)
f1score = round(f1_score(y_test, y_pred_knn, average="macro")*100,2)
print('Konfusi Matrix\n',cm)
print('precision: {}'.format(precision))
print('recall: {}'.format(recall))
print('fscore: {}'.format(f1score))
print('accuracy: {}'.format(acc))'''


    st.code(kode  , language='python') 
    #Eksekusi Model
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn import metrics
    #Try running from k=1 through 30 and record testing accuracy
    k_range = range(1,31)
    scores = {}
    scores_list = []
    for k in k_range:
            # install model
            knn = KNeighborsClassifier(n_neighbors=k)
            knn.fit(X_train,y_train)
            # save model
            filenameKNN = 'https://drive.google.com/drive/folders/1c3AsExydve2WKYhOaagqw5NuN4zbclTZ/KNNmodel'+str(k)+'.pkl'
#             joblib.dump(knn,filenameKNN)
            y_pred=knn.predict(X_test)
            scores[k] = accuracy_score(y_test,y_pred)
            scores_list.append(accuracy_score(y_test,y_pred))
    scores    

    st.code(vis  , language='python') 
    #Visualisasi score
    # matplotlib inline
    import matplotlib.pyplot as plt

    #plot the relationship between K and the testing accuracy
    plt.plot(k_range,scores_list)
    plt.xlabel('Value of K for KNN')
    plt.ylabel('Testing Accuracy')  


    st.code(sc  , language='python') 
    scores_list.index(max(scores_list))+1 , max(scores_list)


    st.code(kkk  , language='p  ython') 

    knn = KNeighborsClassifier(n_neighbors=scores_list.index(max(scores_list))+1)
    knn.fit(X_train,y_train)
    y_pred_knn =knn.predict(X_test)

    cm = confusion_matrix(y_test,y_pred_knn)
    precision = round(precision_score(y_test,y_pred_knn, average="macro")*100,2)
    acc = round(accuracy_score(y_test,y_pred_knn)*100,2)
    recall = round(recall_score(y_test,y_pred_knn, average="macro")*100,2)
    f1score = round(f1_score(y_test, y_pred_knn, average="macro")*100,2)
    print('Konfusi Matrix\n',cm)
    print('precision: {}'.format(precision))
    print('recall: {}'.format(recall))
    print('fscore: {}'.format(f1score))
    print('accuracy: {}'.format(acc))

    st.write('Konfusi Matrix')
    cm
    st.write('precision:')
    precision
    st.write('recall:')
    recall
    st.write('fscore:' )
    f1score
    st.write('accuracy:')
    acc

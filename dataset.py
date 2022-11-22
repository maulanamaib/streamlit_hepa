# print("coba")
# x = 10
# x %= 4
# print(x)
# no = 10 == "10"
# print(no)


# a = [1,2,3,4,5]
# for i in range(0,len(a)):
#     b = a[i]
#     print(i)

# d = int(input("masukkan nilai="))
# r = d / 2
# luas = 3.14 *r *r

# print(int(luas))

# a = input("nama depan :")
# b = input("nama belakang :")
# c = input("nama panjang :")

# hasil = input("pilih yang di tampilkan :")

# if hasil == "a":
#     print(a) 
# elif hasil == "b":
#     print(b)
# elif hasil == "c":
#     print(c)


# nilai = [10, 20, 30, 40, 50, 60,70]

# temp = []
# for i in nilai:
#     if i > 40:
#         temp.append(i)
# print(temp)
import joblib
import pandas as pd

def normalisasi(x):
    # import data test
    # cols = ["Age","Sex","ALT","AST"]
    cols = ["Age","Sex","ALT","AST"]
    df = pd.DataFrame([x],columns=cols)
    data_test = pd.read_csv('WebPendat/model/datafix2.csv')
    data_test = data_test.drop(data_test.columns[0],axis=1)
    # data_test = data_test.drop(data_test.columns[7:13],axis=1)
    # memasukkan data kedalam data test
    data_test = data_test.append(df,ignore_index = True)
    # print(data_test.columns)
    # print(data_test)
    # return data_test yang sudah dinormalisasi
    return joblib.load('WebPendat/model/caca.sav').fit_transform(data_test)

def knn(x):
    
    return joblib.load('WebPendat/model/KNNmodel3.pkl').predict(x)


# print(normalisasi([14,1,345,1]))
    

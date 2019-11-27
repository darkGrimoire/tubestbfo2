#Nama:Anthony
#NIM:16019258
#Tanggal:15 September 2019
#Deskripsi:Tugas Pendahuluan-1 Problem 3
audreyimba=int(input('Masukkan X: '))
if audreyimba<0:
    valenimba=' negatif'
elif audreyimba==0:
    valenimba=' nol'
elif audreyimba>0:
    if audreyimba%2==0:
        valenimba=' positif genap'
    else:
        valenimba=' positif ganjil'
print('X adalah bilangan'+valenimba)

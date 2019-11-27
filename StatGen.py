# States Generator
# by Faris-kun

import pandas as pd

def isValid(hygiene, energy, fun):
    return ((0<=hygiene<=15) and (0<=energy<=15) and (0<=fun<=15))

def searchStates(h, e, f) -> str:
    for i in range(64):
        if (arrHygiene[i]==h) and (arrEnergy[i]==e) and (arrFun[i]==f):
            return input_data["Daftar States"][i]

def generateStates(Kolom, h, e, f):
    input_data[Kolom] = [0 for i in range(64)]
    for i in range(64):
        if isValid(arrHygiene[i]+h, arrEnergy[i]+e, arrFun[i]+f):
            input_data[Kolom][i] = searchStates(arrHygiene[i]+h, arrEnergy[i]+e, arrFun[i]+f)
        else:
            input_data[Kolom][i] = input_data["Daftar States"][i]


# Daftar States
input_data = {}
input_data['Daftar States'] = [0 for i in range(64)]
arrHygiene = [0 for i in range(64)]
arrEnergy = [0 for i in range(64)]
arrFun = [0 for i in range(64)]
f = 0
e = 0
h = 0
for i in range(64):
    if (i%4==0) and (i>0):
        e += 5
        e %= 20
    if i%16==0  and (i>0):
        h += 5
        h %= 20
    input_data['Daftar States'][i] = "q" + str(i)
    arrFun[i] = f
    arrEnergy[i] = e
    arrHygiene[i] = h
    f += 5
    f %= 20
    

# Main program
generateStates("Tidur Siang",0,10,0)
generateStates("Tidur Malam",0,15,0)
generateStates("Makan Hamburger",0,5,0)
generateStates("Makan Pizza",0,10,0)
generateStates("Makan Steak and Beans",0,15,0)
generateStates("Minum Air",-5,0,0)
generateStates("Minum Kopi",-10,5,0)
generateStates("Minum Jus",-5,10,0)
generateStates("Buang Air Kecil",5,0,0)
generateStates("Buang Air Besar",10,-5,0)
generateStates("Bersosialisasi di Kafe",-5,-10,15)
generateStates("Bermain Media Sosial",0,-10,10)
generateStates("Bermain Komputer",0,-10,15)
generateStates("Mandi",15,-5,0)
generateStates("Cuci Tangan",5,0,0)
generateStates("Mendengarkan Musik di Radio",0,-5,10)
generateStates("Membaca Koran",0,-5,5)
generateStates("Membaca Novel",0,-5,10)

df = pd.DataFrame(data=input_data)
writer = pd.ExcelWriter("data_out.xlsx")
df.to_excel(writer, "Transition Table")
writer.save()
print("done")
'''
print(df)
print(arrHygiene)
print(arrEnergy)
print(arrFun)
'''
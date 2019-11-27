'''
Tubes TBFO - The Sims 5
by:
	13518098 Difa Habiba Rahman
	13518125 Faris Rizki Ekananda
'''

from dataclasses import dataclass
from os import system

@dataclass
class Status:
    '''Class for keeping track of character status'''
    hygiene: int = 0
    energy: int = 10
    fun: int = 0
	
	# GETTER
    # Memberikan nilai atribut tertentu dari satu variabel bertipe status
    def GetHygiene(self) -> int:
        return self.hygiene
    def GetEnergy(self) -> int:
        return self.energy
    def GetFun(self) -> int:
        return self.fun
        
    #SETTER
    # Menjumlahkan nilai atribut tertentu dari satu variabel bertipe status sebesar n 
    def SetHygiene(self, n):
        self.hygiene += n
    def SetEnergy(self, n):
        self.energy += n
    def SetFun(self, n):
        self.fun += n
    def Set(self, hygiene=0, energy=0, fun=0):
    # Menjumlahkan ketiga atribut status dengan parameter sesuai urutan.
    # Jika tidak disebutkan, atribut tidak berubah
        self.hygiene += hygiene
        self.energy += energy
        self.fun += fun
    
    #FUNCTIONS
    def IsDead(self) -> bool:
    # Mengembalikan true jika seluruh atribut status bernilai 0
    	return ((self.GetHygiene() == 0) and (self.GetEnergy() == 0) and (self.GetFun() == 0))
    def IsOP(self) -> bool:
    # Mengembalikan true jika seluruh atribut status bernilai 15
    	return ((self.GetHygiene() == 15) and (self.GetEnergy() == 15) and (self.GetFun() == 15))
    def IsValid(self, hygiene=0, energy=0, fun=0) -> bool:
    # Memeriksa apakah nilai atribut mengembalikan nilai valid jika dijumlahkan dengan nilai tertentu dalam parameter
    # Nilai atribut yang valid adalah 0, 5, 10, atau 15
        return ((0<=self.GetHygiene()+hygiene<=15) and (0<=self.GetEnergy()+energy<=15) and (0<=self.GetFun()+fun<=15))
'''
Notes:
    buat IsValid, dia bisa 3 cara utk dipakainya:
    1. varStatus.IsValid(): mengecek apakah variabel class Status itu valid ato ngga
    2. varStatus.IsValid(0,0,5) atau varStatus.IsValid(10,0,-5): mengecek apakah variabel class Status kalo ditambah dgn sekian elemen2nya (sesuai urutan: hygiene, energy, fun).
    3. varStatus.IsValid(energy=-10) atau varStatus.IsValid(hygiene=15, fun=-15): mengecek apakah kalau hygiene, energy, atau fun ditambah dgn n masih valid atau tidak.
'''

# Functions
def Tidur(jenis):
# I.S. Pemain memasukan aksi tidur siang/malam
# F.S. Jika aksi memberikan nilai atribut yang valid, status atribut pemain berubah menggunakan setter sesuai jenis aksi
#      Jika aksi memberikan nilai atribut tidak valid, status atribut tetap dan layar menampilkan pesan "Aksi tidak valid"
# Proses : Validasi dilakukan menggunakan IsValid
    print("Kamu memutuskan untuk tidur ", jenis)
    print(". . . .")
    if jenis=="siang":
        if myStat.IsValid(energy=10):
            myStat.SetEnergy(10)
            input()
        else:
            print("Aksi tidak valid")
            input()
    elif jenis=="malam":
        if myStat.IsValid(energy=15):
            myStat.SetEnergy(15)
            input()
        else:
            print("Aksi tidak valid")
            input()

def Makan(jenis):
# I.S. Pemain memasukan aksi makan hamburger/steak and beans/pizza
# F.S. Jika aksi memberikan nilai atribut yang valid, status atribut pemain berubah menggunakan setter sesuai jenis aksi
#      Jika aksi memberikan nilai atribut tidak valid, status atribut tetap dan layar menampilkan pesan "Aksi tidak valid"
# Proses : Validasi dilakukan menggunakan IsValid

    print("Kamu memutuskan untuk makan ", jenis)
    print(". . . .")
    if jenis=="hamburger":
        if myStat.IsValid(energy=5):
            myStat.SetEnergy(5)
            input()
        else:
            print("Aksi tidak valid")
            input()
    elif jenis=="pizza":
        if myStat.IsValid(energy=10):
            myStat.SetEnergy(10)
            input()
        else:
            print("Aksi tidak valid")
            input()
    elif jenis=="snb":
        if myStat.IsValid(energy=15):
            myStat.SetEnergy(15)
            input()
        else:
            print("Aksi tidak valid")
            input()

def Minum(jenis):
# I.S. Pemain memasukan aksi minum air/jus/kopi
# F.S. Jika aksi memberikan nilai atribut yang valid, status atribut pemain berubah menggunakan setter sesuai jenis aksi
#      Jika aksi memberikan nilai atribut tidak valid, status atribut tetap dan layar menampilkan pesan "Aksi tidak valid"
# Proses : Validasi dilakukan menggunakan IsValid

    print("Kamu memutuskan untuk minum ", jenis)
    print(". . . .")
    if jenis=="air":
        if myStat.IsValid(hygiene=-5):
            myStat.SetHygiene(-5)
            input()
        else:
            print("Aksi tidak valid")
            input()
    elif jenis=="kopi":
        if myStat.IsValid(hygiene=-10, energy=5):
            myStat.Set(hygiene=-10, energy=5)
            input()
        else:
            print("Aksi tidak valid")
            input()
    elif jenis=="jus":
        if myStat.IsValid(hygiene=-5, energy=10):
            myStat.Set(hygiene=-5, energy=10)
            input()
        else:
            print("Aksi tidak valid")
            input()

def BuangAir(jenis):
# I.S. Pemain memasukan aksi buang air kecil/besar
# F.S. Jika aksi memberikan nilai atribut yang valid, status atribut pemain berubah menggunakan setter sesuai jenis aksi
#      Jika aksi memberikan nilai atribut tidak valid, status atribut tetap dan layar menampilkan pesan "Aksi tidak valid"
# Proses : Validasi dilakukan menggunakan IsValid

    print("Kamu memutuskan untuk buang air ", jenis)
    print(". . . .")
    if jenis=="kecil":
        if myStat.IsValid(hygiene=5):
            myStat.SetHygiene(5)
            input()
        else:
            print("Aksi tidak valid")
            input()
    elif jenis=="besar":
        if myStat.IsValid(hygiene=10, energy=-5):
            myStat.Set(hygiene=10, energy=-5)
            input()
        else:
            print("Aksi tidak valid")
            input()

def Bermain(jenis):
# I.S. Pemain memasukan aksi bersosialisasi di kafe/bermain komputer/bermain medsos
# F.S. Jika aksi memberikan nilai atribut yang valid, status atribut pemain berubah menggunakan setter sesuai jenis aksi
#      Jika aksi memberikan nilai atribut tidak valid, status atribut tetap dan layar menampilkan pesan "Aksi tidak valid"
# Proses : Validasi dilakukan menggunakan IsValid

    if jenis=="kafe":
        print("Kamu memutuskan untuk bersosialisasi ke kafe")
        print(". . . .")
        if myStat.IsValid(hygiene=-5, energy=-10, fun=15):
            myStat.Set(hygiene=-5, energy=-10, fun=15)
            input()
        else:
            print("Aksi tidak valid")
            input()
    elif jenis=="medsos":
        print("Kamu memutuskan untuk bermain medsos ", jenis)
        print(". . . .")
        if myStat.IsValid(energy=-10, fun=10):
            myStat.Set(energy=-10, fun=10)
            input()
        else:
            print("Aksi tidak valid")
            input()
    elif jenis=="komputer":
        print("Kamu memutuskan untuk bermain komputer")
        print(". . . .")
        if myStat.IsValid(energy=-10, fun=15):
            myStat.Set(energy=-10, fun=15)
            input()
        else:
            print("Aksi tidak valid")
            input()

def Bersih(jenis):
# I.S. Pemain memasukan aksi mandi/cuci tangan
# F.S. Jika aksi memberikan nilai atribut yang valid, status atribut pemain berubah menggunakan setter sesuai jenis aksi
#      Jika aksi memberikan nilai atribut tidak valid, status atribut tetap dan layar menampilkan pesan "Aksi tidak valid"
# Proses : Validasi dilakukan menggunakan IsValid

    if jenis=="mandi":
        print("Kamu memutuskan untuk mandi ", jenis)
        print(". . . .")
        if myStat.IsValid(hygiene=15, energy=-5):
            myStat.Set(hygiene=15, energy=-5)
            input()
        else:
            print("Aksi tidak valid")
            input()
    elif jenis=="cucitangan":
        print("Kamu memutuskan untuk cuci tangan")
        print(". . . .")
        if myStat.IsValid(hygiene=5):
            myStat.SetHygiene(5)
            input()
        else:
            print("Aksi tidak valid")
            input()

def MusikRadio():
# I.S. Pemain memasukan aksi mendengarkan musik di radio
# F.S. Jika aksi memberikan nilai atribut yang valid, status atribut pemain berubah menggunakan setter sesuai jenis aksi
#      Jika aksi memberikan nilai atribut tidak valid, status atribut tetap dan layar menampilkan pesan "Aksi tidak valid"
# Proses : Validasi dilakukan menggunakan IsValid

    print("Kamu memutuskan untuk mendengarkan musik di radio")
    print(". . . .")
    if myStat.IsValid(energy=-5, fun=10):
        myStat.Set(energy=-5, fun=10)
        input()
    else:
        print("Aksi tidak valid")
        input()

def Baca(jenis):
# I.S. Pemain memasukan aksi membaca novel/koran
# F.S. Jika aksi memberikan nilai atribut yang valid, status atribut pemain berubah menggunakan setter sesuai jenis aksi
#      Jika aksi memberikan nilai atribut tidak valid, status atribut tetap dan layar menampilkan pesan "Aksi tidak valid"
# Proses : Validasi dilakukan menggunakan IsValid

    print("Kamu memutuskan untuk membaca ", jenis)
    print(". . . .")
    if jenis=="koran":
        if myStat.IsValid(energy=-5, fun=5):
            myStat.Set(energy=-5, fun=5)
            input()
        else:
            print("Aksi tidak valid")
            input()
    elif jenis=="novel":
        if myStat.IsValid(energy=-5, fun=10):
            myStat.Set(energy=-5, fun=10)
            input()
        else:
            print("Aksi tidak valid")
            input()

# GUI Functions
def MenuUtama():
# Memberikan tampilan antarmuka dari program, beserta nama author, daftar aksi yang dapat dilakukan, dan status pemain.     
    print("███████████████████████████████████████████████████████████████████")
    print("█                                                                 █")
    print("█   ████████╗██╗  ██╗███████╗    ███████╗██╗███╗   ███╗███████╗   █")
    print("█   ╚══██╔══╝██║  ██║██╔════╝    ██╔════╝██║████╗ ████║██╔════╝   █")
    print("█      ██║   ███████║█████╗      ███████╗██║██╔████╔██║███████╗   █")
    print("█      ██║   ██╔══██║██╔══╝      ╚════██║██║██║╚██╔╝██║╚════██║   █")
    print("█      ██║   ██║  ██║███████╗    ███████║██║██║ ╚═╝ ██║███████║   █")
    print("█      ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚══════╝╚═╝╚═╝     ╚═╝╚══════╝   █")
    print("█_________________________________________________________________█")
    print("█  _   _          _   _    _____________________________________  █")
    print("█ | | | |        | | | |  |Created by: UwU                     |. █")
    print("█ | | | |_      _| | | |  |                                    |. █")
    print("█ | | | \\ \\ /\\ / / | | |  | 13518098    Difa Habiba Rahman     |. █")
    print("█ | |_| |\\ V  V /| |_| |  | 13518125    Faris Rizki Ekananda   |. █")
    print("█  \\___/  \\_/\\_/  \\___/   |____________________________________|. █")
    print("█___________.____________________._____________________.__________█")
    print("█    Available Actions                                            █")
    print("█      1. Tidur Siang/Malam                                       █")
    print("█      2. Mandi atau Cuci Tangan                                  █")
    print("█      3. Buang Air Kecil/Besar                                   █")
    print("█      4. Makan Hamburger/Pizza/Steak and Beans                   █")
    print("█      5. Minum Air/Kopi/Jus                                      █")
    print("█      6. Bersosialisasi ke Kafe                                  █")
    print("█      7. Bermain media sosial/komputer                           █")
    print("█      8. Mendengarkan musik di radio                             █")
    print("█      9. Membaca koran/novel                                     █")
    print("█___________.____________________._____________________.__________█")
    print("█    Your Stat:                                                   █")
    print("█      Hygiene = {:2d}".format(myStat.GetHygiene()), "                                              █")
    print("█      Energy  = {:2d}".format(myStat.GetEnergy()), "                                              █")
    print("█      Fun     = {:2d}".format(myStat.GetFun()), "                                              █")
    print("█___________.____________________._____________________.__________█")
    print()

# Initialization
myStat = Status()
justawake = True
while (True):
    # Write current status
    system('cls')
    MenuUtama()
    if (justawake):
        print("Selamat pagi! Bagaimana tidurmu semalam? Semoga hari ini adalah hari baik untukmu!")
        justawake = False
    else:
        print()
    # Cek Game Status
    if myStat.IsDead():
        print("Oops! Too bad, you've died TwT)")
        print("Karaktermu mati dalam kondisi mengenaskan.")
        print("Lain kali jangan lupa mandi, makan, dan main, jangan ambis terus. :(")
        print()
        print()
        input("======= Press Enter to Quit the Game =======")
        print()
        break
    if myStat.IsOP():
        print("Anjay! Kirito uwu)")
        print("Karaktermu bertahan hidup dengan kekuatan super!")
        print("Terima kasih sudah bermain!")
        print()
        print()
        input("======= Press Enter to Quit the Game =======")
        print()
        break
    COM = input("Sekarang, sebut apa yang kamu mau lakukan: ").lower()
    # Tidur
    if COM == "tidur siang":
        Tidur("siang")
    elif COM == "tidur malam":
        Tidur("malam")
    # Makan
    elif COM == "makan hamburger":
        Makan("hamburger")
    elif COM == "makan pizza":
        Makan("pizza")
    elif COM == "makan steak and beans":
        Makan("snb")
    # Minum
    elif COM == "minum air":
        Minum("air")
    elif COM == "minum kopi":
        Minum("kopi")
    elif COM == "minum jus":
        Minum("jus")
    # Buang Air
    elif COM == "buang air kecil":
        BuangAir("kecil")
    elif COM == "buang air besar":
        BuangAir("besar")
    # Bersosialisasi dan Bermain
    elif COM == "bersosialisasi ke kafe":
        Bermain("kafe")
    elif COM == "bermain media sosial":
        Bermain("medsos")
    elif COM == "bermain komputer":
        Bermain("komputer")
    # Bersih-bersih
    elif COM == "mandi":
        Bersih("mandi")
    elif COM == "cuci tangan":
        Bersih("cucitangan")
    # Lain-lain
    elif COM == "mendengarkan musik di radio":
        MusikRadio()
    elif COM == "membaca koran":
        Baca("koran")
    elif COM == "membaca novel":
        Baca("novel")
    # ERROR HANDLING
    else:
        print("Aksi tidak valid")
        input()
    print()

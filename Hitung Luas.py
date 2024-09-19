import math
import os

def hitung_luas_lingkaran(radius):
    return math.pi * radius ** 2
def hitung_luas_segitiga(a,t):
    return 0.5 * a *t
def hitung_luas_persegi(s):
    return s*s
def hitung_luas_persegi_panjang(p,l):
    return p*l 

jenis = 0
while (jenis != 5): 
    os.system("cls")
    print("---------------------------------")
    print("Aplikasi Hitung Luas Bangun Datar")
    print("Pilih Jenis Bangun Datar")
    print("1.Lingkaran")
    print("2.Segitiga")
    print("3.Persegi")
    print("4.Persegi Panjang")
    print("5.Keluar")
    print("---------------------------------")

    jenis = int(input("Masukan jenis bangun datar(1/2/3/4/5) : "))
    if jenis == 1:
        radius = float(input("Masukkan jari-jari lingkaran: "))
        luas = hitung_luas_lingkaran(radius)
        print(f"Luas lingkaran: {luas:.2f}")
    elif jenis == 2:
        alas = float(input("Masukan alas segitiga: "))
        tinggi = float(input("Masukan tinggi segitiga: "))
        luas = hitung_luas_segitiga(alas, tinggi)
        print(f"Luas Segitiga: {luas:.2f}")
    elif jenis == 3:
        sisi = float(input("Masukan sisi persegi: "))
        luas = hitung_luas_persegi(sisi)
        print(f"Luas Persegi: {luas:.2f}")
    elif jenis == 4:
        panjang = float(input("Masukan panjang persegi panjang: "))
        lebar = float(input("Masukan lebar persegi panjang: "))
        luas = hitung_luas_persegi_panjang(panjang, lebar)
        print(f"Luas Persegi Panjang: {luas:.2f}")
    input("\nTekan ENTER untuk melanjutkan")


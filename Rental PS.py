import os

def cari_data(nama):
    for i in semua_data_booking:
        if i["Nama"] == nama:
            return i
def input_data ():
    nama = input("Nama\t: ")

    #waktu mulai
    print("")
    print("input waktu mulai(tgl,jam:menit)")
    tgl = int(input("tgl :"))
    jam = int(input("jam :"))
    menit = int(input("menit:"))
    waktu_mulai = ("tgl {0}, pukul {1}:{2}".format(tgl,jam,menit))

    #durasi
    print("")
    print("input durasi(jam:menit)")
    jam1 = int(input("jam :"))
    menit1 = int(input("menit:"))
    durasi = ("{0} jam {1} menit".format(jam1,menit1))

    #waktu selesai
    jam_akhir = jam + jam1
    menit_akhir = menit + menit1

    if menit_akhir == 60 :
        jam_akhir += 1
        menit_akhir = 00
    if menit_akhir > 60 :
        akhir = menit_akhir - 60
        menit_akhir = akhir
        jam_akhir += 1
    if jam_akhir == 24 : 
        jam_akhir = 00
        tgl += 1
    if jam_akhir > 24 :
        akhir = jam_akhir - 24
        jam_akhir = akhir
        tgl +=1
    waktu_akhir = ("tgl {0}, pukul {1}:{2}".format(tgl,jam_akhir,menit_akhir))

    #harga
    menit2 = menit1 / 60
    waktu = jam1 + menit2
    harga = waktu * 4000
    harga_int = int(harga)
    harga_akhir = str(harga_int)
    data_booking = {"Nama" : str(nama),
                    "Durasi" : durasi,
                    "Harga" : "Rp."+harga_akhir,
                    "Waktu Mulai" : waktu_mulai,
                    "Waktu Selesai" : waktu_akhir}
    semua_data_booking.append(data_booking)

def hapus_data ():
    nama = input("masukan nama yang akan dihapus : ")
    ketemu = 0
    
    for nm in semua_data_booking:
        if nm["Nama"] == nama:
            ketemu = 1
            semua_data_booking.remove(nm)
            print("Data yang dicari telah dihapus")
    if ketemu == 0 :
        print("Data yang dicari tidak ditemukan")
def tampil_data():
    if (len(semua_data_booking) == 0):
        print("Data booking masih kosong")
    else:
        print ("-" * 100)
        print("Nama".ljust(15), "Durasi".ljust(20), "Harga".ljust(15),  "Waktu Mulai".ljust(20), "Waktu Selesai")
        print("-" * 100)
        
        for dt in semua_data_booking:
            print(dt["Nama"].ljust(15), dt["Durasi"].ljust(20), dt["Harga"].ljust(15), dt["Waktu Mulai"].ljust(20),dt["Waktu Selesai"] )



semua_data_booking = []
menu = 0

while (menu != 4): 
    os.system("cls")
    print("---------------------------------")
    print("Aplikasi Rental PS")
    print("")
    print("Pilihan Menu")
    print("1. Tambah booking penyewaan")
    print("2. Hapus booking penyewaan")
    print("3. Tampilkan semua data booking penyewaan")
    print("---------------------------------")

    menu = int(input("pilih menu : "))

    if menu == 1 :
        input_data()
    elif menu == 2 :
        hapus_data()
    elif menu == 3 :
        tampil_data()
    elif menu == 4 :
        print("Anda telah keluar")
    else :
        print("Menu yang dipilih tidak tersedia")

    input("\nTekan ENTER untuk melanjutkan")
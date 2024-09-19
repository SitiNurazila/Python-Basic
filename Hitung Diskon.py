jumlah = 0
harga = 0
while (harga !=1) :
    harga = int(input("masukan harga barang (jika cukup, masukan 1): "))
    jumlah = jumlah + harga 
harga_total = jumlah - 1
print("harga total adalah ",harga_total)

print("Pilih jenis kartu member")
print("1. Kartu Member Platinum")
print("2. Kartu Member Gold")
print("3. Katu Member Silver")
pilih = int(input("masukan jenis kartu (1/2/3/tidak punya=0 ) :"))
if(pilih==1):
    diskon = 0.3
    potongan_harga = harga_total * diskon
elif(pilih==2 ):
    if(harga_total>= 200000):
        diskon = 0.3
        potongan_harga = harga_total * diskon
    else:
        potongan_harga = 0
elif(pilih==3 and harga_total>= 300000):
    potongan_harga = 25000
else :
    potongan_harga = 0
harga_diskon = harga_total - potongan_harga
print("anda mendapat potongan harga sebesar Rp",potongan_harga)
print("total bayar adalah Rp",harga_diskon)
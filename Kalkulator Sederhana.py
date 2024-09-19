def kalkulator():
    operasi = input("Pilih operasi (+, -, *, /): ")
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    if operasi == "+":
        print(f"Hasil: {angka1 + angka2}")
    elif operasi == "-":
        print(f"Hasil: {angka1 - angka2}")
    elif operasi == "*":
        print(f"Hasil: {angka1 * angka2}")
    elif operasi == "/":
        print(f"Hasil: {angka1 / angka2}")
    else:
        print("Operasi tidak valid.")

kalkulator()

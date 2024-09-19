def konversi_IDR_ke_USD():
    IDR = (int(input("nilai yang akan dikonversikan : ")))
    rumus = IDR / 14000
    print("hasil konversi adalah :",rumus)

def konversi_USD_ke_IDR():
    USD = (int(input("nilai yang akan dikonversikan : ")))
    rumus = USD * 14000
    print("hasil konversi adalah :",rumus)

def konversi_IDR_ke_EURO():
    IDR = (int(input("nilai yang akan dikonversikan : ")))
    rumus = IDR / 17000
    print("hasil konversi adalah :",rumus)

def konversi_EURO_ke_IDR():
    EURO = (int(input("nilai yang akan dikonversikan : ")))
    rumus = EURO * 17000
    print("hasil konversi adalah :",rumus)

def konversi_USD_ke_EURO():
    USD = (int(input("nilai yang akan dikonversikan : ")))
    rumus = USD * 1.2
    print("hasil konversi adalah :",rumus)

def konversi_EURO_ke_USD():
    EURO = (int(input("nilai yang akan dikonversikan : ")))
    rumus = EURO / 1.2
    print("hasil konversi adalah :",rumus)
    
def pilih():
    print("------MENU-------")
    print("")
    print("1. Rupiah ke Dollar Amerika")
    print("2. Dollar Amerika ke Rupiah")
    print("3. Rupiah ke Euro")
    print("4. Euro ke Rupiah")
    print("5. Dollar Amerika ke Euro")
    print("6. Euro ke Dollar Amerika")
    print("")
    
    menu = (input("pilih menu : "))

    if(menu=="1"):
        konversi_IDR_ke_USD()
    elif(menu=="2"):
        konversi_USD_ke_IDR()
    elif(menu=="3"):
        konversi_IDR_ke_EURO()
    elif(menu=="4"):
        konversi_EURO_ke_IDR()
    elif(menu=="5"):
        konversi_USD_ke_EURO()
    elif(menu=="6"):
        konversi_EURO_ke_USD()
pilih()
        
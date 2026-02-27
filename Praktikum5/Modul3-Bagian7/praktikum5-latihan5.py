# Nama : Fuad Nizard Attaqi
# NIM  : J0403251086
# Kelas: A1

# Latihan 5: Studi Kasus Pin
def pin(panjang, hasil=""):
    # Base case: jika panjang string hasil sama dengan panjang PIN yang diminta
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return
    
    # Loop melalui karakter yang tersedia: "0", "1", "2", "B"
    for angka in ["0", "1", "2", "B"]:
        # Cek apakah karakter sudah ada di string hasil (mencegah duplikasi)
        if angka in hasil:
            continue
        else:
            # Panggilan rekursif untuk menambah digit berikutnya
            pin(panjang, hasil + angka)

# Menghasilkan variasi PIN unik panjang 4
print("Variasi PIN unik panjang 4:")
pin(4)

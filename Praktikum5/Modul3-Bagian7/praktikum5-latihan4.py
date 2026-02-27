# Nama : Fuad Nizard Attaqi
# NIM  : J0403251086
# Kelas: A1

# Latihan 4: Backtracking Dasar
def kombinasi(n, hasil=""):
    # Base case: jika panjang string hasil sama dengan n, cetak hasil
    if len(hasil) == n:
        print(hasil)
        return
    
    # Cabang pertama: tambahkan karakter "A"
    kombinasi(n, hasil + "A")
    # Cabang kedua: tambahkan karakter "B"
    kombinasi(n, hasil + "B")

# Mencetak kombinasi karakter 'A' dan 'B' panjang 2
print("Kombinasi 'A' dan 'B' panjang 2:")
kombinasi(2)

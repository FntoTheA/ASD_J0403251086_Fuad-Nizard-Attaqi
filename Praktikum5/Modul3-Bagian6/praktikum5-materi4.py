# Nama : Fuad Nizard Attaqi
# NIM  : J0403251086
# Kelas: A1

# Materi 4: Konsep Dasar Backtracking
def biner(n, hasil=""):
    # Base case: jika panjang string hasil sudah sama dengan n, cetak hasil
    if len(hasil) == n:
        print(hasil)
        return
    else:
        # Cabang pertama: tambahkan "0" ke string hasil
        biner(n, hasil + "0")
        # Cabang kedua: tambahkan "1" ke string hasil
        biner(n, hasil + "1")

# Memanggil fungsi untuk menghasilkan kombinasi biner panjang 2
# Output yang diharapkan: 00, 01, 10, 11
print("Kombinasi biner panjang 2:")
biner(2)

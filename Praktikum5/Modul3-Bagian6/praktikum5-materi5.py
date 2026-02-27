# Nama : Fuad Nizard Attaqi
# NIM  : J0403251086
# Kelas: A1

# Materi 5: Konsep Dasar Backtracking dengan pruning
def bineri(n, batas, hasil="", jumlah1=0):
    # Pruning: Jika jumlah angka 1 sudah melebihi batas, hentikan cabang ini
    if jumlah1 > batas:
        return
    
    # Base case: jika panjang string sudah mencapai n, cetak hasilnya
    if len(hasil) == n:
        print(hasil)
        return
    
    # Rekursi pertama: tambahkan "0" (jumlah angka 1 tidak bertambah)
    bineri(n, batas, hasil + "0", jumlah1)
    
    # Rekursi kedua: tambahkan "1" (jumlah angka 1 bertambah 1)
    bineri(n, batas, hasil + "1", jumlah1+1)

# Mencetak kombinasi biner panjang 4 dengan maksimal dua angka '1'
print("Kombinasi biner panjang 4 dengan max dua angka '1':")
bineri(4, 2)

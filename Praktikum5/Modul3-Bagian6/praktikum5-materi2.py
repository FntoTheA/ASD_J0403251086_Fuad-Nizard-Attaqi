# Nama : Fuad Nizard Attaqi
# NIM  : J0403251086
# Kelas: A1

# Materi 2: Tracing Rekursi
# Contoh 1: Tracing Masuk/Keluar

def hitung(n):
    # Base case: jika n bernilai 0, proses berhenti
    if n == 0:
        print("selesai")
        return
    else:
        # Perintah ini dijalankan saat fungsi dipanggil (menuju base case)
        print("Masuk:", n)
        
        # Panggilan rekursif - perintah setelah ini akan 'tertunda' hingga panggilan ini selesai
        hitung(n-1)
        
        # Perintah ini baru dijalankan saat fungsi 'berbalik' atau keluar dari stack
        print("Keluar:", n)

# Menjalankan fungsi hitung dari angka 5
hitung(5)

# Penjelasan:
# 1. Fungsi mencetak "Masuk: 5" sampai "Masuk: 1" secara berurutan.
# 2. Saat n == 0, fungsi mencetak "selesai" (mencapai base case).
# 3. Setelah itu, fungsi mulai "kembali" (backtracking) dan menyelesaikan perintah 
#    yang tertunda yaitu print("Keluar: n"), mulai dari n=1 hingga kembali ke n=5.
# Inilah mengapa outputnya menunjukkan pola masuk yang menurun dan keluar yang menaik.

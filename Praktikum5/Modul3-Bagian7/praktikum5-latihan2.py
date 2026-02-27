# Nama : Fuad Nizard Attaqi
# NIM  : J0403251086
# Kelas: A1

# Latihan 2: Tracing Rekursi

def Tracing (n):
    # Base case: jika n bernilai 0, proses turun berhenti
    if n == 0:
        print("selesai")
    else:
        # Dicetak saat fungsi dipanggil (menuju ke bawah)
        print("Masuk:", n)
        
        # Panggilan rekursif dengan n yang berkurang (mundur)
        Tracing(n-1) 
        
        # Dicetak saat fungsi kembali dari base case (naik ke atas stack)
        print("Keluar:", n)

# Menjalankan tracing dengan nilai awal 5
Tracing(5)

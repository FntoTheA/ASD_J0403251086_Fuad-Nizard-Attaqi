# Nama : Fuad Nizard Attaqi
# NIM  : J0403251086
# Kelas: A1

# Materi 1: Konsep Dasar Rekursif
# Contoh 1: Faktorial

def faktorial(n):
    # Base case: jika n bernilai 1, berhenti dan kembalikan 1
    if n == 1:
        return 1
    # Recursive step: n dikalikan dengan faktorial dari (n-1)
    else:
        return n * faktorial(n-1)

# Memanggil fungsi faktorial dengan argumen 5
# Alur: 5 * 4 * 3 * 2 * 1
print(f"Hasil faktorial dari 5 adalah: {faktorial(5)}")

# Penjelasan cara kerja:
# 1. faktorial(5) memanggil 5 * faktorial(4)
# 2. faktorial(4) memanggil 4 * faktorial(3)
# 3. faktorial(3) memanggil 3 * faktorial(2)
# 4. faktorial(2) memanggil 2 * faktorial(1)
# 5. faktorial(1) mencapai base case, mengembalikan 1
# 6. Hasil akhirnya: 5 * 4 * 3 * 2 * 1 = 120


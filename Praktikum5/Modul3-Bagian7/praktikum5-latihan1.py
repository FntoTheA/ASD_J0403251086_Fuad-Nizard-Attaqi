# Nama : Fuad Nizard Attaqi
# NIM  : J0403251086
# Kelas: A1

# Latihan Rekursi Dasar: Pemangkatan

def pangkat(a, n):
    if n == 0:
        return 1
    # Recursive step: a dikalikan dengan hasil pemangkatan a^(n-1)
    else:
        return a * pangkat(a, n-1)

# Menghitung 2 pangkat 4
# Alur: 2 * 2 * 2 * 2 * 1 = 16
print(f"Hasil dari 2 pangkat 4 adalah: {pangkat(2, 4)}")

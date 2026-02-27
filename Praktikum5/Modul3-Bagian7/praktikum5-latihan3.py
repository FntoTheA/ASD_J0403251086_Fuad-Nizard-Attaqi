# Nama : Fuad Nizard Attaqi
# NIM  : J0403251086
# Kelas: A1

# Latihan 3: Rekursi pada list
def cari_maks(data, indeks=0):
    """
    Fungsi untuk mencari nilai maksimum dalam sebuah list secara rekursif.
    """
    # Base case: jika indeks berada di elemen terakhir, kembalikan elemen tersebut
    if indeks == len(data) - 1:
        return data[indeks]

    # Recursive step: cari nilai maksimum dari sisa list (indeks + 1 ke depan)
    maksimum_sisa = cari_maks(data, indeks + 1)
    
    # Bandingkan elemen saat ini dengan nilai maksimum dari sisa list
    if data[indeks] > maksimum_sisa:
        return data[indeks]
    else:
        return maksimum_sisa

# Dataset angka
angka = [3, 7, 2, 9, 5]
# Memanggil fungsi dan mencetak hasilnya
print("Nilai maksimum dalam list adalah:", cari_maks(angka))


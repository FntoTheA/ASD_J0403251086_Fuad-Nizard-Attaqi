# Nama : Fuad Nizard Attaqi
# NIM  : J0403251086
# Kelas: A1

# Materi 3: Rekursi Pada data list

def jumlah_list(data, index=0):
    # Base case: jika index sudah mencapai panjang data, kembalikan 0
    if index == len(data):
        return 0
    # Recursive step: jumlahkan elemen saat ini dengan hasil penjumlahan elemen sisa
    else:
        return data[index] + jumlah_list(data, index + 1)

# Memanggil fungsi dengan list [1, 2, 3, 4, 5]
print(f"Hasil penjumlahan list: {jumlah_list([1, 2, 3, 4, 5])}")

# Penjelasan:
# 1. data[0] + jumlah_list(data, 1) -> 1 + (jumlah sisa)
# 2. data[1] + jumlah_list(data, 2) -> 2 + (jumlah sisa)
# ... sampai index == 5, mengembalikan 0.
# Total: 1 + 2 + 3 + 4 + 5 + 0 = 15.

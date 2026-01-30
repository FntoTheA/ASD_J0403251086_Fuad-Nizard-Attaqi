# Praktikum1         : Konsep ADT & File Handling
# Nama               : Fuad Nizard Attaqi
# NIM                : J0403251086
# Praktikum/Kelas    : P1/A1

# Buka file dalam satu string
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read()
print(isi_file)
print("tipe data:", type(isi_file))

# Buka file per baris
print("== Membuka File per baris ==")
jumlah_baris = 0
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris += 1
        baris = baris.strip()
        print("Baris ke -", jumlah_baris)
        print("isinya", baris)


# Parsing baris jadi data satuan dan nampilin dalam bentuk kolom2 data
ListData = []

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for eachLine in file:
        baris = eachLine.strip()
        nim, nama, nilai = baris.split(",")
        ListData.append([nim, nama, int(nilai)])

print("=== Nampilin List ===")
print(ListData)
print("contoh record ke 1", ListData[0])
print("contoh record ke 2", ListData[1])
print("Jumlah record ada", len(ListData))

# Baca data dan nyimpen ke struktur data dict
data_dict = {}

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for eachLine in file:
        baris = eachLine.strip()
        nim, nama, nilai = baris.split(",")
        # simpan data ke dict
        data_dict[nim] = {
            "nama": nama,
            "nilai": int(nilai)
        }
print("=== Nampilin data dict ===")
print(data_dict)

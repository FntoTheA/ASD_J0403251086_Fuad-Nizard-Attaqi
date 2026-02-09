# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama  : Fuad Nizard Attaqi
# NIM   : J0403251086
# Kelas : A1/P1
# ==========================================================

namaFile = "data_barang.txt"

# baca data
def baca_data(namafile):
    data_dict = {}
    with open(namafile, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            if baris == "":
                continue
            kode, nama, harga, stok = [x.strip() for x in baris.split(",")]  
            #kode ini diperlukan karena setiap menambah barang baru, tabel nya akan berantakan, 
            # sehingga pada loop baris, harus di loop lagi untuk mengakses tiap kata dan menghapus space
            
            data_dict[kode] = {
                "nama": nama,
                "harga": int(harga),
                "stok": int(stok)
            }
            #untuk menambahkan data yg sudah dipisah ke dictionary
    return data_dict


# bukaData = baca_data(namaFile)

# simpan data
def simpanData(FileSimpan, DataDict):
    with open(FileSimpan, "w", encoding="utf-8") as file:
        for kode in sorted(DataDict.keys()):
            dict_Simpandata = DataDict[kode]
            NamaBarang = dict_Simpandata["nama"]
            HargaBarang = dict_Simpandata["harga"]
            StokBarang = dict_Simpandata["stok"]
            file.write(
                f"{kode}, {NamaBarang}, {HargaBarang}, {StokBarang} \n")
        print("data saved!")

# tamipilin data
#untuk kode ini kurang lebih sama seperti apa yang dilakukan saat praktikum
def Tampilin_data(stokBarang):
    print(f"\n {'KODE': <10} | {'NAMA BARANG': <35} | {'HARGA BARANG': <12}  | {'STOK BARANG': >12}")
    print("-" * 100)

    for kode in sorted(stokBarang.keys()):
        dict_Simpandata = stokBarang[kode]
        NamaBarang = dict_Simpandata["nama"]
        HargaBarang = dict_Simpandata["harga"]
        StokBarang = dict_Simpandata["stok"]
        if StokBarang == 0:
            StokBarang = "Stok habis"
        else:
            StokBarang = StokBarang
        print(
            f"{kode:<10} | {NamaBarang:<35} | {HargaBarang:<13} | {StokBarang:>12}")


# Cari barang berdasarkan kode
def cariKode(datadict):
    print("==== Mencari Barang Berdasarkan Kode ====")
    input_cari = input("Masukkan kode ").upper().strip()
    print(input_cari)
    if input_cari in datadict:
        print("=== Data Ditemukan! ===")
        print(f"{'KODE': <10} | {'NAMA BARANG': <35} | {'HARGA BARANG': <12}  | {'STOK BARANG': >12}")
        print("-" * 100)
        dict_Simpandata = datadict[input_cari]
        NamaBarang = dict_Simpandata["nama"]
        HargaBarang = dict_Simpandata["harga"]
        StokBarang = dict_Simpandata["stok"]
        print(f"{input_cari:<10} | {NamaBarang:<35} | {HargaBarang:<13} | {StokBarang:>12}")
    else:
        print("Data tidak ada, silahkan masukkan data yang lain")


# cariKode(bukaData)

# tambah barang baru
#untuk fungsi ini, saya membuat metode menambahkan data dengan cara memasukkan input baru ke dictionary
def tambah_barang_baru(datadict):
    inputBaru = input("Masukkan kode untuk barang baru: ").upper().strip()
    if inputBaru in datadict:
        print("Kode ini sudah digunakan, gunakan yang lain!")
        return
    namaBaru = input("Masukkan nama untuk barang baru: ").strip()
    HargaBaru = int(input("Masukkan harga untuk barang baru: "))
    StokBaru = int(input("Masukkan stok untuk barang baru: "))
    datadict[inputBaru] = {
        "nama": namaBaru,
        "harga": HargaBaru,
        "stok": StokBaru
    }

# tambah_barang_baru(bukaData)


# update stok barang
def update_stock(datadict):
    kodeInput = input("Masukkan kode barang yang mau di update: ").upper().strip()
    if kodeInput not in datadict:
        print("Barang tidak ada, silahkan cari yang lain")
    else:
        print("Pilih jenis update:")
        print("1. Tambah stok")
        print("2. Kurangi stok")
        inputUpdate = int(input("Masukkan jenis update: "))
        #disini saya menggunakan syntax match case karena saya ingin mencari tahu apakah ada syntax lain yang memiliki fungsi yang sama dengan if...else...
        #dan saya menulis try dan except sebagai error handling jika user memasukkan input selain yang angka/yang sudah ditetapkan
        match inputUpdate:
            case 1:
                while True:
                    try:
                        TambahInput = int(input("Input stok terbaru: "))
                    except ValueError:
                        print("Input angka, jangan huruf")
                        continue
                    if TambahInput < 0 or TambahInput == 0:
                        print("Angka tidak boleh kurang dari 0 atau sama dengan 0")
                    else:
                        datadict[kodeInput]["stok"] += TambahInput
                        break
            case 2:
                while True:
                    if datadict[kodeInput]["stok"] == 0:
                        print("Stok tidak bisa dikurangi lagi karena sudah 0")
                        break
                    else:
                        try:
                            KuranginInput = int(input("Input stok terbaru: "))
                        except ValueError:
                            print("Input angka, jangan huruf")
                            continue
                        if KuranginInput < 0 or KuranginInput == 0:
                            print("Angka tidak boleh kurang dari 0 atau sama dengan 0")
                        else:
                            datadict[kodeInput]["stok"] -= KuranginInput
                        
#Program function
#mengikuti apa yang ada di modul tugas
def main():
    bukaData = baca_data(namaFile)
    while True:
        print("\n=== STOK BARANG DI TOKO A ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")

        try:
            pilihan = int(input("Pilih menu: "))
        except ValueError:
            print("Tolong masukkan angka yang ada di layar")
            continue
        
        match pilihan:
            case 1:
                Tampilin_data(bukaData)
            case 2:
                cariKode(bukaData)
            case 3:
                tambah_barang_baru(bukaData)
            case 4:
                update_stock(bukaData)
            case 5:
                simpanData(namaFile, bukaData)
            case 0:
                break
            case _:
                print("Mohon masukkan angka yang tertera pada layar")
                

# Menjalankan program utama
if __name__ == "__main__":
    main()

#Nama   : Fuad Nizard Attaqi
#NIM        : J0403251086
#Kelas      : A


#Insertion Sort Descend

def InsertionSort(data):
    #Mulai dari elemen kedua, bandingkan dengan elemen sebelumnya
    for index in range(1, len(data)):
        #Simpan nilai elemen saat ini
        currentValue = data[index]
        #Posisi awal untuk perbandingan
        position = index

        #Geser elemen ke kanan selama lebih kecil dari currentValue (descending)
        while position>0 and data[position-1] < currentValue:
            data[position] = data [position-1]
            position -= 1
            #Tempatkan currentValue di posisi yang tepat
            data[position] = currentValue

#Data yang akan diurutkan
data = [550,5551,23,4421,5,61,351,31,53,1,21]
#Panggil fungsi InsertionSort
InsertionSort(data)
#Tampilkan hasil pengurutan
print(data)
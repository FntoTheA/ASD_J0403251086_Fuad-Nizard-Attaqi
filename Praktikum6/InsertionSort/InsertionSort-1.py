#Nama   : Fuad Nizard Attaqi
#NIM        : J0403251086
#Kelas      : A


#Insertion Sort Ascend

def InsertionSort(data):
    #Mulai dari elemen kedua, bandingkan dengan elemen sebelumnya
    for index in range(1, len(data)):
        #Simpan nilai elemen saat ini
        currentValue = data[index]
        #Posisi awal untuk perbandingan
        position = index

        #Geser elemen ke kanan selama lebih besar dari currentValue (ascending)
        while position>0 and data[position-1] > currentValue:
            data[position] = data [position-1]
            position -= 1
            #Tempatkan currentValue di posisi yang tepat
            data[position] = currentValue

#Data yang akan diurutkan
data = [50,55,43,21,54,21,56,41,56,74,121]
#Panggil fungsi InsertionSort
InsertionSort(data)
#Tampilkan hasil pengurutan
print(data)
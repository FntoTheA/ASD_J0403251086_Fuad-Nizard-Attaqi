#Nama   : Fuad Nizard Attaqi
#NIM        : J0403251086
#Kelas      : A


#Selection Sort Descend

def SelectionSort(data):
    #Iterasi dari akhir list mundur ke posisi pertama
    for fillSlot in range(len(data)-1,0,-1):
        #Asumsikan elemen pertama adalah yang terkecil
        positionMax = 0
        #Cari posisi elemen terkecil dalam rentang yang belum terurut
        for location in range(1, fillSlot+1):
            if data[location] < data[positionMax]:
                positionMax = location
        #Tukar elemen terkecil ke posisi fillSlot (descending: min di akhir)
        temp = data[fillSlot]
        data[fillSlot] = data[positionMax]
        data[positionMax] = temp

#Data yang akan diurutkan
data = [2,513,5,31,653,76,976,5,43,42]
#Panggil fungsi SelectionSort
SelectionSort(data)
#Tampilkan hasil pengurutan
print(data)
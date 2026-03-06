#Nama   : Fuad Nizard Attaqi
#NIM        : J0403251086
#Kelas      : A


#Selection Sort Ascend

def SelectionSort(data):
    #Iterasi dari akhir list mundur ke posisi pertama
    for fillSlot in range(len(data)-1,0,-1):
        #Asumsikan elemen pertama adalah yang terbesar
        positionMax = 0
        #Cari posisi elemen terbesar dalam rentang yang belum terurut
        for location in range(1, fillSlot+1):
            if data[location] > data[positionMax]:
                positionMax = location
        #Tukar elemen terbesar ke posisi fillSlot (ascending: max di akhir)
        temp = data[fillSlot]
        data[fillSlot] = data[positionMax]
        data[positionMax] = temp

#Data yang akan diurutkan
data = [3,6,732,7,8,23,522,6643]
#Panggil fungsi SelectionSort
SelectionSort(data)
#Tampilkan hasil pengurutan
print(data)
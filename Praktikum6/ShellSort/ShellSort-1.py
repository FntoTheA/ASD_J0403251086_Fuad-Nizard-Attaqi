#Nama   : Fuad Nizard Attaqi
#NIM        : J0403251086
#Kelas      : A


#Shell Sort Ascend

def shellSort(data):
    #Mulai dengan sublist sebesar setengah panjang data
    sublistcount = len(data)//2
    #Ulangi sampai gap/sublistcount menjadi 0
    while sublistcount > 0:
        #Lakukan insertion sort dengan gap untuk setiap sublist
        for startposition in range(sublistcount):
            gapInsertionSort(data,startposition,sublistcount)
        print("After increments of size",sublistcount, "The list is",data)
        #Perkecil gap menjadi setengahnya
        sublistcount = sublistcount // 2

#Insertion sort dengan gap tertentu untuk Shell Sort
def gapInsertionSort(data,start,gap):
    #Iterasi mulai dari elemen kedua dalam sublist
    for i in range(start+gap,len(data),gap):
        #Simpan nilai elemen saat ini
        currentvalue = data[i]
        position = i
        #Geser elemen ke kanan selama lebih besar dari currentvalue (ascending)
        while position>=gap and data[position-gap]>currentvalue:
            data[position]=data[position-gap]
            position = position-gap
        #Tempatkan currentvalue di posisi yang tepat
        data[position]=currentvalue

#Data yang akan diurutkan
data = [3,542,65,24,6642,77,86,434,753,213]
#Panggil fungsi shellSort
shellSort(data)
#Tampilkan hasil pengurutan
print(data)
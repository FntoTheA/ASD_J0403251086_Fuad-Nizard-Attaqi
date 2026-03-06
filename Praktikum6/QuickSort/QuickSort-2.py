#Nama   : Fuad Nizard Attaqi
#NIM        : J0403251086
#Kelas      : A


#Quick Sort Descend

#Fungsi utama yang memanggil helper dengan indeks awal dan akhir
def quickSort(data):
    quickSortHelper(data,0,len(data)-1)

#Fungsi rekursif pembantu quickSort
def quickSortHelper(data,first,last):
    #Basis rekursi: proses jika masih ada elemen yang perlu diurutkan
    if first<last:
        splitpoint = partition(data,first,last)
        #Rekursi untuk bagian kiri dan kanan dari splitpoint
        quickSortHelper(data,first,splitpoint-1)
        quickSortHelper(data,splitpoint+1,last)

#Fungsi untuk mempartisi list berdasarkan pivot
def partition(data,first,last):
    #Pilih elemen pertama sebagai pivot
    pivotvalue = data[first]
    leftmark = first+1
    rightmark = last
    done = False
    while not done:
        #Geser leftmark ke kanan selama elemen >= pivot (descending)
        while leftmark <= rightmark and data[leftmark] >= pivotvalue:
            leftmark = leftmark + 1
        #Geser rightmark ke kiri selama elemen <= pivot (descending)
        while data[rightmark] <= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1
        #Jika rightmark melewati leftmark, partisi selesai
        if rightmark < leftmark:
            done = True
        else:
            #Tukar elemen di leftmark dan rightmark
            temp = data[leftmark]
            data[leftmark] = data[rightmark]
            data[rightmark] = temp
    #Tempatkan pivot di posisi yang benar
    temp = data[first]
    data[first] = data[rightmark]
    data[rightmark] = temp
    return rightmark

#Data yang akan diurutkan
data = [4,7,1,35,6,7,6523,642,76,236542,323]
#Panggil fungsi quickSort
quickSort(data) 
#Tampilkan hasil pengurutan
print(data)

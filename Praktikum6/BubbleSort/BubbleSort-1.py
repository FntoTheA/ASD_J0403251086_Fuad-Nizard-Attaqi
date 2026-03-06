#Nama   : Fuad Nizard Attaqi
#NIM        : J0403251086
#Kelas      : A


#Bubble Sort Ascend

def bubbleSort(data):
    #Iterasi dari akhir list sampai ke awal
    for  i in range(len(data )- 1,0,-1):
        #Bandingkan dua elemen yang bersebelahan
        for j in range (i):
            #Jika elemen kiri lebih besar, tukar posisi (ascending)
            if data [j] > data [j+1]:
                temp = data[j]
                data[j] = data [j+1]
                data[j+1] = temp

#Data yang akan diurutkan
data = [54,26,93,17,77,31,44,55,20]
#Panggil fungsi BubbleSort
bubbleSort(data)
#Tampilkan hasil pengurutan
print(data)


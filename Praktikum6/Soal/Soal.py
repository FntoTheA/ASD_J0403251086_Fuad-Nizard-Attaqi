#Nama   : Fuad Nizard Attaqi
#NIM        : J0403251086
#Kelas      : A


#Latihan Soal Pak Budi

#Sorting dulu
def BubbleSort(data):
    for i in range(len(data)- 1,0,-1):
        for j in range(i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

#Ambil 5 data teratas
def pickTop5(data):
    return data[len(data)-5:]

#Data yang akan diurutkan dan dipilih 5 teratas
data = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]
#Panggil fungsi BubbleSort dan pickTop5
print(pickTop5(BubbleSort(data))[::-1])


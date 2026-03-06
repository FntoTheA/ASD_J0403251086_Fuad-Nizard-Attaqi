#Nama   : Fuad Nizard Attaqi
#NIM        : J0403251086
#Kelas      : A


#Merge Sort Ascend

def mergeSort(data):
    print("Splitting ",data)
    #Basis rekursi: hanya proses jika list memiliki lebih dari 1 elemen
    if len(data)>1:
        #Cari titik tengah list
        mid = len(data)//2
        #Bagi list menjadi dua bagian
        lefthalf = data[:mid]
        righthalf = data[mid:]
        #Rekursi untuk mengurutkan masing-masing bagian
        mergeSort(lefthalf)
        mergeSort(righthalf)
        #Inisialisasi pointer untuk lefthalf, righthalf, dan data
        i=0
        j=0
        k=0
        #Gabungkan dua bagian secara ascending
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                data[k]=lefthalf[i]
                i=i+1
            else:
                data[k]=righthalf[j]
                j=j+1
            k=k+1
        #Salin sisa elemen lefthalf jika masih ada
        while i < len(lefthalf):
            data[k]=lefthalf[i] 
            i=i+1
            k+1
        #Salin sisa elemen righthalf jika masih ada
        while j < len(righthalf):
            data[k]=righthalf[j]
            j=j+1
            k=k+1

#Data yang akan diurutkan
data = [443,6,43,44,36,8,282,84,48,74]
#Panggil fungsi mergeSort
mergeSort(data)
#Tampilkan hasil pengurutan
print(data)

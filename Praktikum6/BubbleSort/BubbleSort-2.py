#Nama   : Fuad Nizard Attaqi
#NIM        : J0403251086
#Kelas      : A


#Bubble Sort Descend



def shortBubbleSort(alist):
    #Flag untuk menandai apakah ada pertukaran dalam satu pass
    exchanges = True
    #Jumlah pass yang tersisa
    passNum = len(alist) - 1
    #Ulangi selama masih ada pass dan terjadi pertukaran
    while passNum > 0 and exchanges:
        exchanges = False
        #Bandingkan dua elemen bersebelahan dalam satu pass
        for i in range(passNum):
            #Jika elemen kiri lebih kecil, tukar posisi (descending)
            if alist[i] < alist[i+1]:
                exchanges = True
                temp = alist[i+1]
                alist[i+1] = alist[i]
                alist[i] = temp
        #Kurangi jumlah pass setelah setiap iterasi
        passNum -= 1
    
#Data yang akan diurutkan
alist=[20,30,40,90,50,60,70,80,100,110]
#Panggil fungsi shortBubbleSort
shortBubbleSort(alist)
#Tampilkan hasil pengurutan
print(alist)

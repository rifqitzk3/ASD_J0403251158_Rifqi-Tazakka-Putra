#==============================================================
# Nama : Rifqi Tazakka Putra
# NIM  : J0403251158
# Kelas: TPL B1
#==============================================================

def insertion_sort(data): 
    for i in range(1, len(data)): 
        key = data[i] 
        j = i - 1 
         
        while j >= 0 and ______________________: 
            data[j + 1] = data[j] 
            j -= 1 
         
        ______________________ 
     
    return data 

'''
Soal: 
1. Lengkapi kondisi agar menjadi sorting ascending. 
2. Ubah agar menjadi descending.

Jawab : 
1.
        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j-=1
        data[j+1] = key
2. 
        while j >= 0 and data[j] < key: (Hanya ubah tanda lebih dari menjadi kurang dari)
            data[j+1] = data[j]
            j-=1
        data[j+1] = key
        
'''
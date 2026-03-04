#==============================================================
# Nama : Rifqi Tazakka Putra
# NIM  : J0403251158
# Kelas: TPL B1
#==============================================================

def merge(left, right): 
    result = [] 
    i = 0 
    j = 0 
     
    while i < len(left) and j < len(right): 
        if __________________________: 
            result.append(left[i]) 
            i += 1 
        else: 
            result.append(right[j]) 
            j += 1 
     
    result.extend(left[i:]) 
    result.extend(right[j:]) 
     
    return result 

'''
Soal: 
1. Lengkapi kondisi agar menjadi ascending. 
2. Jelaskan fungsi result.extend().

Jawab:
1. 
    if left[i] <= right[j]:
        result.append(left[i])
        i+=1
    else:
        result.append(right[j])
        j+=1
        
2. Fungsinya adalah untuk menyisipkan semua sisa elemen dari salah satu list (left atau right) yang belum sempat 
   dimasukkan ke dalam result setelah perulangan while selesai.
'''
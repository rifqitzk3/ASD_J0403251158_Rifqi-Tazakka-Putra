#==============================================================
# Nama : Rifqi Tazakka Putra
# NIM  : J0403251158
# Kelas: TPL B1
#==============================================================

'''
Buat program dengan menggunakan algoritma insertion sort 
Tracing dengan  data = [5, 2, 4, 6, 1, 3]
1. Tuliskan isi list setelah iterasi i = 1. 
2. Tuliskan isi list setelah iterasi i = 3. 
3. Berapa kali pergeseran terjadi pada iterasi i = 4?

Jawab :
1. [2, 5, 4, 6, 1, 3]
2. [2, 4, 5, 6, 1, 3]
3. 4 kali geser 

'''
def insertionSort(data):
    # Melihat data awal
    print("Data awal : ", data)
    print("="*50)
    
    # Loop mulai dari data ke-2 berarti indeks array ke-1
    for i in range (1, len(data)):
        
        key = data[i] # Simpan nilai yang disisipkan
        j = i-1 # Indeks elemen terakhir di bagian kiri
        
        print("Iterasi ke- ", i)
        print("Nilai Key Sekarang = ", key)
        print("Bagian kiri (Terurut) : ", data[:i])
        print("Bagian kanan (Belum Terurut) : ", data[i:])
        
        # Geser 
        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j-=1
        # Sisipkan key ke posisi yang benar 
        data[j+1] = key
        
        print("Setelah disisipkan : ", data)
        print("-"*50)
        
        
    return data

angka = [5, 2, 4, 6, 1, 3]
print("Hasil Sort : ",insertionSort(angka))
# =============================================
# Nama : Rifqi Tazakka Putra
# NIM  : J0403251158
# =============================================

# =============================================
# Insertion Sort dengan tracing
# =============================================

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

angka = [7,8,5,2,4,6]
print("Hasil Sort : ",insertionSort(angka))
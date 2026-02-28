# ==============================================
# NAMA  : Rifqi Tazakka Putra
# NIM   : J0403251158
# ==============================================

def cari_maks(data, index=0):
    # Base case: jika sudah di elemen terakhir, itulah nilai maks sementara 
    if index == len(data) - 1:
        return data[index]
    
    # Recursive case: cari nilai maks dari sisa list di depan 
    maks_sisa = cari_maks(data, index + 1)
    
    # Bandingkan elemen saat ini dengan nilai maks dari sisa list 
    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa

angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka)) # Output: 9 

# Jadi alurnya begini
# Program ini bekerja dengan membandingkan elemen list satu per satu dari posisi belakang ke depan menggunakan bantuan indeks secara rekursif. 
# Alurnya menelusuri list hingga ke ujung indeks terakhir untuk mendapatkan nilai elemen tersebut sebagai pembanding awal. 
# Base case tercapai saat indeks sudah berada di elemen terakhir list, yang menandai dimulainya proses pengembalian nilai untuk dibandingkan. 
# Selama fase kembali, setiap elemen di indeks saat ini akan dibandingkan dengan nilai terbesar yang ditemukan sebelumnya 
# hingga didapatkan nilai maksimum tunggal dari seluruh isi list.
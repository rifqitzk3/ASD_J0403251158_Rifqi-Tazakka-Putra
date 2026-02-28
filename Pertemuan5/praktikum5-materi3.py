# =============================================
# Nama : Rifqi Tazakka Putra
# NIM  : J0403251158
# =============================================

#==============================================================
# Materi Rekursif : Menjumlahkan Elemen List
#==============================================================

def jumlah_list(data, index=0):
    # Base case
    if index == len(data):
        return 0

    # Recursive case
    return data[index] + jumlah_list(data, index+1)

print("\n==========Program Jumlah Data List==========\n")
print(jumlah_list([2,4,5]))

# Jadi intinya program ini bekerja dengan memproses elemen di dalam list secara bertahap menggunakan bantuan indeks sebagai penunjuk posisi.
# Alurnya dimulai dari indeks 0, lalu fungsi memanggil dirinya sendiri dengan menggeser indeks ke posisi berikutnya (index + 1).
# Base case tercapai ketika nilai indeks sudah sama dengan panjang list, yang menandakan tidak ada lagi data yang perlu diproses.
# Pada fase pengembalian, elemen pada indeks saat ini akan dijumlahkan dengan hasil penjumlahan dari elemen-elemen setelahnya 
# hingga didapatkan total akhir.
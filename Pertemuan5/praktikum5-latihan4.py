# ==============================================
# NAMA  : Rifqi Tazakka Putra
# NIM   : J0403251158
# ==============================================

def kombinasi(n, hasil=""):
    if len(hasil) == n:
        print(hasil)
        return
    
    kombinasi(n, hasil + "A") # Cabang untuk huruf A 
    kombinasi(n, hasil + "B") # Cabang untuk huruf B 

print("Kombinasi Huruf (n=2):")
kombinasi(2)

# Jadi gini alurnya
# Program ini bekerja dengan teknik backtracking untuk membangun semua kemungkinan string dari kumpulan huruf A dan B 
# sesuai panjang yang diinginkan. 
# Alurnya mengikuti pola pencarian pohon keputusan di mana setiap langkah rekursi akan bercabang untuk 
# mencoba opsi huruf 'A' lalu mencoba opsi huruf 'B'. 
# Base case tercapai ketika panjang string yang disusun sudah memenuhi target panjang 'n', 
# di mana pada saat itulah kombinasi tersebut dicetak ke layar. 
# Setelah satu kombinasi dicetak, fungsi akan secara otomatis kembali (backtrack) ke langkah sebelumnya 
# untuk mengeksplorasi cabang huruf lain yang belum dicoba.
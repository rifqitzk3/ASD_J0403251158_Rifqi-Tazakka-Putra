# ==============================================
# NAMA  : Rifqi Tazakka Putra
# NIM   : J0403251158
# ==============================================

#==============================================================
# Materi Rekursif : Backtracking Biner
#==============================================================

def biner(n, hasil=""):
    # Base case: jika panjang string 'hasil' sudah mencapai n, cetak 
    if len(hasil) == n:
        print(hasil)
        return

    # Pola Choose & Explore: 
    # Mencoba menambahkan '0' ke string
    biner(n, hasil + "0")
    # Mencoba menambahkan '1' ke string 
    biner(n, hasil + "1")

# Membangun pohon keputusan untuk n=3 
print("Kombinasi Biner 3-bit:")
biner(3)

# Jadi intinya program ini bekerja dengan strategi backtracking untuk mencari semua kemungkinan kombinasi angka biner (0 dan 1) sepanjang 'n'.
# Alurnya mengikuti pola Choose + Explore, di mana program pertama-tama memilih untuk menambah angka '0', mengeksplorasi cabang itu sampai dalam, 
# lalu kembali (backtrack) untuk mencoba memilih angka '1' .
# Base case tercapai ketika panjang string yang sedang disusun sudah sama dengan nilai 'n', lalu program mencetak hasil kombinasi tersebut .
# Proses ini membentuk struktur pohon keputusan yang menelusuri setiap ruang kemungkinan solusi secara sistematis.
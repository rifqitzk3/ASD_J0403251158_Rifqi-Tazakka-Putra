# ==============================================
# NAMA  : Rifqi Tazakka Putra
# NIM   : J0403251158
# ==============================================

#==============================================================
# Materi Rekursif : Backtracking Biner dengan Pruning
#==============================================================

def biner_batas(n, batas, hasil="", jumlah_1=0):
    # Pruning: Jika jumlah angka '1' sudah lewat batas, jangan lanjut eksplorasi 
    if jumlah_1 > batas:
        return
    
    # Base case: Jika panjang string sesuai target 
    if len(hasil) == n:
        print(hasil)
        return
    
    # Pilih 0 (tidak menambah jumlah angka 1)
    biner_batas(n, batas, hasil + "0", jumlah_1)
    # Pilih 1 (menambah jumlah angka 1) 
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)

# Menghasilkan kombinasi 4-bit dengan maksimal dua angka '1'
print("Biner 4-bit (Maks 2 angka '1'):")
biner_batas(4, 2)


# Jadi intinya program ini bekerja lebih efisien daripada backtracking biner yang sebelumnya 
# karena program ini menerapkan strategi pruning (pemangkasan) untuk menghentikan eksplorasi cabang yang tidak memenuhi syarat.
# Alurnya mirip dengan backtracking biasa, namun terdapat pengecekan tambahan apakah jumlah angka '1' sudah melewati batas 
# yang ditentukan sebelum lanjut ke tahap berikutnya.
# Pengecekan pruning ini sangat penting karena program langsung menghentikan langkah (return) 
# jika syarat tidak terpenuhi, tanpa harus menunggu sampai base case.
# Hasilnya, pencarian menjadi lebih cepat karena cabang-cabang yang pasti salah tidak akan pernah ditelusuri sampai ujung.
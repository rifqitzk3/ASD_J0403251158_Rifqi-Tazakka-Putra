# ==============================================
# NAMA  : Rifqi Tazakka Putra
# NIM   : J0403251158
# ==============================================

def pangkat(a, n):
    # Base case: setiap angka pangkat 0 hasilnya 1 
    if n == 0:
        return 1
    # Recursive case: kalikan basis (a) dengan hasil pangkat (n-1)
    return a * pangkat(a, n - 1)

print(f"Hasil 2 pangkat 4: {pangkat(2, 4)}") # Output: 16 

# Jadi alurnya itu 
# Program ini bekerja dengan mengalikan basis secara berulang menggunakan pemanggilan fungsi ke dirinya sendiri dengan nilai pangkat yang lebih kecil. 
# Alurnya dimulai dengan pemanggilan rekursif yang terus menerus mengurangi nilai 'n' hingga mencapai kondisi berhenti. 
# Base case n=0 sangat krusial untuk memberikan nilai 1 sebagai elemen identitas perkalian agar fungsi berhenti dan hasil
# hitung mundur perkalian dapat diselesaikan. 
# Hasil akhir didapat dari perkalian berantai yang dihitung saat fungsi kembali dari base case menuju ke pemanggilan awal di dalam memori.
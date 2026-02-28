# =============================================
# Nama : Rifqi Tazakka Putra
# NIM  : J0403251158
# =============================================

# ======================================================================
# Materi : Fungsi Rekursif (Fungsi yang memanggil dirinya sendiri)
# Program : Faktorial
# Recursive Case = 3! = 3 x 2 x 1      
# Base Case = Kalau 0 berhenti
# ======================================================================

def factorial(n):
    # Base Case
    if n == 0:
        return 1
    # Recursive Case
    return n*factorial(n-1)  # n*n-1*n-2*n-3........n-?

print(factorial(5))

# Jadi intinya program ini bekerja dengan teknik rekursi di mana sebuah fungsi memanggil dirinya sendiri 
# untuk menyelesaikan sub-masalah yang ukurannya lebih kecil.
# Alurnya dimulai dengan pemanggilan rekursif yang terus memperkecil nilai 'n' hingga mencapai kondisi berhenti yang disebut base case.
# Base case (n==0) sangat krusial agar fungsi berhenti (tidak infinite recursion) dan mengembalikan nilai 1 sebagai hasil dasar faktorial.
# Hasil akhir didapat dari hasil perkalian 'n' dengan nilai faktorial (n-1) yang dihitung saat tumpukan fungsi mulai kembali satu per satu.
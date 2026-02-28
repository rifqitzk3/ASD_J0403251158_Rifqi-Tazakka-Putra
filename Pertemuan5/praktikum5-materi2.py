# =============================================
# Nama : Rifqi Tazakka Putra
# NIM  : J0403251158
# =============================================

# ======================================================================
# Materi : Call Stack
# Tracing bilangan (masuk-keluar)
# Input 3
# Masuk 3 - 2 - 1
# Keluar 1 - 2 - 3
# ======================================================================

def hitung(n):

    # Base Case 
    if n == 0:
        print("\nSelesai\n")
        return

    print("Masuk : ", n)
    hitung(n-1) # Recursive Case
    print("Keluar : ", n)

print("\n======== Program Tracing ========\n")
n = int(input("Masukkan angka: "))
hitung(n)

# Jadi intinya program ini bekerja untuk memperlihatkan urutan pemanggilan fungsi melalui proses stacking (masuk) 
# dan unwinding (keluar) di dalam memori.
# Alurnya mencatat setiap kali fungsi dipanggil (fase masuk) sebelum mencapai base case, yang membuat tumpukan atau call stack bertambah.
# Base case tercapai saat n==0, di mana program mencetak "Selesai" dan mulai mengurai tumpukan satu per satu dari yang paling atas.
# Fase keluar menunjukkan urutan eksekusi sisa perintah setelah pemanggilan rekursif selesai, 
# sehingga output yang dihasilkan akan muncul secara terbalik




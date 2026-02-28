# ==============================================
# NAMA  : Rifqi Tazakka Putra
# NIM   : J0403251158
# ==============================================

def buat_pin(panjang, hasil=""):
    # Base case: cetak hasil jika panjang PIN terpenuhi 
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return
    
    # Menggunakan loop untuk mencoba setiap opsi angka (0, 1, 2) 
    for angka in ["0", "1", "2"]:
        # Explore: panggil kembali dengan tambahan angka saat ini 
        buat_pin(panjang, hasil + angka)

print("Semua kemungkinan PIN 3-digit (0-2):")
buat_pin(3) # [cite: 1035]

# Jadi alurnya begini
# Program ini bekerja dengan strategi backtracking untuk mencari semua kemungkinan kombinasi PIN sepanjang 3 digit menggunakan angka 0, 1, dan 2. 
# Alurnya dimulai dengan mencoba setiap angka dari 0 sampai 2 menggunakan perulangan, lalu memanggil dirinya sendiri secara rekursif untuk 
# mengisi posisi digit berikutnya hingga membentuk struktur pohon keputusan. 
# Base case atau kondisi berhenti tercapai ketika panjang string PIN sudah mencapai 3 digit, 
# di mana sistem akan mencetak hasil tersebut dan melakukan backtrack (kembali) untuk mencoba pilihan angka lain pada posisi sebelumnya. 
# Agar angka yang sama tidak muncul berulang dalam satu PIN, 
# kita bisa menambahkan logika pengecekan (pruning) sebelum memanggil rekursi untuk memastikan angka yang dipilih belum ada dalam kombinasi PIN 
# yang sedang disusun.
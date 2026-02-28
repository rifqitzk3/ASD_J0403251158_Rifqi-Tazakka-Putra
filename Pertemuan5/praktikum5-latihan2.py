# ==============================================
# NAMA  : Rifqi Tazakka Putra
# NIM   : J0403251158
# ==============================================

def countdown(n):
    if n == 0:
        print("Selesai")
        return
    print("Masuk:", n)
    countdown(n - 1)
    print("Keluar:", n)

countdown(3)

# Jadi alurnya tuh gini
# Program ini bekerja dengan cara mencetak status eksekusi saat fungsi ditumpuk ke dalam memori (stacking) 
# dan saat dilepaskan kembali (unwinding). 
# Alurnya menggunakan dua fase utama, yaitu fase masuk untuk mencatat urutan pemanggilan 
# dari angka terbesar dan fase keluar untuk melihat urutan penyelesaian. 
# Base case n=0 berfungsi sebagai titik balik agar program berhenti memanggil dirinya sendiri 
# dan mulai mengurai tumpukan fungsi yang menggantung. 
# Output bagian 'Keluar' akan muncul secara terbalik karena mengikuti prinsip Last In First Out (LIFO), 
# di mana fungsi terakhir yang masuk adalah yang pertama kali selesai.
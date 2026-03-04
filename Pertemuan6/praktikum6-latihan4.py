#==============================================================
# Nama : Rifqi Tazakka Putra
# NIM  : J0403251158
# Kelas: TPL B1
#==============================================================

def merge_sort(data): 
    if len(data) <= 1: 
        return data 
     
    mid = len(data) // 2 
    left = data[:mid] 
    right = data[mid:] 
     
    left_sorted = merge_sort(left) 
    right_sorted = merge_sort(right) 
     
    return merge(left_sorted, right_sorted) 

'''
Soal: 
1. Apa yang dimaksud dengan base case? 
2. Mengapa fungsi memanggil dirinya sendiri? 
3. Apa tujuan fungsi merge()?

Jawab:
1. Batas atau kondisi berhenti yang sangat penting dalam rekursi supaya fungsi tidak terus-menerus memanggil dirinya sendiri selamanya. 
   Di kode ini, base case-nya adalah saat panjang data sudah $\le 1$, karena list yang isinya cuma satu angka itu otomatis sudah terurut.
2. Untuk memecah masalah besar menjadi potongan-potongan kecil secara berulang (prinsip Divide and Conquer). 
3. Tujuannya adalah untuk menggabungkan kembali (menyisip) dua bagian list yang sudah terurut tadi menjadi 
   satu list baru yang tetap rapi dan terurut dari kecil ke besar.

'''
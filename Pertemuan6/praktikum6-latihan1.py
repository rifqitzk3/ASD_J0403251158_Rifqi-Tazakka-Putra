#==============================================================
# Nama : Rifqi Tazakka Putra
# NIM  : J0403251158
# Kelas: TPL B1
#==============================================================

def insertion_sort(data): 
    for i in range(1, len(data)): 
        key = data[i] 
        j = i - 1 
         
        while j >= 0 and data[j] > key: 
            data[j + 1] = data[j] 
            j -= 1 
         
        data[j + 1] = key 
     
    return data 

'''

Soal: 
1. Mengapa perulangan dimulai dari indeks 1? 
2. Apa fungsi variabel key? 
3. Mengapa digunakan while, bukan for? 
4. Operasi apa yang terjadi di dalam while?

Jawab:
1. Perulangan dimulai dari indeks 1 karena Insertion Sort menganggap elemen pertama 
   (indeks 0) sudah berada di posisi yang benar atau "sudah terurut" dalam kelompoknya sendiri.
2. Variabel key berfungsi sebagai penampung sementara untuk nilai yang sedang kita coba masukkan ke posisi yang benar.
3. Supaya lebih efisien karena prosesnya bisa langsung berhenti begitu posisi yang pas buat key sudah ketemu atau 
   sudah mentok di ujung, jadi nggak perlu buang tenaga buat ngecek sisa angka yang nggak perlu seperti kalau pakai for
4. Di dalam blok while terjadi operasi/proses pergeseran angka ke kanan melalui penyalinan data[j] ke 
   posisi j + 1 sambil memundurkan pengecekan ke kiri (j -= 1) guna membuka ruang kosong bagi variabel key di tempat yang paling tepat.

'''
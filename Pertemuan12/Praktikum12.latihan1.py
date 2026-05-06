# Nama  : Rifqi Tazakka Putra 
# NIM   : J0403251158
# Kelas : TPL-B1
# Praktikum 12 - Graph II: Shortest Path 

# ========================================================== 
# Latihan 1: Weighted Graph dan Perhitungan Jalur 
# ========================================================== 

# Representasi weighted graph menggunakan dictionary bersarang 
graph = { 
'A': {'B': 4, 'C': 2}, 
'B': {'D': 5}, 
'C': {'D': 1}, 
'D': {} 
} 

# Menghitung dua kemungkinan jalur dari A ke D 
jalur_1 = graph['A']['B'] + graph['B']['D'] 
jalur_2 = graph['A']['C'] + graph['C']['D'] 
print("Jalur 1: A -> B -> D =", jalur_1) 
print("Jalur 2: A -> C -> D =", jalur_2) 
  # A -> B -> D 
  # A -> C -> D 
if jalur_1 < jalur_2: 
    print("Jalur terpendek adalah A -> B -> D") 
else: 
    print("Jalur terpendek adalah A -> C -> D") 
    
    
# Jawaban Analisis: 
# 1. Berapa total bobot jalur A -> B -> D? 
# A ke B bobotnya 4, lalu B ke D bobotnya 5. Jadi totalnya 4 + 5 = 9
# 2. Berapa total bobot jalur A -> C -> D? 
# A ke C bobotnya 2, lalu C ke D bobotnya 1. Jadi totalnya 2 + 1 = 3
# 3. Jalur mana yang dipilih sebagai jalur terpendek? 
# Yang dipilih adalah A → C → D karena total bobotnya hanya 3, jauh lebih kecil dibanding A → B → D yang totalnya 9
# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?
# Karena di weighted graph, setiap edge punya "biaya" yang berbeda-beda 
# bisa merepresentasikan jarak, waktu, ongkos, dll. Jumlah edge hanya menghitung berapa kali berpindah, 
# bukan seberapa berat perjalanannya.
# Nama  : Rifqi Tazakka Putra 
# NIM   : J0403251158
# Kelas : TPL-B1
# Praktikum 12 - Graph II: Shortest Path 

# ========================================================== 
# Latihan 2: Implementasi Dijkstra 
# ==========================================================

import heapq 
# Weighted graph dengan bobot positif 
graph = { 
'A': {'B': 4, 'C': 2}, 
'B': {'D': 5}, 
'C': {'D': 1}, 
'D': {} 
} 

def dijkstra(graph, start): 
    ''' 
    Fungsi untuk mencari jarak terpendek dari node start 
    ke seluruh node lain menggunakan algoritma Dijkstra. 
    ''' 
    # Semua jarak awal dibuat tak hingga 
    distances = {node: float('inf') for node in graph} 
    # Jarak dari start ke start adalah 0 
    distances[start] = 0 
    # Priority queue menyimpan pasangan (jarak, node) 
    priority_queue = [(0, start)] 
 
 
    while priority_queue: 
        current_distance, current_node = heapq.heappop(priority_queue) 
 
        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat, 
        # maka proses dilewati 
        if current_distance > distances[current_node]: 
            continue 
 
        # Periksa semua tetangga dari node saat ini 
        for neighbor, weight in graph[current_node].items(): 
            distance = current_distance + weight 
 
            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya 
            if distance < distances[neighbor]: 
                distances[neighbor] = distance 
                heapq.heappush(priority_queue, (distance, neighbor)) 
 
    return distances 
 

hasil = dijkstra(graph, 'A') 
 
print("Jarak terpendek dari node A:") 

for node, distance in hasil.items(): 
    print(node, "=", distance)


# Jawaban Analisis: 
# 1. Berapa jarak terpendek dari A ke B? 
# 4, hanya ada satu jalur yaitu A → B langsung dengan bobot 4

# 2. Berapa jarak terpendek dari A ke C? 
# 2, hanya ada satu jalur yaitu A → C langsung dengan bobot 2

# 3. Berapa jarak terpendek dari A ke D? 
# 3, dicapai lewat jalur A → C → D dengan total bobot 2 + 1 = 3

# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B? 
# Meskipun sama-sama 2 langkah, bobot tiap edge-nya berbeda jauh. 
# Jalur lewat C jauh lebih "murah" karena edge C → D hanya berbobot 1, sedangkan B → D berbobot 5. 
# Ini bukti bahwa jumlah langkah tidak menentukan jalur terpendek yang menentukan adalah total bobotnya

# 5. Apa fungsi priority_queue dalam algoritma Dijkstra? 
# Priority queue bertugas memastikan Dijkstra selalu memproses node dengan jarak terkecil terlebih dahulu. 
# Ibarat antrian rumah sakit pakai sistem triase — siapa yang paling kritis (paling dekat) dilayani duluan, 
# bukan siapa yang datang duluan. Tanpa priority queue, kita bisa saja memproses node yang jauh lebih dulu dan menghasilkan keputusan yang salah.

# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif? 
# Dijkstra berasumsi bahwa begitu sebuah node diproses, jaraknya sudah final dan tidak bisa lebih kecil lagi. 
# Dengan bobot negatif, asumsi ini bisa salah — bisa saja ada jalur yang awalnya terlihat jauh, 
# tapi setelah melewati edge negatif justru jadi lebih dekat. Dijkstra tidak akan kembali mengecek node yang sudah diproses, 
# sehingga hasilnya bisa keliru. Untuk kasus bobot negatif, gunakan Bellman-Ford yang memang dirancang untuk mengatasinya.
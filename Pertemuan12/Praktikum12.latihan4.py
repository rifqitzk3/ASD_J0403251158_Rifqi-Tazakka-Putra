# Nama  : Rifqi Tazakka Putra 
# NIM   : J0403251158
# Kelas : TPL-B1
# Praktikum 12 - Graph II: Shortest Path 

# ========================================================== 
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus 
# Algoritma: Dijkstra 
# ========================================================== 
import heapq 
# Graph lokasi kampus 
# Bobot menunjukkan waktu tempuh dalam menit 
graph = { 
'Gerbang': {'Perpustakaan': 6, 'Kantin': 2}, 
'Perpustakaan': {'Lab': 3}, 
'Kantin': {'Lab': 4, 'Aula': 7}, 
'Lab': {'Aula': 1}, 
'Aula': {} 
} 
def dijkstra(graph, start): 
    distances = {node: float('inf') for node in graph} 
    distances[start] = 0 
    priority_queue = [(0, start)] 
    while priority_queue: 
        current_distance, current_node = heapq.heappop(priority_queue) 
        if current_distance > distances[current_node]: 
            continue 
        for neighbor, weight in graph[current_node].items(): 
            distance = current_distance + weight 
            if distance < distances[neighbor]: 
                distances[neighbor] = distance 
                heapq.heappush(priority_queue, (distance, neighbor)) 
    return distances 

hasil = dijkstra(graph, 'Gerbang') 
print("Jarak terpendek dari Gerbang Kampus:") 
for lokasi, jarak in hasil.items(): 
    print(lokasi, "=", jarak, "menit")


# Jawaban Analisis: 
# 1. Lokasi mana yang paling dekat dari Gerbang? 
# Kantin, dengan waktu tempuh hanya 2 menit langsung dari Gerbang

# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula? 
# 7 menit, lewat jalur Gerbang → Kantin → Lab → Aula dengan total 2 + 4 + 1 = 7 menit

# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan. 
# Tidak selalu. Contohnya jalur ke Lab — tidak ada jalur langsung dari Gerbang, tapi bisa dicapai lewat dua rute:
# Gerbang -> Perpustakaan -> Lab  =  6 + 3  =  9 menit
# Gerbang -> Kantin -> Lab        =  2 + 4  =  6 menit  
# Jalur yang lebih banyak langkahnya justru bisa lebih cepat jika bobot tiap edgenya kecil. 
# Yang penting total bobotnya, bukan jumlah langkahnya.

# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
# Karena semua bobot di graph ini positif (waktu tempuh tidak mungkin minus). 
# Dijkstra dirancang khusus untuk kondisi ini dan bekerja sangat efisien 
# selalu memproses lokasi terdekat duluan menggunakan priority queue, 
# sehingga hasilnya pasti optimal tanpa perlu mengecek ulang semua kemungkinan seperti Bellman-Ford.
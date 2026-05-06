# ==============================================
# Nama : Rifqi Tazakka Putra
# NIM  : J0403251158
#===============================================
# Implemantasi Djikstra
#===============================================

import heapq 
graph = { 
'A': {'B': 4, 'C': 2}, 
'B': {'D': 5}, 
'C': {'D': 1}, 
'D': {} 
}

def dijkstra(graph, start): 
    # Menyimpan jarak minimum 
    distances = {node: float('inf') for node in graph} 
 
    # Jarak node awal = 0 
    distances[start] = 0 
 
    # Priority queue 
    pq = [(0, start)] 
 
    while pq: 
        current_distance, current_node = heapq.heappop(pq) 
 
        # Periksa semua tetangga 
        for neighbor, weight in graph[current_node].items(): 
 
            distance = current_distance + weight 
 
            # Jika ditemukan jarak lebih kecil 
            if distance < distances[neighbor]: 
 
                distances[neighbor] = distance 
 
                heapq.heappush(pq, (distance, neighbor)) 
 
    return distances 
 
hasil = dijkstra(graph, 'A') 
print(hasil)


# ==========================================================
# Kesimpulan:
# Algoritma Dijkstra berhasil menemukan jarak terpendek dari
# node A ke semua node lain. Hasilnya — A ke B = 4, A ke C = 2,
# dan A ke D = 3 (bukan 9 lewat B, melainkan lewat C: 2+1=3).
# Ini membuktikan bahwa jalur terpendek tidak selalu jalur
# langsung, melainkan jalur dengan total bobot terkecil.
# Dijkstra bekerja efisien karena priority queue memastikan
# node dengan jarak terkecil selalu diproses lebih dulu.
# ==========================================================

# Nama  : Rifqi Tazakka Putra 
# NIM   : J0403251158
# Kelas : TPL-B1
# Praktikum 12 - Graph II: Shortest Path 

# ========================================================== 
# Latihan 3: Implementasi Bellman-Ford 
# ========================================================== 
 
# Weighted graph dengan bobot negatif 
graph = { 
    'A': {'B': 5, 'C': 4}, 
    'B': {}, 
    'C': {'B': -2} 
} 
 
def bellman_ford(graph, start): 
    """ 
    Fungsi untuk mencari jarak terpendek dari node start 
    ke seluruh node lain menggunakan algoritma Bellman-Ford. 
    """ 
 
    # Semua jarak awal dibuat tak hingga 
    distances = {node: float('inf') for node in graph} 
 
    # Jarak dari start ke start adalah 0 
    distances[start] = 0 
 
    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1 
    for _ in range(len(graph) - 1): 
 
        # Periksa semua edge 
        for node in graph: 
            for neighbor, weight in graph[node].items(): 
 
                # Jika jarak ke node saat ini sudah diketahui, 
                # dan ditemukan jarak yang lebih kecil ke neighbor, 
                # maka lakukan update jarak 
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]: 
                    distances[neighbor] = distances[node] + weight 
 
    return distances 
 
 
hasil = bellman_ford(graph, 'A') 
 
print("Jarak terpendek dari node A:") 
for node, distance in hasil.items(): 
    print(node, "=", distance)


# Jawaban Analisis: 
# 1. Berapa bobot langsung dari A ke B? 
# 5, terlihat langsung di graph: 'A': {'B': 5, ...}.

# 2. Berapa total bobot jalur A -> C -> B? 
# 2, A ke C bobotnya 4, lalu C ke B bobotnya -2. Totalnya 4 + (-2) = 2

# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B? 
# Jalur A → C → B lebih kecil karena edge C → B berbobot negatif (-2) yang "memotong" total jarak.

# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif? 
# Karena Bellman-Ford tidak berasumsi bahwa jarak yang sudah ditemukan itu final. 
# Ia melakukan relaksasi berulang sebanyak V-1 kali terhadap semua edge, 
# sehingga setiap kemungkinan jalur termasuk yang melewati bobot negatif pasti akan dievaluasi dan diperbarui.
# Berbeda dengan Dijkstra yang langsung "mengunci" jarak begitu node diproses.

# 5. Apa yang dimaksud dengan proses relaksasi edge? 
# Relaksasi adalah proses mencoba memperbarui jarak ke suatu node jika ditemukan jalur yang lebih pendek

# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
# Dijkstra lebih cepat tapi hanya untuk bobot positif. 
# Bellman-Ford lebih lambat tapi lebih tangguh karena bisa menangani bobot negatif sekaligus mendeteksi jika ada siklus negatif yang berbahaya.

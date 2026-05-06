# Nama  : Rifqi Tazakka Putra 
# NIM   : J0403251158
# Kelas : TPL-B1
# Praktikum 12 - Graph II: Shortest Path 

# ==========================================================
# Latihan 5: Studi Kasus Jalur Terpendek Antar Kota
# Algoritma: Djikstra
# ==========================================================

import heapq

# 1. Representasi graph berbobot menggunakan dictionary
#    Format: { kota: { tetangga: bobot, ... }, ... }
graph = {
    'Bogor'  : {'Jakarta': 5, 'Depok': 2},
    'Depok'  : {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

# ==========================================================
# 2. Fungsi Dijkstra
# ==========================================================

def dijkstra(graph, start):
    '''
    Mencari jarak terpendek dari node start ke seluruh node lain.
    Menggunakan priority queue (min-heap) agar selalu memproses
    node dengan jarak terkecil terlebih dahulu.
    '''

    # Inisialisasi semua jarak sebagai tak hingga
    distances = {node: float('inf') for node in graph}
    predecessors = {node: None for node in graph}

    # Jarak dari start ke dirinya sendiri = 0
    distances[start] = 0

    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Lewati jika jarak ini sudah usang (ada yang lebih kecil)
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Update jika ditemukan jalur yang lebih pendek
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node  # catat jalur
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, predecessors


def get_path(predecessors, start, end):
    '''Rekonstruksi jalur dari start ke end menggunakan predecessors.'''
    path = []
    current = end

    while current is not None:
        path.append(current)
        current = predecessors[current]

    path.reverse()

    # Jika titik awal bukan start, berarti tidak ada jalur
    if not path or path[0] != start:
        return None

    return path


# ==========================================================
# 3. Penentuan node awal
# ==========================================================

start_node = 'Bogor'

# Jalankan algoritma Dijkstra
distances, predecessors = dijkstra(graph, start_node)

# ==========================================================
# 4. Output jarak terpendek dari node awal ke semua node
# ==========================================================

print(f"Jarak terpendek dari {start_node}:")
print()

for node in graph:
    path  = get_path(predecessors, start_node, node)
    path_str = " -> ".join(path) if path else "Tidak terjangkau"

    if distances[node] == float('inf'):
        print(f"  {start_node} -> {node} = Tidak terjangkau")
    else:
        print(f"  {path_str} = {distances[node]}")


# Jawaban Analisis: 
# 1. Node awal yang digunakan apa? 
# Bogor, ditentukan lewat variabel start_node = 'Bogor' di bagian penentuan node awal

# 2. Node mana yang memiliki jarak paling kecil dari node awal? 
# Depok, dengan jarak hanya 2, dicapai langsung dari Bogor dengan satu edge berbobot 2

# 3. Node mana yang memiliki jarak paling besar dari node awal? 
# Bandung, dengan jarak 8 dicapai lewat jalur Bogor → Depok → Bandung dengan total 2 + 6 = 8.

# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
# Algoritma Dijkstra dimulai dengan mencatat jarak Bogor = 0 dan semua kota lain tak hingga, 
# lalu memasukkan Bogor ke priority queue. Bogor diproses pertama karena jaraknya terkecil 
# dari sini ditemukan dua tetangga, Jakarta dicatat 5 menit dan Depok dicatat 2 menit, keduanya masuk ke queue. 
# Queue lalu memilih Depok karena jaraknya paling kecil (2), dan dari Depok ditemukan bahwa Jakarta bisa dicapai dalam 2 + 2 = 4 menit 
# yang ternyata lebih kecil dari catatan sebelumnya (5), sehingga langsung diperbarui — selain itu Bandung juga dicatat 2 + 6 = 8 menit. 
# Berikutnya Jakarta diproses dengan jarak 4, dicek ke Bandung hasilnya 4 + 7 = 11 yang lebih besar dari 8 yang sudah tercatat 
# sehingga tidak diupdate. Di queue masih ada sisa Jakarta lama dengan jarak 5 dari langkah pertama, 
# tapi karena jarak Jakarta di catatan sudah 4, entri lama itu dianggap kadaluarsa dan langsung dilewati. 
# Terakhir Bandung diproses dengan jarak 8, tidak punya tetangga, 
# dan algoritma pun selesai dengan hasil akhir Bogor = 0, Depok = 2, Jakarta = 4 lewat Depok bukan jalur langsung, dan Bandung = 8.



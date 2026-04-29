# ======================================================
# Nama : Rifqi Tazakka Putra
# NIM  : J0403251158
# ======================================================
# Breadth First Search (BFS) [Luas]
# ======================================================

from collections import deque

# Representasi Graph

graph = {
    'A' : ['B', 'C'],
    'B' : ['A', 'D'],
    'C' : ['A', 'D'],
    'D' : ['B', 'C']
}

def bfs(graph, start):
    # Fungsi untuk melakukan penelusuran/pencarian pada graph dengan BFS 
    # Graph : Dictionary yang menyimpan struktur dari graph
    # Start : Node awal penelusuran
    
    # Queue digunakan untuk menyimpan node yang akan diproses atau dibaca  
    queue = deque()
    
    # Variabel yang digunakan untuk menyimpan node yang sudah diproses/sudah dikunjungi
    visited = set()
    
    # Masukkan node awal ke queue
    queue.append(start)
    
    # Tandai node awal yang sudah masuk queue tadi sebagai node yang sudah dikunjungi
    visited.add(start)
    
    while queue:
        # Mengambil node paling depan dari queue 
        node = queue.popleft()
        print(node)
        
        # Periksa semua tetangga dari node yang diambil
        for neighbor in graph[node]:
            # Jika tetangga belum dikunjungi
            if neighbor not in visited:
                # Tandai sebagai sudah dikunjungi
                visited.add(neighbor)
                # Masukkan tetangga ke queue untuk diproses nanti
                queue.append(neighbor)
                
                
# Menjalankan BFS dari node A
bfs(graph, 'A')

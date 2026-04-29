# ======================================================
# Nama : Rifqi Tazakka Putra
# NIM  : J0403251158
# ======================================================
# Depth First Search (DFS) [Kedalaman]
# ======================================================

# Representasi graph

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def dfs(graph, node, visited):
    # Fungsi untuk melakukan penelusuran graph menggunakan DFS
    # Graph  : dictionary yang menyimpan graph
    # Node   : menyimpan node yang sedang dikunjungi
    # Visited: menyimpan node yang sudah dikunjungi
    
    # Tandai node saat ini sebagai node yang sudah dikunjungi
    visited.add(node)
    
    # Tampilkan node yang sedang dikunjungi
    print(node, end=" ")
    
    # Periksa semua tetangga dari node saat ini
    for neighbor in graph[node]:
    
    # Jika tetangga belum pernah dikunjungi
        if neighbor not in visited:
            # Lakukan DFS secara rekursif ke tetangga terdekat
            dfs(graph, neighbor, visited)


# Variabel yang digunakan untuk menyimpan node yang sudah diproses/sudah dikunjungi
visited = set()

# Menjalankan DFS dari A
dfs(graph, 'A', visited)
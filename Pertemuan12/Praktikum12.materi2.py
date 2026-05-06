# ==============================================
# Nama : Rifqi Tazakka Putra
# NIM  : J0403251158
#===============================================
# Implemantasi Bellman Ford
#===============================================

def bellman_ford(graph, start):
    distances = {node: float('inf') for node in graph}
    predecessors = {node: None for node in graph}
    distances[start] = 0

    # Relaksasi sebanyak V-1 kali
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    predecessors[neighbor] = node  # catat jalur

    # Deteksi negative cycle (iterasi ke-V)
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] + weight < distances[neighbor]:
                raise ValueError(f"Negative cycle terdeteksi di node: {neighbor}")

    return distances, predecessors


def get_path(predecessors, start, end):
    """Rekonstruksi jalur dari start ke end."""
    path = []
    current = end

    while current is not None:
        path.append(current)
        current = predecessors[current]

    path.reverse()

    if path[0] != start:
        return None  # Tidak ada jalur

    return path

# Contoh Penggunaan
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'C': -1, 'D': 5},
    'C': {'D': 8, 'E': 10},
    'D': {'E': 2},
    'E': {}
}

start_node = 'A'

try:
    distances, predecessors = bellman_ford(graph, start_node)

    print(f"=== Bellman-Ford dari node '{start_node}' ===\n")

    for node in graph:
        if distances[node] == float('inf'):
            print(f"  {start_node} -> {node} : Tidak terjangkau")
        else:
            path = get_path(predecessors, start_node, node)
            path_str = " -> ".join(path)
            print(f"  {start_node} -> {node} : jarak = {distances[node]:<5} | jalur = {path_str}")

except ValueError as e:
    print(f"ERROR: {e}")


# ============================================================
# Kesimpulan:
# Bellman-Ford berhasil menemukan jalur terpendek dari node A
# ke semua node lain, termasuk melewati edge berbobot negatif
# (B -> C = -1). Hasilnya berbeda dari Dijkstra karena
# relaksasi dilakukan berulang V-1 kali sehingga pengaruh
# bobot negatif ikut diperhitungkan. Selain itu, algoritma
# ini dilengkapi deteksi negative cycle — jika ada siklus
# yang terus-menerus mengurangi jarak, program langsung
# melempar error daripada looping tanpa henti.
# ============================================================
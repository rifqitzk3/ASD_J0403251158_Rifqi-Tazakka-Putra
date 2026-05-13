# Nama  : Rifqi Tazakka Putra
# NIM   : J0403251158
# Kelas : TPL-B1
# Praktikum 13 - Graph III: Spanning Tree
# File  : praktikum13.materi2.py
# Materi: Implementasi Algoritma Prim

# ==========================================================
# MATERI 2 - Implementasi Algoritma Prim
# ==========================================================
# Algoritma Prim membangun MST dengan cara:
# 1. Mulai dari satu node awal
# 2. Dari node yang sudah dikunjungi, cari edge terkecil
#    yang menghubungkan ke node yang belum dikunjungi
# 3. Tambahkan node dan edge tersebut ke MST
# 4. Ulangi sampai semua node terhubung

# Perbedaan dengan Kruskal:
# - Kruskal: memilih edge terkecil secara GLOBAL
# - Prim   : memilih edge terkecil dari node yang sudah DIKUNJUNGI
# ==========================================================

import heapq  # Modul untuk priority queue (min-heap)

# Representasi graph sebagai adjacency dictionary
# Format: { node: { tetangga: bobot, ... }, ... }
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    """
    Fungsi untuk mencari MST menggunakan algoritma Prim.
    Parameter:
        graph : adjacency dictionary berisi node dan bobot edge
        start : node awal untuk memulai pembangunan MST
    Return:
        mst          : list edge yang terpilih (u, v, bobot)
        total_weight : total bobot MST
    """

    visited = set([start])  # Set node yang sudah masuk ke MST
    edges = []              # Priority queue (min-heap) untuk kandidat edge

    # Masukkan semua edge dari node awal ke dalam heap
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []           # List untuk menyimpan edge MST
    total_weight = 0   # Total bobot MST

    print(f"\nMulai dari node: {start}")
    print(f"Kandidat edge awal dari {start}: {list(graph[start].items())}")
    print("\nProses pemilihan edge:")

    while edges:
        # Ambil edge dengan bobot terkecil dari heap
        weight, u, v = heapq.heappop(edges)

        if v not in visited:
            # Node v belum dikunjungi → edge ini aman, tidak membentuk cycle
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
            print(f"  ✓ Pilih edge {u}-{v} (bobot {weight}) → Node aktif: {visited}")

            # Tambahkan edge-edge baru dari node v ke dalam heap
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
        else:
            # Node v sudah ada di MST → edge ini akan membentuk cycle
            print(f"  ✗ Lewati edge {u}-{v} (bobot {weight}) → {v} sudah dikunjungi")

    return mst, total_weight


# Jalankan algoritma Prim mulai dari node 'A'
mst, total = prim(graph, 'A')

print("\n" + "=" * 50)
print("Hasil Minimum Spanning Tree (Prim):")
print("=" * 50)
for edge in mst:
    print(f"  {edge[0]} -- {edge[1]}  bobot: {edge[2]}")
print(f"\nTotal bobot MST = {total}")
print("=" * 50)

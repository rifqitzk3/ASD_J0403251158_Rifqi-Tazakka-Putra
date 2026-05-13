# Nama  : Rifqi Tazakka Putra
# NIM   : J0403251158
# Kelas : TPL-B1
# Praktikum 13 - Graph III: Spanning Tree
# File  : praktikum13.latihan3.py
# Latihan 3: Implementasi Algoritma Prim

# ==========================================================
# LATIHAN 3 - Implementasi Algoritma Prim
# ==========================================================
# Prim membangun MST bertahap dari satu node awal.
# Setiap langkah memilih edge TERKECIL dari node-node
# yang sudah ada di MST menuju node yang belum dikunjungi.
# ==========================================================

import heapq  # Digunakan untuk priority queue (min-heap)

# Representasi graph sebagai adjacency dictionary
# Format: { node: { tetangga: bobot } }
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    """
    Algoritma Prim untuk mencari Minimum Spanning Tree.
    Berbeda dengan Kruskal yang memilih edge secara global,
    Prim memperluas tree dari node yang sudah dikunjungi.
    """

    visited = set([start])  # Set node yang sudah masuk MST, dimulai dari node awal
    edges = []              # Min-heap untuk kandidat edge berikutnya

    # Masukkan semua edge dari node awal ke priority queue
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []           # Menyimpan edge-edge hasil MST
    total_weight = 0   # Total bobot MST

    print(f"  Node awal: {start}")
    print(f"  Edge kandidat dari {start}: {sorted(graph[start].items(), key=lambda x: x[1])}")
    print("\nProses Prim step-by-step:")

    step = 1
    while edges:
        # Ambil edge dengan bobot terkecil dari heap
        weight, u, v = heapq.heappop(edges)

        if v not in visited:
            # Node v belum ada di MST → aman untuk ditambahkan
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
            print(f"  Step {step}: Pilih {u}-{v} (bobot {weight}) | Node aktif: {sorted(visited)}")
            step += 1

            # Tambahkan semua edge dari node v yang belum dikunjungi ke heap
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
        else:
            # Node v sudah dikunjungi → edge ini akan membentuk cycle, lewati
            print(f"  Skip: {u}-{v} (bobot {weight}) → {v} sudah ada di MST")

    return mst, total_weight


print("=" * 50)
print("  LATIHAN 3 - Algoritma Prim")
print("=" * 50)
print()

# Jalankan Prim mulai dari node 'A'
mst, total = prim(graph, 'A')

print("\n" + "=" * 50)
print("Minimum Spanning Tree:")
for edge in mst:
    print(f"  {edge[0]} -- {edge[1]}  bobot: {edge[2]}")
print(f"\nTotal bobot = {total}")
print("=" * 50)

# ==========================================================
# Jawaban Analisis:
#
# 1. Node awal apa yang digunakan?
#    → Node 'A' digunakan sebagai node awal/starting point.
#      Pemilihan node awal tidak mempengaruhi hasil MST akhir,
#      hanya mempengaruhi urutan pemilihan edge.
#
# 2. Edge mana yang dipilih pertama kali?
#    → Edge A-C (bobot 2) dipilih pertama karena dari node A,
#      edge terkecil yang tersedia adalah A-C dengan bobot 2.
#      (A-B=4, A-C=2, A-D=5 → yang terkecil A-C)
#
# 3. Bagaimana Prim menentukan edge berikutnya?
#    → Prim menggunakan min-heap (priority queue). Setiap kali
#      node baru ditambahkan ke MST, semua edge dari node tersebut
#      ke node yang belum dikunjungi dimasukkan ke heap.
#      Selanjutnya, edge dengan bobot terkecil dari heap dipilih.
#      Proses: A → pilih A-C(2) → dari C tambah C-D(1) →
#      pilih C-D(1) → dari D tambah D-B(3) → pilih D-B(3) → selesai
#
# 4. Berapa total bobot MST yang dihasilkan?
#    → Total bobot = 2 + 1 + 3 = 6
#      Edge yang dipilih: A-C(2), C-D(1), D-B(3)
#
# 5. Apa perbedaan pendekatan Prim dan Kruskal?
#    → Kruskal : mengurutkan SEMUA edge lebih dulu, lalu memilih
#                dari yang terkecil secara global. Berorientasi pada EDGE.
#                Cocok untuk sparse graph (sedikit edge).
#    → Prim    : mulai dari satu node, lalu memperluas MST ke node
#                tetangga terdekat. Berorientasi pada NODE.
#                Cocok untuk dense graph (banyak edge).
#    → Keduanya menghasilkan MST dengan total bobot yang sama.
# ==========================================================

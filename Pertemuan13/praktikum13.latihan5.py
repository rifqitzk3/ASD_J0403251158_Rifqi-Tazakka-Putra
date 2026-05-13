# Nama  : Rifqi Tazakka Putra
# NIM   : J0403251158
# Kelas : TPL-B1
# Praktikum 13 - Graph III: Spanning Tree
# File  : praktikum13.latihan5.py
# Latihan 5: Tugas Mandiri - MST dengan Kasus Baru

# ==========================================================
# LATIHAN 5 - Tugas Mandiri: MST Kasus Baru
# ==========================================================
# Kasus yang dipilih: KASUS 2 - Jaringan Komputer
#
# Deskripsi:
# Sebuah jaringan komputer memiliki beberapa router yang perlu
# dihubungkan. Setiap jalur antar router memiliki biaya berbeda.
# Tujuan: hubungkan semua router dengan total biaya MINIMUM.
#
# Data jaringan:
#   RouterA - RouterB = 3
#   RouterA - RouterC = 2
#   RouterB - RouterD = 5
#   RouterC - RouterD = 1
#   RouterB - RouterC = 4
#
# Algoritma yang digunakan: PRIM
# Alasan: Graph direpresentasikan sebagai adjacency dictionary,
#         struktur ini lebih cocok untuk Prim.
# ==========================================================

import heapq  # Untuk priority queue pada algoritma Prim

# -------------------------------------------------------
# Representasi weighted graph sebagai adjacency dictionary
# -------------------------------------------------------
graph = {
    'RouterA': {'RouterB': 3, 'RouterC': 2},
    'RouterB': {'RouterA': 3, 'RouterD': 5, 'RouterC': 4},
    'RouterC': {'RouterA': 2, 'RouterD': 1, 'RouterB': 4},
    'RouterD': {'RouterB': 5, 'RouterC': 1}
}

# -------------------------------------------------------
# Implementasi Algoritma Prim
# -------------------------------------------------------
def prim(graph, start):
    """
    Mencari MST menggunakan algoritma Prim.
    Membangun tree secara bertahap dari satu node awal.
    Setiap langkah memilih edge terkecil menuju node baru.

    Parameter:
        graph : dict adjacency berisi node dan bobot
        start : node awal
    Return:
        mst          : list edge MST
        total_weight : total bobot minimum
    """

    visited = set([start])  # Mulai dari node awal
    heap = []               # Priority queue untuk kandidat edge

    # Masukkan semua edge dari node awal ke heap
    for neighbor, weight in graph[start].items():
        heapq.heappush(heap, (weight, start, neighbor))

    mst = []           # Edge yang terpilih
    total_weight = 0   # Total bobot MST

    print(f"  Mulai dari: {start}")
    print(f"  Edge kandidat awal: {sorted(graph[start].items(), key=lambda x: x[1])}")
    print("\nProses Prim step-by-step:")

    step = 1
    while heap:
        weight, u, v = heapq.heappop(heap)  # Ambil edge terkecil

        if v not in visited:
            # Node v belum ada di MST → tambahkan
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
            print(f"  Step {step}: Pilih {u} → {v} (biaya {weight}) | Router terhubung: {sorted(visited)}")
            step += 1

            # Tambahkan edge baru dari v ke heap
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(heap, (w, v, neighbor))
        else:
            # Router v sudah terhubung → lewati untuk hindari cycle
            print(f"  Skip: {u} → {v} (biaya {weight}) | {v} sudah terhubung")

    return mst, total_weight


# -------------------------------------------------------
# Jalankan program dan tampilkan hasil
# -------------------------------------------------------
print("=" * 60)
print("  LATIHAN 5 - Jaringan Komputer (Algoritma Prim)")
print("=" * 60)
print("\nData koneksi antar router:")
all_edges_shown = set()
for node, neighbors in graph.items():
    for neighbor, weight in neighbors.items():
        pair = tuple(sorted([node, neighbor]))
        if pair not in all_edges_shown:
            print(f"  {node} ↔ {neighbor}  biaya: {weight}")
            all_edges_shown.add(pair)
print()

mst, total = prim(graph, 'RouterA')

print("\n" + "=" * 60)
print("HASIL MST: Koneksi router dengan biaya minimum")
print("=" * 60)
for i, edge in enumerate(mst, 1):
    print(f"  {i}. Hubungkan: {edge[0]} ↔ {edge[1]}  biaya: {edge[2]}")
print(f"\nTotal bobot MST          = {total}")
print(f"Jumlah koneksi yang dibuat = {len(mst)}")
print("=" * 60)

# Tampilkan edge yang TIDAK dipilih beserta alasannya
print("\nEdge yang TIDAK dipilih dalam MST:")
all_edges = [
    ('RouterA', 'RouterB', 3),
    ('RouterA', 'RouterC', 2),
    ('RouterB', 'RouterD', 5),
    ('RouterC', 'RouterD', 1),
    ('RouterB', 'RouterC', 4)
]
mst_pairs = {(u, v) for u, v, w in mst} | {(v, u) for u, v, w in mst}
for u, v, w in all_edges:
    if (u, v) not in mst_pairs:
        print(f"  {u} ↔ {v} (biaya {w}) → tidak dipilih karena akan membentuk cycle")

# ==========================================================
# Jawaban Analisis:
#
# 1. Kasus apa yang dipilih?
#    → Kasus 2: Jaringan Komputer — menghubungkan 4 router
#      (RouterA, RouterB, RouterC, RouterD) dengan biaya minimum.
#
# 2. Algoritma apa yang digunakan?
#    → Algoritma PRIM, karena graph direpresentasikan sebagai
#      adjacency dictionary yang efisien diproses secara node-by-node.
#      Prim juga lebih intuitif untuk graph yang dibangun bertahap.
#
# 3. Edge mana saja yang dipilih dalam MST?
#    → RouterA ↔ RouterC (biaya 2)
#    → RouterC ↔ RouterD (biaya 1)
#    → RouterA ↔ RouterB (biaya 3)
#    Total: 3 edge untuk 4 router (n-1 = 4-1 = 3) ✓
#
# 4. Berapa total bobot MST?
#    → Total = 2 + 1 + 3 = 6
#
# 5. Mengapa edge tertentu tidak dipilih?
#    → RouterB ↔ RouterD (biaya 5): Tidak dipilih karena saat
#      diproses, RouterB dan RouterD sudah terhubung melalui
#      jalur RouterB → RouterA → RouterC → RouterD.
#      Menambahkannya akan membentuk cycle.
#    → RouterB ↔ RouterC (biaya 4): Tidak dipilih karena
#      RouterB dan RouterC sudah terhubung via RouterA-RouterC.
#      Ini juga akan membentuk cycle jika dipaksakan.
#    Kesimpulan: edge dengan bobot lebih besar yang redundan
#    selalu diabaikan demi mempertahankan struktur tree tanpa cycle.
# ==========================================================

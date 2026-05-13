# Nama  : Rifqi Tazakka Putra
# NIM   : J0403251158
# Kelas : TPL-B1
# Praktikum 13 - Graph III: Spanning Tree
# File  : praktikum13.latihan4.py
# Latihan 4: Studi Kasus - Jaringan Kabel Antar Gedung

# ==========================================================
# LATIHAN 4 - Studi Kasus: Jaringan Kabel Antar Gedung
# ==========================================================
# Deskripsi Kasus:
# Sebuah kampus ingin membangun jaringan kabel internet antar
# gedung dengan total biaya MINIMUM. Setiap hubungan memiliki
# biaya pemasangan kabel yang berbeda.
#
# Data hubungan antar gedung:
#   GedungA - GedungB = 4 (juta rupiah)
#   GedungA - GedungC = 2
#   GedungB - GedungD = 3
#   GedungC - GedungD = 1
#   GedungA - GedungD = 5
#
# Algoritma yang digunakan: KRUSKAL
# Alasan: Data berbentuk edge list, cocok untuk Kruskal.
# ==========================================================

import heapq  # Untuk implementasi Prim (digunakan sebagai pembanding)

# -------------------------------------------------------
# Representasi weighted graph sebagai adjacency dictionary
# -------------------------------------------------------
graph = {
    'GedungA': {'GedungB': 4, 'GedungC': 2, 'GedungD': 5},
    'GedungB': {'GedungA': 4, 'GedungD': 3},
    'GedungC': {'GedungA': 2, 'GedungD': 1},
    'GedungD': {'GedungA': 5, 'GedungB': 3, 'GedungC': 1}
}

# Representasi sebagai edge list untuk Kruskal
# Format: (biaya, gedung1, gedung2)
edges = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
]

# -------------------------------------------------------
# Implementasi Algoritma Kruskal
# -------------------------------------------------------
def kruskal(edges):
    """
    Mencari MST menggunakan algoritma Kruskal.
    Strategi: pilih edge berbiaya terkecil yang tidak membentuk cycle.
    """
    # Urutkan edge dari biaya terkecil ke terbesar
    sorted_edges = sorted(edges)

    mst = []            # Edge yang terpilih dalam MST
    total_cost = 0      # Total biaya kabel
    connected = set()   # Node yang sudah terhubung

    print("Urutan edge setelah diurutkan berdasarkan biaya:")
    for cost, u, v in sorted_edges:
        print(f"  Biaya {cost}: {u} ↔ {v}")

    print("\nProses pemilihan kabel:")

    for cost, u, v in sorted_edges:
        # Pilih edge jika tidak membentuk cycle sederhana
        if u not in connected or v not in connected:
            mst.append((u, v, cost))
            total_cost += cost
            connected.add(u)
            connected.add(v)
            print(f"  ✓ PASANG kabel {u} ↔ {v}  biaya: {cost} juta")
        else:
            print(f"  ✗ SKIP  kabel {u} ↔ {v}  biaya: {cost} juta (tidak diperlukan)")

    return mst, total_cost


# -------------------------------------------------------
# Jalankan program dan tampilkan hasil
# -------------------------------------------------------
print("=" * 60)
print("  LATIHAN 4 - Jaringan Kabel Antar Gedung (Kruskal)")
print("=" * 60)
print("\nData hubungan antar gedung:")
for cost, u, v in edges:
    print(f"  {u} ↔ {v}  biaya: {cost} juta rupiah")
print()

mst, total = kruskal(edges)

print("\n" + "=" * 60)
print("HASIL: Jaringan kabel dengan biaya minimum:")
print("=" * 60)
for i, edge in enumerate(mst, 1):
    print(f"  {i}. Pasang kabel: {edge[0]} ↔ {edge[1]}  biaya: {edge[2]} juta")
print(f"\nTotal biaya minimum pemasangan kabel = {total} juta rupiah")
print(f"Jumlah kabel yang dipasang           = {len(mst)} kabel")
print("=" * 60)

# ==========================================================
# Jawaban Analisis:
#
# 1. Algoritma apa yang digunakan?
#    → Algoritma KRUSKAL, karena data tersedia dalam bentuk
#      edge list yang mudah diurutkan. Kruskal efisien untuk
#      kasus dengan jumlah edge yang tidak terlalu banyak (sparse).
#
# 2. Edge mana saja yang dipilih?
#    → GedungC ↔ GedungD (biaya 1 juta)
#    → GedungA ↔ GedungC (biaya 2 juta)
#    → GedungB ↔ GedungD (biaya 3 juta)
#
# 3. Berapa total biaya minimum?
#    → Total = 1 + 2 + 3 = 6 juta rupiah
#      (jauh lebih hemat dibanding pasang semua kabel = 15 juta)
#
# 4. Mengapa MST cocok digunakan pada kasus ini?
#    → Karena tujuannya adalah menghubungkan SEMUA gedung (node)
#      dengan biaya MINIMUM tanpa jalur redundan (cycle).
#      MST menjamin semua gedung terhubung dengan total panjang/biaya
#      kabel sekecil mungkin. Persis sesuai kebutuhan kampus ini.
#      Jika ada cycle, berarti ada kabel yang dipasang sia-sia
#      karena koneksi antar gedung sudah bisa dicapai lewat jalur lain.
# ==========================================================

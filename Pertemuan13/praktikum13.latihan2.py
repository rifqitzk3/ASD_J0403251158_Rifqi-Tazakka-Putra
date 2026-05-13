# Nama  : Rifqi Tazakka Putra
# NIM   : J0403251158
# Kelas : TPL-B1
# Praktikum 13 - Graph III: Spanning Tree
# File  : praktikum13.latihan2.py
# Latihan 2: Implementasi Algoritma Kruskal

# ==========================================================
# LATIHAN 2 - Implementasi Algoritma Kruskal
# ==========================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
# Kruskal selalu mulai dari edge dengan bobot TERKECIL (greedy)
edges.sort()

mst = []           # Menyimpan edge hasil MST
total_weight = 0   # Total bobot MST

# Set sederhana untuk node yang sudah dipilih/masuk ke MST
connected = set()

print("=" * 50)
print("  LATIHAN 2 - Algoritma Kruskal")
print("=" * 50)
print("\nEdge setelah diurutkan (bobot terkecil ke terbesar):")
for w, u, v in edges:
    print(f"  bobot {w}: {u} -- {v}")

print("\nProses pemilihan edge oleh Kruskal:")

for weight, u, v in edges:
    # Memilih edge yang tidak membentuk cycle sederhana
    # Edge aman jika minimal satu node-nya belum masuk MST
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)
        print(f"  ✓ PILIH {u}-{v} bobot={weight} | Node terhubung: {connected}")
    else:
        print(f"  ✗ LEWATI {u}-{v} bobot={weight} | Kedua node sudah terhubung (cycle!)")

print("\n" + "=" * 50)
print("Minimum Spanning Tree:")
for edge in mst:
    print(f"  {edge[0]} -- {edge[1]}  bobot: {edge[2]}")
print(f"\nTotal bobot = {total_weight}")
print("=" * 50)

# ==========================================================
# Jawaban Analisis:
#
# 1. Edge mana yang dipilih pertama kali?
#    → Edge C-D dengan bobot 1 dipilih pertama karena memiliki
#      bobot terkecil dari semua edge yang ada.
#
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
#    → Kruskal menggunakan pendekatan greedy: selalu memilih
#      pilihan terbaik (bobot terkecil) saat itu. Dengan memilih
#      edge terkecil lebih dulu, total bobot MST dijamin minimum.
#      Ini adalah inti dari algoritma greedy pada MST.
#
# 3. Berapa total bobot MST yang dihasilkan?
#    → Total bobot = 1 + 2 + 3 = 6
#      Edge yang dipilih: C-D(1), A-C(2), B-D(3)
#
# 4. Mengapa edge tertentu tidak dipilih?
#    → Edge A-B (bobot 4) dan A-D (bobot 5) tidak dipilih karena
#      pada saat diproses, kedua node dari edge tersebut sudah
#      terhubung di dalam MST. Jika tetap dipilih, akan terbentuk
#      cycle yang melanggar syarat spanning tree.
# ==========================================================

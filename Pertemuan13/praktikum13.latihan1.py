# Nama  : Rifqi Tazakka Putra
# NIM   : J0403251158
# Kelas : TPL-B1
# Praktikum 13 - Graph III: Spanning Tree
# File  : praktikum13.latihan1.py
# Latihan 1: Memahami Konsep Spanning Tree

# ==========================================================
# LATIHAN 1 - Memahami Konsep Spanning Tree
# ==========================================================
# Edge pada graph: A-B, A-C, A-D, C-D, B-D
# Graph ini memiliki cycle, contohnya: A → C → D → A
# ==========================================================

# Daftar edge pada graph awal (unweighted/tanpa bobot)
edges = [
    ('A', 'B'),  # A terhubung ke B
    ('A', 'C'),  # A terhubung ke C
    ('A', 'D'),  # A terhubung ke D (membentuk cycle dengan A-C-D)
    ('C', 'D'),  # C terhubung ke D
    ('B', 'D')   # B terhubung ke D
]

# Contoh spanning tree yang valid dari graph di atas
# Spanning tree memilih edge yang menghubungkan semua node TANPA cycle
# Dengan 4 node (A, B, C, D), spanning tree harus punya tepat 3 edge (4-1=3)
spanning_tree = [
    ('A', 'C'),  # Menghubungkan A ke C
    ('C', 'D'),  # Menghubungkan C ke D
    ('D', 'B')   # Menghubungkan D ke B
]

# Tampilkan semua edge pada graph
print("=" * 45)
print("  LATIHAN 1 - Konsep Spanning Tree")
print("=" * 45)

print("\nEdge pada graph awal:")
for edge in edges:
    print(f"  {edge[0]} -- {edge[1]}")

# Tampilkan spanning tree yang valid
print("\nContoh Spanning Tree yang valid:")
for edge in spanning_tree:
    print(f"  {edge[0]} -- {edge[1]}")

# Tampilkan jumlah edge
print(f"\nJumlah edge graph awal    = {len(edges)}")
print(f"Jumlah edge spanning tree = {len(spanning_tree)}")
print(f"Jumlah node               = 4")
print(f"Rumus: edge spanning tree = node - 1 = 4 - 1 = 3 ✓")

# Verifikasi: spanning tree valid jika jumlah edge = jumlah node - 1
nodes = {'A', 'B', 'C', 'D'}
if len(spanning_tree) == len(nodes) - 1:
    print("\n✓ Spanning tree VALID: jumlah edge = jumlah node - 1")
else:
    print("\n✗ Spanning tree TIDAK valid")

print("=" * 45)

# ==========================================================
# Jawaban Analisis:
#
# 1. Apa perbedaan graph awal dan spanning tree?
#    - Graph awal memiliki 5 edge dan mengandung cycle
#      (contoh cycle: A → C → D → A, atau A → D → B → ... )
#    - Spanning tree hanya memiliki 3 edge (node-1), tidak ada cycle,
#      namun tetap menghubungkan semua node (A, B, C, D)
#    - Graph awal adalah "superset" dari spanning tree
#
# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#    - Cycle berarti ada jalur lebih dari satu antara dua node
#    - Ini menyebabkan edge yang redundant (tidak diperlukan)
#    - Dalam konteks nyata (misalnya kabel jaringan), cycle berarti
#      pemborosan biaya karena ada kabel yang tidak perlu dipasang
#    - Tujuan spanning tree adalah menghubungkan semua node
#      dengan jumlah edge MINIMUM, cycle melanggar tujuan ini
#
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#    - Spanning tree hanya membutuhkan tepat (n-1) edge untuk
#      menghubungkan n node tanpa cycle
#    - Graph awal bisa memiliki lebih banyak edge karena ada
#      multiple path antar node
#    - Setiap edge tambahan melebihi (n-1) pasti membentuk cycle
# ==========================================================

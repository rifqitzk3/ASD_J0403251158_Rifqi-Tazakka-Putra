# Nama  : Rifqi Tazakka Putra
# NIM   : J0403251158
# Kelas : TPL-B1
# Praktikum 13 - Graph III: Spanning Tree
# File  : praktikum13.materi1.py
# Materi: Implementasi Algoritma Kruskal

# ==========================================================
# MATERI 1 - Implementasi Algoritma Kruskal
# ==========================================================
# Algoritma Kruskal membangun MST dengan cara:
# 1. Mengurutkan semua edge dari bobot terkecil ke terbesar
# 2. Memilih edge satu per satu dari yang terkecil
# 3. Edge hanya ditambahkan jika tidak membentuk cycle
# 4. Proses berhenti ketika semua node sudah terhubung
# ==========================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil (greedy approach)
edges.sort()

mst = []           # List untuk menyimpan edge yang terpilih dalam MST
total_weight = 0   # Akumulator total bobot MST

# Set sederhana untuk melacak node yang sudah masuk ke MST
connected = set()

print("=" * 50)
print("  ALGORITMA KRUSKAL - Minimum Spanning Tree")
print("=" * 50)
print("\nUrutan edge setelah diurutkan berdasarkan bobot:")
for w, u, v in edges:
    print(f"  {u} -- {v}  bobot: {w}")

print("\nProses pemilihan edge:")

for weight, u, v in edges:
    # Cek apakah edge ini membentuk cycle sederhana:
    # Edge aman jika salah satu node-nya belum ada di MST
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)
        print(f"  ✓ Pilih edge {u}-{v} (bobot {weight}) → DITAMBAHKAN ke MST")
    else:
        # Kedua node sudah terhubung → akan membentuk cycle → diabaikan
        print(f"  ✗ Lewati edge {u}-{v} (bobot {weight}) → membentuk cycle, DIABAIKAN")

print("\n" + "=" * 50)
print("Hasil Minimum Spanning Tree (Kruskal):")
print("=" * 50)
for edge in mst:
    print(f"  {edge[0]} -- {edge[1]}  bobot: {edge[2]}")
print(f"\nTotal bobot MST = {total_weight}")
print("=" * 50)

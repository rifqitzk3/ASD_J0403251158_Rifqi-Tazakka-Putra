# =================================================
# Nama : Rifqi Tazakka Putra
# NIM  : J0403251158
# =================================================
# Latihan 6 : Rotasi Kanan pada BST Tidak Seimbang
# =================================================

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan nilai Node
        self.left = None # Child Kiri
        self.right = None # Child Kanan

# Fungsi preorder untuk melihat bentuk tree
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

# Fungsi sederhana untuk menampilkan struktur tree
def tampil_struktur(root, level = 0, posisi="root"):
    if root is not None:
        print("     " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")

# Fungsi rotasi kiri
def rotate_right(y):
    # x adalah root lama
    x = y.left       # x adalah child kanan y
    T2 = x.right     # subtree kiri milik x disimpan sementara

    # proses rotasi
    x.right = y      # y menjadi child kiri dari x
    y.left = T2    # child kanan y diganti dengan T2

    # x menjadi root baru
    return x

# Main program

# Membuat tree yang tidak seimbang:
# 30 -> 20 -> 10
root = Node(30)
root.left = Node(20)
root.left.left = Node(10)

print("Preorder sebelum rotasi kanan: ")
preorder(root)

print("\n\nStruktur sebelum rotasi kanan: ")
tampil_struktur(root)

# Melakukan rotasi kanan pada root
root = rotate_right(root)

print("Preorder sesudah rotasi kanan: ")
preorder(root)

print("\n\nStuktur sesudah rotasi kanan: ")
tampil_struktur(root)
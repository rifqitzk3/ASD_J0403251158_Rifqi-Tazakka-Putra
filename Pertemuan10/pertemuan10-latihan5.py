# ================================================
# Nama : Rifqi Tazakka Putra
# NIM  : J0403251158
# ================================================
# Latihan 5 : Rotasi Kiri pada BST Tidak Seimbang
# ================================================

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


def tampil_struktur(root, level = 0, posisi="root"):
    if root is not None:
        print("     " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")

# Fungsi rotasi kiri
def rotate_left(x):
    # x adalah root lama
    y = x.right     # y adalah child kanan x
    T2 = y.left     # subtree kiri milik y disimpan sementara

    # proses rotasi
    y.left = x      # x menjadi child kiri dari y
    x.right = T2    # child kanan x diganti dengan T2

    # y menjadi root baru
    return y

# Main program

# Membuat tree yang tidak seimbang:
# 10 -> 20 -> 30
root = Node(10)
root.right = Node(20)
root.right.right = Node(30)

print("Preorder sebelum rotasi kiri: ")
preorder(root)

print("\n\nStruktur sebelum rotasi kiri: ")
tampil_struktur(root)

#melakukan rotasi kiri pada root
root = rotate_left(root)

print("Preorder sesudah rotasi kiri: ")
preorder(root)

print("\n\nStuktur sesudah rotasi kiri: ")
tampil_struktur(root)
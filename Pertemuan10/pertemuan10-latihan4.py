class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    return root

def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print(" " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")

# Program utama
root = None
data_list = [10, 20, 30]

for data in data_list:
    root = insert(root, data)

print("Preorder BST:")
preorder(root)

print("\n\nStruktur BST:")
tampil_struktur(root)

'''
Penjelasan :
Pada latihan kali ini, dibuat salah satu struktur data yaitu Binary Search Tree (BST) yang dimana setiap node memiliki aturan 
bahwa nilai di sebelah kiri lebih kecil dari root dan nilai di sebelah kanan lebih besar dari root.

Program dimulai dengan pembuatan class Node yang digunakan untuk menyimpan data serta memiliki dua child yaitu left dan right.

Kemudian terdapat fungsi insert yang digunakan untuk memasukkan data ke dalam tree sesuai aturan BST. 
Jika root masih kosong maka akan dibuat node baru, jika tidak maka data akan dibandingkan dengan root, 
jika lebih kecil akan masuk ke kiri, jika lebih besar akan masuk ke kanan secara rekursif.

Selanjutnya terdapat fungsi preorder yang digunakan untuk menampilkan isi tree dengan metode preorder 
yaitu root -> left -> right.

Lalu terdapat fungsi tampil_struktur yang digunakan untuk menampilkan struktur tree secara visual berdasarkan level, 
dimana root berada di level paling atas, lalu child kiri (L) dan child kanan (R) ditampilkan bertingkat sesuai kedalamannya.

Pada program utama, dibuat list data yaitu [10, 20, 30] yang kemudian dimasukkan ke dalam BST menggunakan fungsi insert.

Berikut visualisasi nya:
10 -> 20 -> 30
'''
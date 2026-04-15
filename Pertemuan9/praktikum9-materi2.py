########################################
# Latihan 2 : Membuat Node
########################################

# Class Node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan nilai Node
        self.left = None # Child Kiri
        self.right = None # Child Kanan
    

# Membuat Root
root = Node("A")

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

# Level 2
root.left.left = Node ("D")
root.left.right = Node ("E")

# Menampilkan isi Tree
print("Data pada Root : ", root.data)
print("Data pada Child Kiri Root : ", root.left.data)
print("Data pada Child Kanan Root : ", root.right.data)
print("Data pada Child Kiri 'B' : ", root.left.left.data)
print("Data pada Child Kanan 'B' : ", root.left.right.data)

'''
Penjelasan : Pada latihan ini, kita mulai membangun struktur tree secara manual dengan menambahkan node-node ke root.
Setelah root "A" dibuat, ditambahkan dua child di level 1 yaitu "B" di kiri dan "C" di kanan.
Lalu di level 2, node "B" punya dua child lagi yaitu "D" di kiri dan "E" di kanan, sementara "C" tidak punya child (jadi dia adalah leaf node).
Cara mengaksesnya pakai chaining titik seperti root.left.left untuk sampai ke node "D".
'''
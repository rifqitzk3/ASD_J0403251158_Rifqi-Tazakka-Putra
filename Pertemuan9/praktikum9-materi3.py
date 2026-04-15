########################################
# Latihan 3 : Membuat Node
########################################

# Class Node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan nilai Node
        self.left = None # Child Kiri
        self.right = None # Child Kanan
    
def preorder(node):
    if node is not None:
        print(node.data, end=" -> ")
        preorder(node.left)
        preorder(node.right)


# Membuat sebuah node root
root = Node("A")

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# Menjalankan traversal preorder
print("Hasil Traversal Preorder: ")
preorder(root)

'''
Penjelasan : Pada latihan ini diperkenalkan salah satu cara menelusuri (traversal) tree yaitu Preorder.
Urutan Preorder adalah Root -> Left -> Right, artinya setiap kali mengunjungi node, yang pertama dicetak adalah node itu sendiri, 
baru kemudian rekursif ke child kiri, lalu child kanan.
Hasilnya: A -> B -> D -> E -> C, karena mulai dari root A, lalu turun ke kiri (B), terus ke kiri lagi (D), 
balik ke E, baru pindah ke cabang kanan (C).
'''
########################################
# Latihan 4 : Membuat Node
########################################

# Class Node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan nilai Node
        self.left = None # Child Kiri
        self.right = None # Child Kanan
    
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" -> ")
        inorder(node.right)


# Membuat sebuah node root
root = Node("A")

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# Menjalankan traversal Inorder
print("Hasil Traversal Inorder: ")
inorder(root)

'''
Penjelasan : Pada latihan ini diperkenalkan cara traversal Inorder.
Urutan Inorder adalah Left -> Root -> Right, artinya sebelum mencetak sebuah node, 
program akan terus turun ke child kiri sampai habis, baru cetak nodenya, lalu ke child kanan.
Hasilnya: D -> B -> E -> A -> C, urutan ini menarik karena pada Binary Search Tree (BST), 
Inorder akan menghasilkan data yang terurut dari kecil ke besar.
'''
########################################
# Latihan 5 : Membuat Node
########################################

# Class Node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan nilai Node
        self.left = None # Child Kiri
        self.right = None # Child Kanan
    
def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" -> ")
        


# Membuat sebuah node root
root = Node("A")

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# Menjalankan traversal Postorder
print("Hasil Traversal Postorder: ")
postorder(root)

'''
Penjelasan : Pada latihan ini diperkenalkan cara traversal Postorder.
Urutan Postorder adalah Left -> Right -> Root, kebalikan dari Preorder. 
Artinya sebuah node baru dicetak setelah kedua child-nya (kiri dan kanan) sudah selesai dikunjungi semua.
Hasilnya: D -> E -> B -> C -> A, root "A" selalu dicetak paling terakhir karena ia baru diproses 
setelah semua subtree di bawahnya selesai. Postorder sering dipakai misalnya saat ingin menghapus tree, 
karena child-child dihapus dulu sebelum parent-nya.
'''


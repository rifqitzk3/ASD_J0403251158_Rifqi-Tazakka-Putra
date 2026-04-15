########################################
# Latihan 6 : Membuat Node
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
        
# Membuat Root
root = Node("Direktur")

# Membuat child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

# Level 2
root.left.left = Node ("Staff 1")
root.left.right = Node ("Staff 2")

root.right.right = Node("Staff 3")

# Menampilkan isi Tree
print("Struktur Organisasi (Preorder): ")
preorder(root)


'''
Penjelasan :
Pada latihan kali ini, dibuat salah satu struktur data yaitu tree yang dimana memiliki cara pengurutan yang berbeda-beda 
dan disini dipakai cara pengurutan preorder, cara pengurutannya adalah root -> left -> right.

Direktur sebagai root, lalu dibawah sebelah kiri ada Manajer A sebagai child level 1 yang memiliki child level 2 Staff 1 dan Staff 2
Lalu ada Manajer B sebagai child level 1 di bawah root sebelah kanan, yang memiliki child level 2 staff 3.

Berikut visualisasi nya:
Direktur -> Manajer A -> Staff 1 -> Staff 2 -> Manajer B -> Staff 3 
'''




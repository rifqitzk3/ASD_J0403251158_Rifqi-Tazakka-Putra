# =============================================
# Nama : Rifqi Tazakka Putra
# NIM  : J0403251158
# =============================================
# Latihan : BST (Binary Search Tree)
# =============================================


class Node:
    def __init__(self, data):
        self.data = data # Menyimpan nilai Node
        self.left = None # Child Kiri
        self.right = None # Child Kanan
        
def insert(root, data):    
    if root is None:
        return Node(data)
    
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    
    return root

# Mengisi data pada BST yang udah kita buat

root = None
data_list = [50,30,70,20,40,50,80]

for data in data_list:
    root = insert(root,data)
    
print("BST Berhasil Dibuat!")


# =============================================
# Latihan : Tranversal Inorder
# =============================================

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

print("Hasil Inorder : ")
inorder(root)


# =============================================
# Latihan : Search di BST
# =============================================
def search(root, key):
    if root is None:
        return False
    
    if root.data == key:
        return True
    elif key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)
    
# Uji Pencarian 
key = 40

if search(root, key):
    print("Data ditemukan!")
else:
    print("Data tidak ditemukan!")
    
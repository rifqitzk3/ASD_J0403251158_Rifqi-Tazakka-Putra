########################################
# Latihan 1 : Membuat Node
########################################

# Class Node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan nilai Node
        self.left = None # Child Kiri
        self.right = None # Child Kanan
    

# Membuat Root
root = Node("A")

# Menampilkan isi Root
print("Data pada Root : ", root.data)

'''
Penjelasan : Tree merupakan salah satu dari banyaknya struktur data, struktur data ini berbentuk seperti akar pohon yang memiliki cabang-cabangnya.
Karena struktur data ini tidak ada pada bawaan python, jadi untuk mengimplementasikannya pada python kita butuh cetakannya dulu alias Class.
Nah pada class ini baru lah dibuat strukturnya, yaitu ada root (akar), dan cabang cabangnya di sebelah kiri dan kanan pada tiap cabang.
'''

# =============================================
# Nama : Rifqi Tazakka Putra
# NIM  : J0403251158
# =============================================


# =============================================
# Implementasi Dasar :  Node pada Linked List
# =============================================

# Membuat class Node (merupakan unit dasar dari Linked List)
class Node:
    def __init__(self, data): # Konstruktor = Fungsi dalam class yang pasti dijalankan otomatis ketika objek mengakses class ini
        self.data = data # Buat nyimpen nilai
        self.next = None # Pointer buat nunjuk ke node selanjutnya 

# 1. Membuat node satu per satu 
nodeA = Node("A") 
nodeB = Node("B")
nodeC = Node("C")

# 2. Menghubungkan Node : A -> B -> C -> None
nodeA.next = nodeB
nodeB.next = nodeC

# 3. Menentukan head atau node pertama nya
head = nodeA

# 4. Traversal : Menelusuri dari head sampai None
current = head
while current is not None:
    print(current.data, end=' -> ')
    current = current.next
    

# =================================================
# Implementasi Dasar : Linked List + Insert Awal
# =================================================

class LinkedList: # Bisa juga jadi Class implementasi stack
    def __init__(self):
        print("\n\n======== List Baru =========") # Misahin list yang manual yg diatas (sblmnya) sama yg sekarang 
        self.head = None # Awalnya kosong
        
    def insertAwal(self, data): # Push dalam stack
        # 1) Buat node baru
        nodeBaru = Node(data) # Manggil class Node
        
        # 2) Node baru menunjuk ke head
        nodeBaru.next = self.head    
        
        # 3) head pindah ke node baru
        self.head = nodeBaru
    
    def hapusAwal(self): # Kalau dalam stack ini namanya Pop
        dataTerhapus = self.head.data # Peek dalam Stack
        # Menggeser head nya (Jadi head yang sekarang adalah Node selanjutnya dari Head sebelumnya)
        self.head = self.head.next
        print(f"\nData {dataTerhapus} dihapus.")
        
    def tampilkan(self):
        current = self.head
        while current is not None:
            print(current.data, end=' -> ')
            current = current.next
    
ll = LinkedList() # Instantiasi objek ke class Linked List

ll.insertAwal("X")
ll.insertAwal("Y")
ll.insertAwal("Z")

ll.tampilkan()

ll.hapusAwal()

ll.tampilkan()            
                
    








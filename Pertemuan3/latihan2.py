# ==========================================================
# IMPLEMENTASI SINGLE CIRCULAR LINKED LIST
# Latihan 2: Pencarian pada node tertentu
# ==========================================================

# Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Circular Linked List
class CircularLinkedList:
    def __init__(self):
        self.head = None


    # Insert di akhir (circular)
    def insert_at_end(self, data):
        new_node = Node(data)

        # Jika list kosong
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head


    # Display (biar bisa lihat isinya)
    def display(self):
        if not self.head:
            print("Circular Linked List kosong.")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(kembali ke head)")


    # ===================
    # FUNGSI SEARCH
    # ===================
    
    def search(self, key):

        if not self.head:
            print("Circular Linked List kosong. Tidak ada elemen yang bisa dicari.")
            return

        temp = self.head

        while True:
            if temp.data == key:
                print(f"Elemen {key} ditemukan dalam Circular Linked List.")
                return

            temp = temp.next
            if temp == self.head:
                break

        print(f"Elemen {key} tidak ditemukan dalam Circular Linked List.")
        

# ========
# Mainns
# ========

cll = CircularLinkedList()

# Input elemen
data_input = input("Masukkan elemen (pisahkan dengan koma): ")

if data_input.strip() != "":
    numbers = list(map(int, data_input.split(",")))
    for num in numbers:
        cll.insert_at_end(num)

print("\nIsi Circular Linked List:")
cll.display()

# Input pencarian
cari = int(input("\nMasukkan elemen yang ingin dicari: "))
cll.search(cari)

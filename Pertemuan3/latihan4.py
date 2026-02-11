# ==========================================================
# IMPLEMENTASI PENGGABUNGAN DUA SINGLE LINKED LIST
# Latihan 4: Menggabungkan dua Single Linked List
# ==========================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    # ===================
    # FUNGSI MERGE
    # ===================
    
    def merge(self, other):
        if not self.head:
            self.head = other.head
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = other.head


# =======
# Mainns
# =======

ll1 = LinkedList()
ll2 = LinkedList()

# Input Linked List 1
data1 = input("Masukkan elemen untuk Linked List 1 (pisahkan koma): ")
if data1.strip() != "":
    for num in map(int, data1.split(",")):
        ll1.insert_at_end(num)

# Input Linked List 2
data2 = input("Masukkan elemen untuk Linked List 2 (pisahkan koma): ")
if data2.strip() != "":
    for num in map(int, data2.split(",")):
        ll2.insert_at_end(num)

print("\nLinked List 1:")
ll1.display()

print("Linked List 2:")
ll2.display()

# Gabungin
ll1.merge(ll2)

print("Linked List setelah digabungkan:")
ll1.display()

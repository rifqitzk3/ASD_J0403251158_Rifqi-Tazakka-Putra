# ==========================================================
# IMPLEMENTASI SINGLE LINKED LIST 
# Latihan 1: Menghapus node berdasarkan nilai tertentu 
# ==========================================================

# Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedList
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
        print("None")

    # ===================
    # FUNGSI DELETE
    # ===================

    def delete_node(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Nilai tidak ditemukan.")
            return

        prev.next = temp.next
        print(f"Node dengan nilai {key} berhasil dihapus.")

# ======
# Mainns
# ======

ll = LinkedList()

# Input data dari user
data_input = input("Masukkan data ke dalam linked list (pisahkan dengan koma): ")

if data_input.strip() != "":
    numbers = [int(x.strip()) for x in data_input.split(",")]
    for num in numbers:
        ll.insert_at_end(num)

print("\nLinked List awal:")
ll.display()

hapus = int(input("Masukkan nilai yang ingin dihapus: "))
ll.delete_node(hapus)

print("\nLinked List setelah penghapusan:")
ll.display()

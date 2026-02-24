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

# Queue dengan 2 pointer : front dan rear
class QueueLL:
    def __init__(self):
        self.front = None # Node paling depan
        self.rear = None # Node paling belakang
    
    def is_empty(self):
        return self.front is None
    
    def enqueue(self, data):
        # Menambah data di belakang
        nodeBaru = Node(data)    
        
        # Jika queue kosong, fornt dan rear akan menunjuk ke node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        
        # Jika queue tidak kosong:
        # Rear lama menunjuk ke node baru
        self.rear.next = nodeBaru
        
        # Rear pindah ke node baru
        self.rear = nodeBaru
    
    def dequeue(self):
        # Menghapus data dari depan
        
        # 1) Lihat data yang paling depan
        dataTerhapus = self.front.data
        
        # 2) Geser front ke node berikutnya
        self.front = self.front.next

        # 3) Jika setelah geser front menjadi none, maka queue kosong
        # Rear juga harus jadi none
        if self.front is None:
            self.rear = None
        return dataTerhapus
    
    def tampilkan(self):
        # Menampilkan isi queue dari front ke rear
        current = self.front
        print("Front", end=' -> ')
        while current is not None:
            print(current.data, end=' -> ')
            current = current.next     
        print("Rear")
        
q = QueueLL()

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

q.tampilkan()

q.dequeue()
q.tampilkan()
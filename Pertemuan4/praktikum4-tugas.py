# =============================================
# Nama : Rifqi Tazakka Putra
# NIM  : J0403251158
# =============================================

# ========================================================== 
# Tugas Hands-On: Sistem Antrian Bengkel Motor 
# ========================================================== 
 
class Node: 
    def __init__(self, no, nama, servis): 
        self.no = no 
        self.nama = nama 
        self.servis = servis 
        self.next = None 
 
 
class QueueBengkel: 
    def __init__(self): 
        self.front = None 
        self.rear = None 
 
    def isEmpty(self):
        # Ketika queue kosong maka front = rear = None
        return self.front is None
    
    def enqueue(self, no, nama, servis):
        nodeBaru = Node(no, nama, servis)
        # Jika data baru masuk dan queue masih kosong, maka data baru menjadi front sekaligus rear
        if self.isEmpty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        
        # Jika queue tidak kosong, maka data baru diletakkan setelah rear kemudian dijadikan sebagai rear yang baru
        nodeBaru = Node(no, nama, servis)
        self.rear.next = nodeBaru
        self.rear = nodeBaru
    def dequeue(self):
        #Error handling
        if self.isEmpty():
            print("Antrian Kosong. Tidak ada Pelanggan yang dilayani")
            return None
            
        # Lihat/peek bagian front, simpan di variabel data yang akan dihapus(dilayani)
        nodeDilayani = self.front

        # Geser pointer front ke next front
        self.front = self.front.next

        # Jika front menjadi none (data antrian terakhir yang dilayani, maka front = rear = none)
        if self.front is None:
            self.rear = None
                
        return nodeDilayani
 
    def tampilkan(self): 

        print("Daftar Antrian Pelanggan (Front -> Rear) : ")
        current = self.front
        while current is not None:
            print(f"{current.no} - {current.nama} - {current.servis}")
            current = current.next    
 
  
def main(): 
    q = QueueBengkel() 
 
    while True: 
        print("\n=== Sistem Antrian Bengkel ===") 
        print("1. Tambah Pelanggan") 
        print("2. Layani Pelanggan") 
        print("3. Lihat Antrian") 
        print("4. Keluar") 
 
        pilih = input("Pilih menu: ") 
 
        if pilih == "1": 
            no = input("No Antrian : ") 
            nama = input("Nama      : ") 
            servis = input("Servis    : ") 
            q.enqueue(no, nama, servis) 
 
        elif pilih == "2": 
            dilayani = q.dequeue() 
            if dilayani:
                print(f"\nPelanggan dilayani : {dilayani.no} - {dilayani.nama} - {dilayani.servis}")
 
        elif pilih == "3": 
            q.tampilkan() 
 
        elif pilih == "4": 
            print("\nProgram Selesai. Terima kasih")
            break 
 
        else: 
            print("Pilihan tidak valid. Tolong input angka 1-4.") 
 
 
if __name__ == "__main__": 
    main() 
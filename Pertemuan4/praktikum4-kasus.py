# =============================================
# Nama : Rifqi Tazakka Putra
# NIM  : J0403251158
# =============================================

# ========================================================================================
# Studi Kasus : Sistem Antrian Layanan Akademik
# Implementasi Queue
# Perbedaan Queue dan Stack
# Enqueue : memindahkan pointer rear (entry queue/menambah data baru dari belakang) 
# Dequeue : memindahkan pointer front (delete queue/menghapus data dari depan)
# Stack => Front -> C -> B -> A -> None
# Queue => Front ->  A -> B -> C -> Rear
# =========================================================================================

# 1) Mendefinisikan Node (Unit dasar linked list)
class Node:
    def __init__(self, nim, nama):
        self.nim = nim           # Menyimpan NIM Mahasiswa
        self.nama = nama          # Menyimpan nama Mahasiswa
        self.next = None           # Pointer ke node berikutnya

# 2) Mendefinisikan queue, terdiri dari front dan rear
class queueAkademik:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        # Ketika queue kosong maka front = rear = None
        return self.front is None
    
    def enqueue(self, nim, nama):
        nodeBaru = Node(nim, nama)
        # Jika data baru masuk dan queue masih kosong, maka data baru menjadi front sekaligus rear
        if self.isEmpty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        
        # Jika queue tidak kosong, maka data baru diletakkan setelah rear kemudian dijadikan sebagai rear yang baru
        nodeBaru = Node(nim, nama)
        self.rear.next = nodeBaru
        self.rear = nodeBaru

        # Menghapus data (karena ini queue berarti yang dilayani yang paling awal masuk/front)
    def dequeue(self):
        #Error handling
        if self.isEmpty():
            print("Antrian Kosong. Tidak ada Mahasiswa yang dilayani")
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

        print("Daftar Antrian Mahasiswa (Front -> Rear) : ")
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. {current.nim} - {current.nama}")
            current = current.next  
            no += 1   
    

# Program Utama
def main():
    # Instantiasi queue
    q = queueAkademik()

    while True:
        print("\n======= Sistem Antrian Akademik =======")
        print("1. Tambahkan Mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Lihat Antrian Mahasiswa")
        print("4. Keluar")

        pilihan = input("Pilih Menu (1-4) : ").strip()

        if pilihan == "1":
            nim = input("\nMasukkan NIM : ")
            nama = input("Masukkan Nama : ")

            q.enqueue(nim,nama)
            print("\nMahasiswa Berhasil ditambahkan ke Antrian")
         
        elif pilihan == "2":
             dilayani = q.dequeue()
             if dilayani:
                print(f"\nMahasiswa dilayani : {dilayani.nim} - {dilayani.nama}")

        elif pilihan == "3":
             print()
             q.tampilkan()
        
        elif pilihan == "4":
             print("\nProgram Selesai. Terima kasih")
             break
        else:
             print("\nPilihan tidak valid. Silahkan masukkan angka 1-4")

if __name__ == "__main__": 
    main()


         

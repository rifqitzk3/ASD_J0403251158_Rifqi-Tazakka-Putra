# ======================================================
# Nama : Rifqi Tazakka Putra
# NIM  : J0403251158
# ======================================================
# Studi Kasus BFS (Jalur Terdekat Lokasi)
# ======================================================

from collections import deque 

# Sebuah graph digunakan untuk merepresentasikan hubungan antar lokasi sebagai berikut: 

graph = { 
'Rumah': ['Sekolah', 'Toko'], 
'Sekolah': ['Perpustakaan'], 
'Toko': ['Pasar'], 
'Perpustakaan': [], 
'Pasar': [] 
} 

# Graph tersebut menggambarkan jalur dari Rumah ke lokasi lain. 
# Gunakan algoritma BFS untuk menampilkan urutan kunjungan node dimulai dari Rumah.

def bfs(graph, start): 
    visited = set() 
    queue = deque([start]) 
    visited.add(start) 
    
    while queue: 
        node = queue.popleft() 
        print(node, end=" ") 
        
        for neighbor in graph[node]: 
            if neighbor not in visited: 
                visited.add(neighbor) 
                queue.append(neighbor) 
            
            
print("BFS dari Rumah:") 
bfs(graph, 'Rumah')


'''
Pertanyaan Analisis 
1. Node mana yang dikunjungi pertama?  
Jawab : Rumah

2. Mengapa BFS cocok untuk mencari jalur terdekat?  
Jawab : BFS cocok untuk mencari jalur terdekat karena cara kerjanya menelusuri graph secara melebar (level per level). 
Jadi, node yang paling dekat dari titik awal akan dikunjungi lebih dulu sebelum node yang lebih jauh. 

3. Apa perbedaan urutan BFS jika struktur graph diubah? 
Jawab : Perbedaannya terletak pada urutan node yang dikunjungi. Jika struktur graph diubah, 
misalnya urutan neighbor di dalam adjacency list diubah atau hubungan antar node berbeda, maka urutan BFS juga akan berubah. 

Contohnya, jika dari node "Rumah" urutan neighbor awalnya ['Sekolah', 'Toko'], maka BFS akan mengunjungi "Sekolah" dulu baru "Toko". 
Tetapi jika diubah menjadi ['Toko', 'Sekolah'], maka BFS akan mengunjungi "Toko" terlebih dahulu. 
Hal ini terjadi karena BFS menggunakan queue (FIFO), sehingga urutan node yang dimasukkan ke dalam queue akan mempengaruhi urutan hasil traversal

'''




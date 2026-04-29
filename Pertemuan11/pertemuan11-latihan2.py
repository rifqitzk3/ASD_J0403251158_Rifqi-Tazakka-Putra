# ======================================================
# Nama : Rifqi Tazakka Putra
# NIM  : J0403251158
# ======================================================
# Studi Kasus DFS (Eksplorasi Jalur)
# ======================================================

# Graph berikut merepresentasikan jalur eksplorasi: 

graph = { 
'A': ['B', 'C'], 
'B': ['D', 'E'], 
'C': ['F'], 
'D': [], 
'E': [], 
'F': [] 
} 

# Gunakan algoritma DFS untuk menelusuri graph mulai dari node A.

def dfs(graph, node, visited): 
    visited.add(node) 
    print(node, end=" ") 
    
    for neighbor in graph[node]: 
        if neighbor not in visited: 
            dfs(graph, neighbor, visited) 
    
visited = set() 

print("DFS dari A:") 
dfs(graph, 'A', visited) 

'''
Pertanyaan Analisis 
1. Mengapa DFS masuk ke node terdalam terlebih dahulu?  
Jawab: DFS masuk ke node terdalam terlebih dahulu karena cara kerjanya menggunakan konsep rekursi atau stack, 
di mana algoritma akan terus mengikuti satu jalur sampai tidak ada node baru yang bisa dikunjungi. 
Setelah mentok, baru kembali (backtracking) ke node sebelumnya untuk mencoba jalur lain.

2. Apa yang terjadi jika urutan neighbor diubah?  
Jawab : Jika urutan neighbor diubah, maka urutan traversal DFS juga akan berubah. 
Hal ini karena DFS selalu memilih tetangga pertama yang ada di dalam adjacency list untuk ditelusuri lebih dulu. 
Jadi, perubahan urutan neighbor akan mempengaruhi jalur yang diambil dan hasil akhir penelusuran.

3. Bandingkan hasil DFS dengan BFS pada graph yang sama.
Jawab : Perbedaannya adalah pada urutan kunjungan node. DFS akan menelusuri graph secara mendalam (depth), 
sehingga hasilnya mengikuti satu jalur sampai selesai baru pindah ke jalur lain, misalnya: A → B → D → E → C → F.  

Sedangkan BFS menelusuri graph secara melebar (level per level), sehingga semua node yang dekat dengan node awal akan dikunjungi terlebih dahulu, 
misalnya: A → B → C → D → E → F.  
Jadi, DFS fokus ke kedalaman jalur, sedangkan BFS fokus ke tingkat kedekatan node dari titik awal.

'''
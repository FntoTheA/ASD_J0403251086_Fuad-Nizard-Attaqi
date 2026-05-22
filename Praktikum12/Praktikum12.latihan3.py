# Nama : Fuad Nizard Attaqi
# NIM : J0403251086
# Kelas : A1
# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================
# Weighted graph dengan bobot negatif
graph = {
 'A': {'B': 5, 'C': 4},
 'B': {},
 'C': {'B': -2}
}
def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak dari start ke start adalah 0
    distances[start] = 0
    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):
        # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():
                # Jika jarak ke node saat ini sudah diketahui,
                # dan ditemukan jarak yang lebih kecil ke neighbor,
                # maka lakukan update jarak
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
    return distances

hasil = bellman_ford(graph, 'A')
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# Jawaban Analisis:
# 1. Berapa bobot langsung dari A ke B?
# Jawab: Bobot langsung dari A ke B adalah 5.
#
# 2. Berapa total bobot jalur A -> C -> B?
# Jawab: Total bobot jalur A -> C -> B adalah 2 (diperoleh dari 4 + (-2)).
#
# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
# Jawab: Jalur A -> C -> B, karena menghasilkan total jarak 2 yang lebih kecil dibanding jalur langsung A -> B yang bernilai 5.
#
# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
# Jawab: Karena Bellman-Ford menggunakan pendekatan relaksasi seluruh edge secara berulang sebanyak V-1 kali. 
# Berbeda dengan Dijkstra yang bersifat greedy dan menandai node "selesai" secara permanen setelah dikunjungi, 
# Bellman-Ford terus mengevaluasi dan memperbarui semua edge di setiap iterasinya sehingga perubahan jarak akibat 
# bobot negatif akan terhitung secara akurat.
#
# 5. Apa yang dimaksud dengan proses relaksasi edge?
# Jawab: Proses relaksasi edge adalah memeriksa apakah jarak sementara ke node tetangga (neighbor) dapat diperpendek 
# dengan melewati node saat ini ditambah bobot edge ke tetangga tersebut. Jika distances[node] + weight < distances[neighbor], 
# maka distances[neighbor] akan diperbarui dengan nilai yang lebih kecil tersebut.
#
# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
# Jawab:
# - Bobot Negatif: Bellman-Ford bisa menangani graph dengan bobot negatif dan mendeteksi siklus negatif (negative cycle), 
#   sedangkan Dijkstra tidak bisa menangani bobot negatif.
# - Pendekatan: Dijkstra menggunakan pendekatan Greedy (selalu memilih node dengan jarak terkecil berikutnya), 
#   sedangkan Bellman-Ford menggunakan pendekatan dynamic programming/relaksasi semua edge secara berulang.
# - Kecepatan: Dijkstra lebih cepat dengan kompleksitas O((V + E) log V), sedangkan Bellman-Ford lebih lambat dengan kompleksitas O(V * E).
# Nama : Fuad Nizard Attaqi
# NIM : J0403251086
# Kelas : A1

# ==========================================================
# Latihan 5: Studi Kasus dengan Program Shortest Path
# ==========================================================

import heapq
# Graph lokasi
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
 'Bogor': {'Jakarta': 5, 'Depok': 2},
 'Depok': {'Jakarta': 2, 'Bandung': 6},
 'Jakarta': {'Bandung': 7},
 'Bandung': {},
}
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances
hasil = dijkstra(graph, 'Bogor')
print("Jarak terpendek dari Bogor:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")

# Jawaban Analisis:
# 1. Node awal yang digunakan apa?
# Jawab: Node awal yang digunakan adalah Bogor.
#
# 2. Node mana yang memiliki jarak paling kecil dari node awal?
# Jawab: Node Depok memiliki jarak paling kecil dari node awal, yaitu 2 menit.
#
# 3. Node mana yang memiliki jarak paling besar dari node awal?
# Jawab: Node Bandung memiliki jarak paling besar dari node awal, yaitu 7 menit.
#
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
# Jawab: 
# Algoritma Dijkstra bekerja dengan cara:
# 1. Menginisialisasi jarak setiap node ke tak terhingga, kecuali node awal (Bogor) yang jaraknya 0.
# 2. Memasukkan node awal ke dalam priority queue.
# 3. Berulang kali mengambil node dengan jarak sementara terkecil dari priority queue.
# 4. Untuk setiap node yang diambil, dilakukan proses relaksasi ke node-node tetangganya, yaitu jika ditemukan jalur yang lebih pendek, maka jarak node tetangga diperbarui dan dimasukkan ke dalam priority queue.
# 5. Proses ini terus berlanjut hingga priority queue kosong.

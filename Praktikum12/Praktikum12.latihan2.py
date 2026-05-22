# Nama : Fuad Nizard Attaqi
# NIM : J0403251086
# Kelas : A1

# ==========================================================
# Latihan 2: Implementasi Dijkstra
# ==========================================================
import heapq
# Weighted graph dengan bobot positif
graph = {
 'A': {'B': 4, 'C': 2},
 'B': {'D': 5},
 'C': {'D': 1},
 'D': {}
}
def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak dari start ke start adalah 0
    distances[start] = 0
    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat,
        # maka proses dilewati
        if current_distance > distances[current_node]:
            continue
        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances

hasil = dijkstra(graph, 'A')
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# Jawaban Analisis:
# 1. Berapa jarak terpendek dari A ke B?
# Jawab: Jarak terpendek dari A ke B adalah 4.
#
# 2. Berapa jarak terpendek dari A ke C?
# Jawab: Jarak terpendek dari A ke C adalah 2.
#
# 3. Berapa jarak terpendek dari A ke D?
# Jawab: Jarak terpendek dari A ke D adalah 3 (melalui C).
#
# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
# Jawab: 
# - Melalui C: Jalur A -> C -> D = 2 + 1 = 3.
# - Melalui B: Jalur A -> B -> D = 4 + 5 = 9.
# Karena 3 < 9, maka jalur melalui C memiliki bobot/jarak yang lebih kecil.
#
# 5. Apa fungsi priority_queue dalam algoritma Dijkstra?
# Jawab: Priority queue berfungsi untuk selalu memilih dan memproses node dengan 
# jarak sementara terkecil secara efisien (O(log V)). Ini memastikan sifat greedy 
# dari Dijkstra berjalan optimal, mengeksplorasi jalur terpendek terlebih dahulu.
#
# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?
# Jawab: Dijkstra berasumsi bahwa ketika suatu node telah dikunjungi/selesai diproses, 
# jarak terpendek ke node tersebut sudah final dan tidak akan pernah berkurang lagi. 
# Adanya bobot negatif membatalkan asumsi ini karena bisa saja ada jalur memutar lain 
# (yang melewati edge negatif tersebut) yang menghasilkan total jarak lebih kecil, 
# namun tidak akan dideteksi oleh Dijkstra.

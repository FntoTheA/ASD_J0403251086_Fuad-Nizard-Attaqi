# Nama : Fuad Nizard Attaqi
# NIM : J0403251086
# Kelas : A1
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================
import heapq
# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
 'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
 'Perpustakaan': {'Lab': 3},
 'Kantin': {'Lab': 4, 'Aula': 7},
 'Lab': {'Aula': 1},
 'Aula': {}
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
hasil = dijkstra(graph, 'Gerbang')
print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")
    
# Jawaban Analisis:
# 1. Lokasi mana yang paling dekat dari Gerbang?
# Jawab: Lokasi yang paling dekat dari Gerbang adalah Kantin, dengan waktu tempuh 2 menit.
#
# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
# Jawab: Waktu tempuh terpendek dari Gerbang ke Aula adalah 7 menit.
# Jalur yang dilalui: Gerbang -> Kantin -> Lab -> Aula (2 + 4 + 1 = 7 menit).
#
# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
# Jawab: Tidak selalu. Sebagai contoh pada kasus ini:
# - Jalur langsung Kantin -> Aula membutuhkan waktu 7 menit.
# - Jalur tidak langsung Kantin -> Lab -> Aula membutuhkan waktu 4 + 1 = 5 menit.
# Di sini terlihat bahwa jalur memutar dengan jumlah edge lebih banyak justru lebih cepat (5 menit) dibandingkan jalur langsung (7 menit).
#
# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
# Jawab: Algoritma Dijkstra sangat cocok karena semua bobot edge pada graph lokasi kampus ini merepresentasikan waktu tempuh (menit) yang bernilai positif. 
# Dijkstra dirancang khusus untuk mencari lintasan terpendek pada graph yang tidak memiliki bobot edge negatif, sehingga dijamin akan menghasilkan solusi yang optimal dan efisien.

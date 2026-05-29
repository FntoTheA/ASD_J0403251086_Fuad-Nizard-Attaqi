#Nama   : Fuad Nizard Attaqi
#NIM    : J0403251086
#Kelas  : A/1
#Praktikum 13 - Graph III: Spanning Tree

edges = [
    (4, 'A', 'B'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (1, 'C', 'D'),
    (5, 'A', 'D')
]

edges.sort()

mst = []
total_weight = 0
connected = set()

for weight, u, v in edges:
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
print("Total bobot =", total_weight)

# Jawaban Analisis:
# 1. Algoritma apa yang digunakan?
#    Algoritma Kruskal.
# 2. Edge mana saja yang dipilih?
#    Edge (1, 'C', 'D'), (2, 'A', 'C'), (3, 'B', 'D').
# 3. Berapa total biaya minimum?
#    Total biaya minimum adalah 6 (1 + 2 + 3).
# 4. Mengapa MST cocok digunakan pada kasus ini?
#    Karena MST digunakan untuk mencari biaya minimum untuk menghubungkan semua node dalam graph.

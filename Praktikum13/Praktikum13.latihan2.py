#Nama   : Fuad Nizard Attaqi
#NIM    : J0403251086
#Kelas  : A/1
#Praktikum 13 - Graph III: Spanning Tree

edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
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
# 1. Edge mana yang dipilih pertama kali?
#    Edge dengan bobot paling kecil yaitu (1, 'C', 'D') dipilih pertama kali.
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
#    Karena menggunakan algoritma Kruskal yang mengurutkan edge berdasarkan bobot.
# 3. Berapa total bobot MST yang dihasilkan?
#    Total bobot MST yang dihasilkan adalah 6 (1 + 2 + 3).
# 4. Mengapa edge tertentu tidak dipilih?
#    Karena edge tersebut membentuk cycle (misalnya (4, 'A', 'B') dan (5, 'A', 'D')).
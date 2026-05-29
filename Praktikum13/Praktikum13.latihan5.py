#Nama   : Fuad Nizard Attaqi
#NIM    : J0403251086
#Kelas  : A/1
#Praktikum 13 - Graph III: Spanning Tree

#Kasus 2 : Jaringan Komputer

import heapq
graph = {
 'A': {'B': 3, 'C': 2},
 'B': {'A': 3, 'C':4, 'D': 5},
 'C': {'A': 2, 'D': 1},
 'D': {'B': 5, 'C': 1}
}
def prim(graph, start):
    visited = set([start])
    edges = []
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))
    mst = []
    total_weight = 0
    while edges:
        weight, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
    return mst, total_weight
mst, total = prim(graph, 'A')
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
print("Total bobot =", total)

# Jawaban Analisis:
# 1. Kasus apa yang dipilih?
#    Jaringan Komputer
# 2. Algoritma apa yang digunakan?
#    Algoritma Prim.
# 3. Edge mana saja yang dipilih dalam MST?
#    Edge (2, 'A', 'C'), (1, 'C', 'D'), (3, 'A', 'B').
# 4. Berapa total bobot MST?
#    Total bobot MST adalah 6 (1 + 2 + 3).
# 5. Mengapa edge tertentu tidak dipilih?
#    Karena edge tersebut akan membentuk cycle.
# 6. Kenapa memilih algoritma prim?
#    Karena Prim digunakan untuk mencari biaya minimum untuk menghubungkan semua node dalam graph.

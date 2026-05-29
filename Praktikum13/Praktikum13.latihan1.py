#Nama   : Fuad Nizard Attaqi
#NIM    : J0403251086
#Kelas  : A/1
#Praktikum 13 - Graph III: Spanning Tree

# Daftar edge graph
edges = [
 ('A', 'B'),
 ('A', 'C'),
 ('A', 'D'),
 ('C', 'D'),
 ('B', 'D')
]
# Contoh spanning tree
spanning_tree = [
 ('A', 'C'),
 ('C', 'D'),
 ('D', 'B')
]
print("Edge pada graph:")
for edge in edges:
    print(edge)
print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)
print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))    

# Jawaban Analisis:
# 1. Apa perbedaan graph awal dan spanning tree?
# Graph awal: memiliki 5 edge (A-B, A-C, A-D, C-D, B-D) dengan total 4 node
# Spanning tree: memiliki 3 edge (A-C, C-D, D-B) dengan total 4 node
# Perbedaan: Spanning tree tidak memiliki edge A-B

# 2. Mengapa spanning tree tidak boleh memiliki cycle?
# Spanning tree tidak boleh memiliki cycle karena jika ada cycle, maka akan ada lebih dari satu path antar node

# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
# Jumlah edge spanning tree selalu lebih sedikit karena

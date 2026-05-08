#Praktikum 4: Studi Kasus Peta Kota

#Nama   : Fuad Nizard Attaqi
#NIM    : J0403251086
#Kelas   : A/P1


#Node: Kota
#Edges: Rute

#Kota: Jakarta, Bogor, Depok, Bekasi, Tangerang
#Rute: Jakarta-Bogor, Jakarta-Depok, Jakarta-Bekasi, Jakarta-Tangerang, Bogor-Depok, Bogor-Bekasi, Bogor-Tangerang, Depok-Bekasi, Depok-Tangerang, Bekasi-Tangerang

#Output: Adjacency List dan Matrix

#code
#Membuat adjacency list
def adjacencyList (V, edges):
    #using dictionary
    graph = {}

    for it in edges:
        u = it[0]
        v = it[1]

        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []

        graph[u].append(v)
        graph[v].append(u)

    return graph

if __name__ == "__main__":
    V = 5
    edges =  [
        ["Jakarta","Bogor"], 
        ["Jakarta", "Depok"], 
        ["Jakarta", "Bekasi"], 
        ["Jakarta", "Tangerang"], 
        ["Bogor", "Depok"], 
        ["Bogor", "Bekasi"], 
        ["Bogor", "Tangerang"], 
        ["Depok", "Bekasi"], 
        ["Depok", "Tangerang"], 
        ["Bekasi", "Tangerang"]
        ]
    adj = adjacencyList(V, edges)
    print("Adjacency list representation \n")
    for i in adj:
        print(f"{i}:", end=' ')
        for node in adj[i]:
            print(node, end=', ')
        print ()


#Membuat adjacency Matrix
#Jakarta = 0
#Bogor = 1
#Depok = 2
#Bekasi = 3
#Tangerang = 4

def createGraph(V, edges):
    mat = [[0 for _ in range(V)] for _ in range(V)]
    
    for it in edges:
        u = it[0]
        v = it[1]
        mat[u][v] = 1
        mat[v][u] = 1
    return mat

if __name__ == "__main__":
    V = 5

    edges = [
        [0,1],
        [0,2],
        [0,3],
        [0,4],
        [1,2],
        [1,3],
        [1,4],
        [2,3],
        [2,4],
        [3,4]
        ]

    adj = createGraph(V, edges)

    print("\nAdjacency matrix representation")
    for i in range(V):
        for node in adj[i]:
            print(node, end=' ')
        print ()



    




    
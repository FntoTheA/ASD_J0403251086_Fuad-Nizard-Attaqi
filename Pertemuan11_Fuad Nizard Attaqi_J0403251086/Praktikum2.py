# Praktikum 2: Representasi Adjacency List
# Nama   : Fuad Nizard Attaqi
# NIM    : J0403251086
# Kelas   : A/P1

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
    V = 4
    edges =  [["A", "B"], ["A", "C"], ["B", "D"], ["D", "C"]]
    adj = adjacencyList(V, edges)
    print("adjacency list representation")
    for i in adj:
        print(f"{i}:", end=' ')
        for node in adj[i]:
            print(node, end=' ')
        print ()
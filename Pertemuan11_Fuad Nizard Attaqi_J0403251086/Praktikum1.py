#Praktikum 1 : Membuat adjacency matrix
#Nama   : Fuad Nizard Attaqi
#NIM    : J0403251086
#Kelas   : A/P1

#setup node
def createGraph(V, edges):
    mat = [[0 for _ in range(V)] for _ in range(V)]
    
    for it in edges:
        u = it[0]
        v = it[1]
        mat[u][v] = 1
        mat[v][u] = 1
    return mat

#masukin datanya
if __name__ == "__main__":
    V = 4

    edges = [[0,1],[0,2],[1,2],[2,3]]

    adj = createGraph(V, edges)

    print("adjacency matrix representation")
    for i in range(V):
        for node in adj[i]:
            print(node, end=' ')
        print ()



    

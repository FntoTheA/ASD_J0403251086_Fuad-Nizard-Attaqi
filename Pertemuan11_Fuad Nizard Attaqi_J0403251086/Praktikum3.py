# Praktikum 3: Konversi Matrix ke List
#Nama   : Fuad Nizard Attaqi
#NIM    : J0403251086
#Kelas   : A/P1

def createGraph(V, edges):

    mat = [[0 for _ in range(V)] for _ in range(V)]

    for it in edges:

        u = it[0]
        v = it[1]

        mat[u][v] = 1
        mat[v][u] = 1

    return mat


if __name__ == "__main__":

    V = 4

    edges = [
        [0,1],
        [0,2],
        [1,2],
        [2,3]
    ]

    adj = createGraph(V, edges)

    # menampilkan matrix
    print("Adjacency Matrix:\n")

    for i in range(V):

        for node in adj[i]:
            print(node, end=' ')

        print()

    # konversi matrix ke list
    print("\nAdjacency List:\n")

    for i in range(V):

        print(f"{i}:", end=' ')

        for j in range(V):

            if adj[i][j] == 1:
                print(j, end=' ')

        print()
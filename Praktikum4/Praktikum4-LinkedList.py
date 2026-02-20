# Identitas
# NAMA   : Fuad Nizard Attaqi
# NIM    : J0403251086
# Kelas  : A

# Implementasi dasar LinkedList
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


Nodea = Node("A")
Nodeb = Node("B")
Nodec = Node("C")

# hubungin Node
headNode = Nodea
Nodea.next = Nodeb
Nodeb.next = Nodec

# menelusuri node
current = headNode
print(current)
while current is not None:
    print(current.data)
    current = current.next

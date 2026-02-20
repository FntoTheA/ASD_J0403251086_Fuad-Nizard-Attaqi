# Identitas
# NAMA   : Fuad Nizard Attaqi
# NIM    : J0403251086
# Kelas  : A

# Implementasi dasar stack
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        nodeBaru = Node(data)

        nodeBaru.next = self.top

        self.top = nodeBaru

    def pop(self):
        if self.top is None:
            print("Stack Kosong")
            return None
        else:
            data_terhapus = self.top.data
            self.top = self.top.next
            return data_terhapus

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.top.data

    def tampilkan(self):
        current = self.top
        print("Top ", end="->")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None")


s = stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()


print("Data terhapus:", s.pop())
s.tampilkan()
print("data top =", s.peek())

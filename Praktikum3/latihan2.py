#Latihan2:Buat	kode	Implementasikan	Pencarian	pada	node	tertentu	Single Circular	Linked	List.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLL:
    def __init__(self):
        self.head = None
        self.tail = None
    def insertNewValue(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
    def display(self):
        if not self.head:
            print("List is Empty")
            return
        
        print("circular LL Traversal")
        temp = self.head
        print(temp.data, end="->")
        temp = temp.next
        
        while temp != self.head:
            print(temp.data, end="->")
            temp = temp.next
        print("back to head")
    
    def searching(self, key):
       if not self.head:
            print("List is empty")
            return
       temp = self.head
       while True:
            if temp.data == key:
                print(f"Node found: {key}")
                return
            temp = temp.next
            if temp == self.head:
                break 
            
       print("Node not found")

cll	= CircularLL()	

for element in [1,2,3,4,5,6,7,8,9,10]:
    cll.insertNewValue(element)
cll.display()
cll.searching(1)
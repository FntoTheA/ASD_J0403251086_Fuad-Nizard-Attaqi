#Latihan	4:		Buat	metode	untuk	menggabungkan	dua	single	linked	list	menjadi	satu
class node:
    def __init__(self ,data):
        self.data = data
        self.next = None
        
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None #for pointer
        
    def insert_at_end(self,data):
        new_node = node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("null")
        
    def merge(self, other_list):
        if not self.head:
            self.head = other_list.head
            self.tail = other_list.tail
            return
        if not other_list.head:   
            return

        self.tail.next = other_list.head 
        self.tail = other_list.tail     
        

# Contoh Penggunaan 
ll = LinkedList() 
ll2 = LinkedList()
for element in [1,2,3,4,5,6,7,8,9,10]:
    ll.insert_at_end(element)
    
for element in [11,12,13,14,15]:
    ll2.insert_at_end(element)   
ll.display()
ll2.display()

ll.merge(ll2)
ll.display()

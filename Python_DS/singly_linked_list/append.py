class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next
    
    #added data in next
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    #add data in first
    def prepend(self,data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node
    
    #add data next on given node
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous Node doesn't exist!")
        
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    #Delete node by value
    def delete_node(self, key):
        curr_node = self.head

        if curr_node and curr_node.next == key:
            self.head = curr_node.next
            curr_node == None
            return
        prev = None
        while curr_node and curr_node.data !=key:
            prev = curr_node
            curr_node = curr_node.next
        if curr_node is None:
            return
        prev.next = curr_node.next
        curr_node=None


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

llist.prepend("E")


llist.print_list() 
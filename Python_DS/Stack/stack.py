"""
Stack Data structure in Python
"""
class Stack():
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def get_stack(self):
        return self.items

my_stack = Stack()
my_stack.push('A')
my_stack.push('B')
print(my_stack.get_stack())
my_stack.push('C')
print(my_stack.get_stack())
my_stack.pop()
print(my_stack.get_stack())

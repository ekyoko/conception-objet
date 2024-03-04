class MyEmptyStackException(Exception):
    pass

class MyOutOfSizeException(Exception):
    pass

class StackNode:
    def __init__(self, item, next_node=None):
        self.item = item
        self.next_node = next_node
 
class myStack:
    def __init__(self, max_size):
        self.top = None
        self.size = 0
        self.max_size = max_size

    def add_to_stack(self, item):
        if self.size >= self.max_size:
            raise MyOutOfSizeException("La pile est pleine.")
        new_node = StackNode(item, self.top)
        self.top = new_node
        self.size += 1

    def pop_from_stack(self):
        if self.size == 0:
            raise MyEmptyStackException("La pile est vide.")
        item = self.top.item
        self.top = self.top.next_node
        self.size -= 1
        return item

    def is_full(self):
        return self.size >= self.max_size

    def is_empty(self):
        return self.size == 0

print(myStack.pop_from_stack())
print(myStack.is_empty())
print(myStack.pop_from_stack())
print(myStack.is_empty())
print(myStack.pop_from_stack())
print(myStack.is_empty())

try:
    myStack.add_to_stack('hello') 
except MyOutOfSizeException as e:
    print(e)
    
try:
    print(myStack.pop_from_stack()) 
except MyEmptyStackException as e:
    print(e)


#implement a stack
class Node(object):
    def __init__(self, data):
        self.data = data

class Stack(object):
    def __init__(self, data):
        self.top = None
    
    def pop(self):
        if(self.top != None):
            popped = self.top.data
            self.top = self.top.next
            return popped
        return None

        
    
    def push(self, data):
            t = Node(data)
            t.next = self.top
            self.top = Node(data)
    
    def peek(self):
        return self.top.data
    
        
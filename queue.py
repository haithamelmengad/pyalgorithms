#implement a queue
class Node(object):
    def __init__(self, data):
        self.data = data

class Queue(object):
    def __init__(self):
        self.first = None
        self.last = None
    
    def enqueue(self, data):
        if(last != None):
            self.last.next = Node(data)
            self.last = self.last.next
        else: 
            self.last = Node(data)
            self.first = self.last
    
    def dequeue(self):
        if(self.first != None):
            dequeued = self.first.data
            self.first = self.first.next
            if(self.first == None ):
                self.last = None
            return dequeued
        else:
            return None


            
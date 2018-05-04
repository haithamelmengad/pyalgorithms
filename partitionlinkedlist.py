class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def appendToTail(self, data):
        end = Node(data)
        n = self
        while n.next != None:
            n = n.next
        n.next = end

    def node(self, data):
        self.data = data

    def deleteNode(self, data):
        n = self 
        if data == self.data:
            self = n.next
            return self
        else:
            while n.next != None:
                if (n.next.data == data):
                    n.next = n.next.next
                    return n.next
                n = n.next
        return "node doesn't exist"
    
def partition_linked_list(head, d):
    lessInitialized = False
    greaterInitialized = False
    n = head
    less = Node(0)
    greater = Node(0)
    while n.next != None or n.next == None and n.data != None :
        if (n.data < d):
            if not lessInitialized:
                less.node(n.data)
                lessInitialized = True
            else:
                less.appendToTail(n.data)
        if (n.data >= d):
            if not greaterInitialized:
                greater.node(n.data)
                greaterInitialized = True
            else:
                greater.appendToTail(n.data)
        if n.next != None:
          n = n.next
        else:
          break
    p = less.next
    while p.next != None:
      p = p.next
    p.next = greater
    return less            

listhead = Node(4)
listhead.appendToTail(9)
listhead.appendToTail(5)
listhead.appendToTail(3)
listhead.appendToTail(10)
listhead.appendToTail(-10)
listhead.appendToTail(300)
listhead.appendToTail(1000)
listhead.appendToTail(1)
listhead.appendToTail(120)



partitioned = partition_linked_list(listhead, 6)
n = partitioned
while n.next != None or n.next == None and n.data != None:
  print(n.data)
  if n.next != None:
          n = n.next
  else:
          break    




        

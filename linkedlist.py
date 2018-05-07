#implement 
class Node:
  def __init__(self, data):
    self.next = None
    self.data = data
  
  def Node(self, d):
    self.data = d
    
  def appendToTail(self, d):
    end = Node(d)
    n = self
    while n.next != None:
      n = n.next
    n.next = end
  
  def deleteNode(self, d):
    n = self
    if d == self.data:
      self = self.next
      return self.next
      
    while n.next != None:
      if n.next.data == d:
        n.next = n.next.next
        return self
        
      n= n.next

    return self
    
    

#populate
llist = Node(1)
llist.appendToTail(2)
llist.appendToTail(3)
llist.appendToTail(4)
llist.appendToTail(5)
llist.appendToTail(6)
llist.appendToTail(7)
llist.appendToTail(8)
llist.appendToTail(9)
llist.appendToTail(10)
llist.appendToTail(11)
llist.appendToTail(12)
llist.appendToTail(13)
llist.appendToTail(14)
llist.appendToTail(15)
llist.appendToTail(16)
llist.appendToTail(17)




#runner technique
p1 = llist
p2 = llist
while p1.next != None:
  print("pointer 1: ", p1.data)
  p1 = p1.next


while p2.next != None and p2.next.next != None:
    print("pointer 2: ", p2.data)
    p2 = p2.next.next
    print (p2.data)
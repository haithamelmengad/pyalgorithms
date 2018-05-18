# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self.nxt = None
        if self.iterator.hasNext():
            self.nxt = self.iterator.next()
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
=        

    def peek(self):
        return self.nxt
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        

    def next(self):
        current = self.nxt
        if self.iterator.hasNext():
            self.nxt = self.iterator.next()
            return current 
        self.nxt = None
        return current
        """
        :rtype: int
        """
        

    def hasNext(self):
        if self.nxt != None:
            return True
        return False
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
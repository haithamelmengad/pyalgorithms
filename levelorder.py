# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        nodes, level = [], [root]
        while root and level:
            nodes.append([node.val for node in level])
            level = [node for nodepair in [(node.left, node.right) for node in level] for node in nodepair if node]
        return nodes
            
            
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
#         class Queue(object):
#             def __init__(self):
#                 self.l = []

#             def enqueue(self, x):
#                 self.l.append(x)
#                 return True

#             def dequeue(self):
#                 return self.l.pop(0)
#         if root == None:
#             return []
            
#         nodes = []
#         nodes.append([root.val])
#         q = Queue()
#         q.enqueue(root)
#         n = len(q.l)
#         while len(q.l) != 0:
#             level = []
#             while n > 0:
#                 n -= 1
#                 r = q.dequeue()
#                 if r.left != None:
#                     level.append(r.left.val)
#                     q.enqueue(r.left)
#                 if r.right != None:
#                     level.append(r.right.val)
#                     q.enqueue(r.right)
#             if len(level) != 0:
#                 nodes.append(level)
#             n = len(q.l)
            
            
#         return nodes
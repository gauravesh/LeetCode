from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        first=deque()
        second=deque()
        f=list()
        s=list()
        if p:
            first.append(p)
        if q:
            second.append(q)

        #bfs for p

        while first:
            for i in range(len(first)):
                node1=first.popleft()
                f.append(node1.val)
                if node1.left:
                    first.append(node1.left)
                if not node1.left:
                    f.append('not left')

                if node1.right:
                    first.append(node1.right)

                if not node1.right:
                    f.append('not right')

        while second:
            for j in range(len(second)):
                node2=second.popleft()
                s.append(node2.val)
                if node2.left:
                    second.append(node2.left)
                if not node2.left:
                    s.append('not left')

                if node2.right:
                    second.append(node2.right)
                if not node2.right:
                    s.append('not right')
        print(s)
        print(f)
        if f == s:
            return True
        else :
            return False

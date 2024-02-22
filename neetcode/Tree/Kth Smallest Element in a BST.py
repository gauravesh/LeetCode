# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack=[root]
        li=list()
        while stack:
            node=stack.pop()
            if node:
                li.append(node.val)
                
                stack.append(node.right)
                stack.append(node.left)
        li.sort()
        return li[k-1]
        
                

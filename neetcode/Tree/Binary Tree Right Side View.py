from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        li=list()
        res=list()
        first=deque()
        if root:
            first.append(root)
        while first:
            res.append(first[-1].val)
            for i in range(len(first)):
                
                node=first.popleft()
                li.append(node.val)
                if node.left:
                    first.append(node.left)
                if node.right:
                    first.append(node.right)
        return res
                


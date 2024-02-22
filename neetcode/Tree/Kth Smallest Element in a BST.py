# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def find_left_nodes(r):
            li=list()

            if not r:
                return []
            

            if root.left:
                li += find_left_nodes(r.left)
            li.append(r.val)


            
            return li
        d=find_left_nodes(root)
        print(d)
        return d[k-1]
            
            

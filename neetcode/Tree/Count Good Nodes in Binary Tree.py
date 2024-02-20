from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        #preorder verification
        bad_nodes=list()
        def preorder(node,max_val):
            li=list()
            
            if not node:
                return []
            li.append(node.val)
            if node.val < max_val:
                bad_nodes.append(node.val)
            max_val=max(max_val,node.val)

            if node.left:
                li+= preorder(node.left,max_val)
            if node.right:

                li+= preorder(node.right,max_val)
            return li
        x=float('-inf')
        preorder_list=preorder(root,x)
        print(bad_nodes)
        print(preorder_list)
        return len(preorder_list)-len(bad_nodes)

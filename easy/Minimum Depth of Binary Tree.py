# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def preorder(node):
            li=list()
            if node is None:
                return []
            li.append(node.val)
            if node.left:
                li+=preorder(node.left)
            elif not node.left:
                li.append(999)
            if node.right:
                li+=preorder(node.right)
            elif not node.right:
                li.append(999)
            return li
        ss=preorder(root)
        final_length=0
        print(ss)
    


        for index in range(len(ss)):
            if ss[index] == 999 and ss[index+1] == 999:
                
                temp=ss[:index]
                print(temp)
                c=temp.count(999)
                print(c)
                final_length=len(temp)-c
                break
        return final_length

        

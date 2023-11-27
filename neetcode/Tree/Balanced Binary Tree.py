# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_true=True
        def dfs(root):
            nonlocal is_true
            if not root :
                return 0
            left=dfs(root.left)
            right=dfs(root.right)

            val=abs(left-right)
            print(val)

            if val > 1:
                is_true=False

            return 1 + max(left,right)
        dfs(root)
        return is_true


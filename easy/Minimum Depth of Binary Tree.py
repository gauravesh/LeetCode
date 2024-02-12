class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def preorder(node, depth):
            if not node:
                return float('inf')  # Return infinity if the node is None
            
            if not node.left and not node.right:
                return depth  # Return depth if it's a leaf node
            
            left_depth = preorder(node.left, depth + 1)  # Traverse left subtree
            right_depth = preorder(node.right, depth + 1)  # Traverse right subtree
            
            return min(left_depth, right_depth)  # Return the minimum depth
            
        return preorder(root, 1)  # Start the traversal from the root with initial depth 1

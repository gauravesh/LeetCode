from collections import defaultdict

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        def inorder_traversal(node):
            if not node:
                return []
            return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)
        
        # Perform inorder traversal to get a sorted list of values
        values = inorder_traversal(root)
        
        # Count occurrences of each value
        frequency = defaultdict(int)
        for val in values:
            frequency[val] += 1
        
        # Find the maximum frequency
        max_frequency = max(frequency.values())
        
        # Find all values with maximum frequency
        modes = [val for val, freq in frequency.items() if freq == max_frequency]
        
        return modes

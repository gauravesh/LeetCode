from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        first=deque()
        second=deque()
        f=list()
        s=list()
        if root:
            first.append(root)
        if subRoot:
            second.append(subRoot)
        while first:
            for i in range(len(first)):
                node1=first.popleft()
                f.append(node1.val)
                if node1.right:
                    first.append(node1.right)
                elif not node1.right:
                    f.append('not right')
                if node1.left:
                    first.append(node1.left)
                elif not node1.left:
                    f.append('not left')
        while second:
            for i in range(len(second)):
                node2=second.popleft()
                s.append(node2.val)
                if node2.right:
                    second.append(node2.right)
                elif not node2.right:
                    s.append('not right')
                if node2.left:
                    second.append(node2.left)
                elif not node2.left:
                    s.append('not left')
        ins=0
        match=bool()
        for i in range(len(f)):
            if f[i] == s[0]:
                for j in range(len(s)):
                    match=True
                    if f[i+j] != s[j]:
                        match=False
                        break
                    if match:
                        return True
        return False

                    

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# A binary tree is made up of nodes
        # Each node has 3 values
            # node.val, node.left, node.right, pretty easy

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root is None: # We need a way to stop recursion,
            return None

        # TO SWAP THEM:
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)
    
        return root
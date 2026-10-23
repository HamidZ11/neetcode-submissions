# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Longest path between ANY TWO NODES in the binary tree
        
        def dfs(node): #recursive helper function 
            if node is None:
                return 0
            
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            self.diameter = max(self.diameter, left_depth + right_depth)

            return 1 + max(left_depth, right_depth)
        
        self.diameter = 0
        dfs(root)
        return self.diameter

        

        
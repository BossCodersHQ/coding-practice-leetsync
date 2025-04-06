# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(curr):
            if not curr:
                return None
            temp = dfs(curr.left)
            curr.left = dfs(curr.right)
            curr.right = temp
            return curr

        return dfs(root)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        
        def lvs(root):
            ans=[]
            def dfs(root):
                if root is None:
                    return 
                if root.left is None and root.right is None:
                    ans.append(root.val)
                    return 
                dfs(root.left)
                dfs(root.right)
            dfs(root)
            return ans
        sequence1=lvs(root1)
        sequence2=lvs(root2)
        return sequence1==sequence2


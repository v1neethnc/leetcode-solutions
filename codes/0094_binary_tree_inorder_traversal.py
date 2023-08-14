# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
		result = []
		
		def bst_traverse(root, result):
			if root is None:
				return
			bst_traverse(root.left, result)
			result.append(root.val)
			bst_traverse(root.right, result)
			return result
		return bst_traverse(root, result)
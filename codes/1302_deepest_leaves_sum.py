# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
		depth = self.max_depth(root)
		return self.leaves_sum(root, depth, 1)
		
	def leaves_sum(self, root, depth, curr_depth):
		if root is None:
			return 0
		if curr_depth == depth:
			return root.val
		return self.leaves_sum(root.left, depth, curr_depth + 1) + self.leaves_sum(root.right, depth, curr_depth + 1)
	
	def max_depth(self, root):
		if root is None:
			return 0
		left = self.max_depth(root.left)
		right = self.max_depth(root.right)
		return max(left, right) + 1
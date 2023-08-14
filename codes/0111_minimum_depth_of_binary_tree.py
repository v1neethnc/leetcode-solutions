# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def minDepth(self, root: Optional[TreeNode]) -> int:
		if root is None:
			return 0
		
		l_dist = self.minDepth(root.left)
		r_dist = self.minDepth(root.right)
		if l_dist != 0 and r_dist != 0:
			return min(l_dist, r_dist) + 1
		if l_dist == 0:
			return r_dist + 1
		if r_dist == 0:
			return l_dist + 1
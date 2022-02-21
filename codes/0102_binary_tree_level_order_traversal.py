# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
		queue = []
		res = []
		if root == None:
			return []
		queue.append(root)
		while len(queue) > 0:
			level = []
			for i in range(0, len(queue)):
				node = queue.pop(0)
				level.append(node.val)
				if node.left != None:
					queue.append(node.left)
				if node.right != None:
					queue.append(node.right)
			res.append(level)
		return res
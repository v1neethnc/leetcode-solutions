# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def getDecimalValue(self, head: ListNode) -> int:
		str_val = ''
		tmp = head
		while tmp != None:
			str_val += str(tmp.val)
			tmp = tmp.next
		# print(str_val)
		return int(str_val, 2)
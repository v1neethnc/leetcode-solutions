# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
		result, start = None, None
		carry_value = 0
		while l1 is not None or l2 is not None:
			l1_val, l2_val = 0, 0
			if l1 is not None:
				l1_val = l1.val
				l1 = l1.next
			if l2 is not None:
				l2_val = l2.val
				l2 = l2.next

			node_val = l1_val + l2_val + carry_value

			new_node = ListNode(node_val % 10)
			carry_value = node_val // 10
			if result == None:
				result = new_node
				start = result
			else:
				result.next = new_node
				result = result.next
		if carry_value > 0:
			result.next = ListNode(carry_value)
		return start
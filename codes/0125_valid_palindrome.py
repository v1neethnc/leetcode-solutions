class Solution:
	def isPalindrome(self, s: str) -> bool:
		special_char = "~!@#$%^&*()_+`-=[]\\;',./{} |:<>?\"'"
		s = s.lower()
		for i in special_char:
			s = s.replace(i, "")
		return s == s[::-1]
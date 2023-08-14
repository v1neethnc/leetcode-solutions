class Solution:
	def uniqueMorseRepresentations(self, words: List[str]) -> int:
		morse_code_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
		mc_words = []
		for i in words:
			res = ''.join([morse_code_list[ord(j) - ord('a')] for j in i])
			if res not in mc_words:
				mc_words.append(res)
		return len(mc_words)
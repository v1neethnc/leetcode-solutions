class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        start, end = 0, k
        max_vowels = 0
        for start in range(0, len(s) - k + 1):
            st = s[start:start+k]
            vowels = sum(st.count(i) for i in 'aeiou')
            # print(s[start:start+k], vowels, max_vowels)
            max_vowels = max(vowels, max_vowels)
        return max_vowels
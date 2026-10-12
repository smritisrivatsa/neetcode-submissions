class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = Counter(s)
        for char in t:
            freq[char] -= 1
        return all(v==0 for v in freq.values()) 

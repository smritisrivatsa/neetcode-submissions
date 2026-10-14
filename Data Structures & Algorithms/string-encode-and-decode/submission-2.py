class Solution:
    def encode(self, strs: List[str]) -> str:
        # length + "@" + strs[i]
        result = ""

        for i in range(len(strs)):
            result += str(len(strs[i])) + "@" + strs[i]
        return result

    # index:  0 1 2 3 4 5 6 7 8 9 10 11 12 13
    # char:   5 @ H e l l o 5 @ W  o  r  l  d
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "@":
                j += 1
            length = int(s[i:j])
            result.append(s[j+1:j+1+length])
            i = j+1+length
        return result
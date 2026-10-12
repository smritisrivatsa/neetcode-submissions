class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # the key of the map is the sorted string, and the value is 
        # all the anagrams
        anagrams = dict()

        for word in strs:
            key = ''.join(sorted(word))

            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(word)
        return list(anagrams.values())
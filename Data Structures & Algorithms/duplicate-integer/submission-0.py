class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # brute force: nested loops and check nums[i] == nums[j] and return true if case holds. 
        # intialize set, add numbers to set. if nums[i] already in set, return true else false
        seen = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False
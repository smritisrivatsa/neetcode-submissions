class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        # get complement which is target-nums[i]
        # seen stores -> num : index
        # if complement in seen, then return the indices
        # else add nums[i] to seen
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in seen: 
                # pair exists -> complement + nums[i] = target
                return [seen[complement], i]
            seen[nums[i]] = i
        
            
            

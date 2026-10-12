class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        # buckets -> frequency : [numbers with that frequency]
        buckets = dict()
        for num in counts:
            if counts[num] not in buckets:
                buckets[counts[num]] = []
            buckets[counts[num]].append(num)
        
        result = []
        # loop thru buckets k times, add the values to result 
        for i in range(len(nums), 0, -1):
            # check if the num exists as a frequency in buckets
            if i in buckets:
                # loop thru values of i
                for num in buckets[i]:
                    result.append(num)
                    if len(result) == k:
                        return result


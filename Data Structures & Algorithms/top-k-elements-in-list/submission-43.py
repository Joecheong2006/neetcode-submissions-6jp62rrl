class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        l = len(nums)
        freq = [[] for _ in nums]
        for num, f in count.items():
            freq[l - f].append(num)
        
        res = []
        for nums in freq:
            for num in nums:
                res.append(num)
                if len(res) == k:
                    return res

        return res
        
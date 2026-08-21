class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        n = len(nums)
        freq = [[] for _ in nums]

        for num in nums:
            count[num] = count[num] + 1
        
        for item, count in count.items():
            freq[n - count].append(item)

        res = []
        for items in freq:
            for item in items:
                res.append(item)
                if len(res) == k:
                    return res
        
        return res
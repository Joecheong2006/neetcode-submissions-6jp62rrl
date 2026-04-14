class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
    
        count = sorted(count.items(), key=lambda count: count[1], reverse=True)

        return [
            x[0]
            for x in count[0:k]
        ]

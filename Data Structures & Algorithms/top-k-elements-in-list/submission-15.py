class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
    
        count = list(count.items())
        count = sorted(count, key=lambda count: count[1], reverse=True)

        count = [x[0] for x in count[0:k]]
        return count

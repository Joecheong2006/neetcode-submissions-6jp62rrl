class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
    
        count = list(count.items())
        count = sorted(count, key=lambda count: count[1], reverse=True)

        result = []
        for item in count[0:k]:
            result.append(item[0])

        return result

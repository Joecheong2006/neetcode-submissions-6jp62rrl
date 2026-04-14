class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
    
        count = list(count.items())
        count = sorted(count, key=lambda count: count[1])

        result = []
        for item in count[len(count)-k:len(count)]:
            result.append(item[0])

        return result

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        buket = [[] for i in range(len(nums))]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
    
        for key, val in count.items():
            buket[val - 1].append(key)

        result = []
        for i in range(len(buket) - 1, -1, -1):
            for f in buket[i]:
                result.append(f)
                if len(result) == k:
                    return result

        return []
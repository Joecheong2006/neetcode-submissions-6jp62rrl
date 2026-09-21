class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for _ in nums]
        l = len(freq)

        for num in nums:
            count[num] += 1

        for num, f in count.items():
            freq[l - f].append(num)
        
        res = []
        for items in freq:
            for item in items:
                res.append(item)
                k -= 1
                if k == 0:
                    return res

        return res

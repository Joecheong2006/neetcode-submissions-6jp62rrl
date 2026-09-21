class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        freq = defaultdict(list)

        for num, f in count.items():
            freq[f].append(num)
        
        sorted_freq = sorted(freq.keys(), reverse=True)
        res = []

        for f in sorted_freq:
            for item in freq[f]:
                res.append(item)
                k -= 1
                if k == 0:
                    return res

        return res

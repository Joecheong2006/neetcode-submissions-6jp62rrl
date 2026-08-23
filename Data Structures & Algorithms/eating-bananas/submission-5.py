class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 0
        jump = 1

        while True:
            k = jump + start
            count = 0
            for pile in piles:
                count += math.ceil(pile / k)
            
            if jump == 1 and count <= h:
                return start + 1;
                
            if count <= h:
                start += jump // 2
                jump = 1
            else:
                jump *= 2

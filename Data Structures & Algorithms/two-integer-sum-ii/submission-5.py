class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers) - 1):
            a = target - numbers[i]
            
            l = i + 1
            r = len(numbers) - 1

            while l <= r:
                m = (l + r) // 2
                if numbers[m] > a:
                    r = m - 1
                elif numbers[m] < a:
                    l = m + 1
                else:
                    return [i + 1, m + 1]
        return []
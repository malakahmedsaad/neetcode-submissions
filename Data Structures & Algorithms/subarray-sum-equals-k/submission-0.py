class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        sum = 0
        total = 0
        map = {0:1}
        for i in nums:
            sum += i
            x = sum - k

            total += map.get(x,0)
            map[sum] = map.get(sum, 0) + 1
        return total
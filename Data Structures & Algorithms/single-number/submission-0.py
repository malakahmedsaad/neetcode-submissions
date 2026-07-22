class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hm = defaultdict(int)

        for num in nums:
            hm[num] += 1

        for num in nums:
            if hm[num] == 1:
                return num
        return -1

        
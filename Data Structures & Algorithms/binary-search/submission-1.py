import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # else:
        #     return -1 
        index = bisect.bisect_left(nums, target) #Returns the leftmost index where the target should be inserted to keep the list sorted.
        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1
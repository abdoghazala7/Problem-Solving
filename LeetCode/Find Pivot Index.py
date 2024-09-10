class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            if sum(nums[0:i]) == sum(nums[i+1: ]): return i 

        return -1

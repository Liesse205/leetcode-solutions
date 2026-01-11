class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(0, n-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0
        non_zeros = [x for x in nums if x!= 0]
        zeros = [y for y in nums if y == 0]
        return(non_zeros + zeros)
        
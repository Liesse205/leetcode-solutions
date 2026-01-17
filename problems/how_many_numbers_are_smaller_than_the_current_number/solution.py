class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        max_num = max(nums)
        cnt = [0]*(max_num+1)
        for num in nums:
            cnt[num]+=1
        prefix = [0]*(max_num+1)
        for i in range(1, max_num+1):
            prefix[i] = prefix[i-1] + cnt[i-1]
        return [prefix[x] for x in nums]
        
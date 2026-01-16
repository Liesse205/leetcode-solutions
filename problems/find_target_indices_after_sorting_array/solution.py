class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        indices = []
        max_num = max(nums)
        cnt = [0]*(max_num+1)
        res = []
        for i in nums:
            cnt[i] += 1
        for idx, count in enumerate(cnt):
            for _ in range(count):
                res.append(idx)
        for id, num in enumerate (res):
            if num == target:
                indices.append(id)
        return(indices)

        
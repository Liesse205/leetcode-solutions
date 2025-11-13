class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        vals = []
        for num in nums:
            if not vals or num != vals[-1]:
                vals.append(num)
        count = 0
        for i in range (1, len(vals) -1):
            if vals[i] > vals[i-1] and vals[i] > vals[i+1]:
                count +=1
            elif vals[i] < vals[i-1] and vals[i] < vals[i+1]:
                count +=1
        return count

                

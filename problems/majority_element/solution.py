class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        n = len(nums)
        m_occurence = n/2
        num = Counter(nums)
        for i, j in num.items():
            if j > m_occurence:
                return(i)
        
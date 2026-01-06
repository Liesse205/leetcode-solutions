class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        n = len(nums)
        m_appearence = n/3
        majority = []
        count = Counter(nums)
        for i, j in count.items():
            if j > m_appearence:
                majority.append(i)
        return(majority)
        
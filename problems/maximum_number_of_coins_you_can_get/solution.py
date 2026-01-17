class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        s_piles = sorted(piles)
        return(sum(s_piles[(len(s_piles))//3::2]))
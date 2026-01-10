class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 != 0:
            small = n * 2
        else:
            small = n
        return(small)
        
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d1 = "".join(str(num) for num in digits) 
        d2 = int(d1)+1
        res = [int(n) for n in str(d2)]
        return(res)      
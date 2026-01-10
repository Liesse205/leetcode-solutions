class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        checkp = 0
        original = x
        while original > 0:
            checkp = checkp * 10 + original % 10
            original //= 10
        if (checkp == x):
            return True
        return False 
        
        
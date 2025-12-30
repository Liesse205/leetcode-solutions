class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        original = x
        rev_num = 0
        while x > 0:
            rev_num = rev_num * 10 + x % 10
            x //= 10
        return original == rev_num
        
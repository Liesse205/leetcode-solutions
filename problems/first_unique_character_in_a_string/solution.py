class Solution:
    def firstUniqChar(self, s: str) -> int:
        r = {}
        for ch in s:
            r[ch] = r.get(ch, 0)+1
        for i, ch in enumerate(s):
            if r[ch] == 1:
                return(i)
        return (-1)    
        
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return("")
        pref = ""
        for i in range(len(strs[0])):
            char = strs[0][i]
            for word in strs:
                if i >= len(word) or word[i] != char:
                    return pref
            pref += char
        return(pref)

        

        
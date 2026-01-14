class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(1, len(names)):
            key = heights[i]
            name = names[i]
            for j in range(i-1, -1, -1):
                if j >= 0 and key > heights[j]:
                    heights[j+1] = heights[j]
                    names[j+1] = names[j]
                    heights[j] = key
                    names[j] = name
        return(names)        
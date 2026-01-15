class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        from collections import Counter
        cnt = Counter(arr1)
        res = []
        for x in arr2:
            res.extend([x]*cnt[x])
        n_arr2 = [x for x in arr1 if x not in arr2]
        n_arr2.sort()
        res.extend(n_arr2)
        return(res)

        
        
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        diagonals = [[] for _ in range(rows+cols-1)]
        for i in  range(rows):
            for j in range(cols):
                diagonals[i+j].append(mat[i][j])
        result = []
        for idx, diagonal in enumerate(diagonals):
            if idx%2 == 0:
                result.extend(diagonal[::-1])
            else:
                result.extend(diagonal)
        return(result)
        
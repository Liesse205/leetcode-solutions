class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ans = [[0] * (len(img[0])) for _ in range(len(img))]
        for row in range (len(img)):
            for col in range(len(img[row])):
                total, cnt = 0, 0
                for i in range(row-1, row+2):
                    for j in range(col-1, col+2):
                        if i >=len(img) or i<0 or j>=len(img[row]) or j<0:
                            continue
                        total +=img[i][j]
                        cnt += 1
                average = total//cnt
                ans[row][col] = average
        return(ans)
        
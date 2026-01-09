class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [x for x in range (1, n+1)]
        res = 0
        while len(players) > 1:
            res = (res+k-1)% len(players)
            players.pop(res)
        return(players[0])
        
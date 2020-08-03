class Solution:

    def numJewelsInStones(self, J: str, S: str) -> int:

        

        J = list(J)

        counts = [S.count(i) for i in J]

        ans = sum(counts)

        

        return an
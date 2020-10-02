class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        gem = set()
        for each in J:
            gem.add(each)
        res = 0
        for each in S:
            if each in gem:
                res += 1
        return res

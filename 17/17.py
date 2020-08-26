class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        num2char = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        def dfs(digits,prefix):
            if not digits:
                nonlocal res
                res.append(prefix)
            else:
                for eachChar in num2char[digits[0]]:
                    dfs(digits[1:],prefix+eachChar)
        dfs(digits,"")
        return res
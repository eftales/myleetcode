class Solution:
    def reverseWords(self, s: str) -> str:
        subStrs = []
        subStr = []
        for each in s:
            if each != " ":
                subStr.insert(0,each)
            else:
                subStrs.append(subStr)
                subStr = []
        subStrs.append(subStr)
        res = ""
        for each in subStrs:
            
            res += "".join(each)
            res += " "
        return res[0:-1]

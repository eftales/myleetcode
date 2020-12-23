class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = dict()
        for i,each in enumerate(s): 
            if each in count:
                count[each] = -1
            else:
                count[each] = i
        first = len(s)
        for key in count:
            if count[key] != -1 and first > count[key] :
                first = count[key]

        
        return first if first != len(s) else -1
        
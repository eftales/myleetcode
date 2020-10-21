class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
       
        i = 0
        j = 0
        cur = None
        while  j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
                cur = name[i-1]
            elif typed[j] == cur:
                j += 1
            else:
                break
        if i == len(name) and j == len(typed):
            return True
        else:
            return False

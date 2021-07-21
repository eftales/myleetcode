class Solution:
    def maxTurbulenceSize(self, arr) -> int:
        arrLen = len(arr)
        if arrLen <= 2:
            return arrLen
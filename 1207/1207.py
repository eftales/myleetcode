class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        numCount = dict()
        for each in arr:
            if each not in numCount:
                numCount[each] = 1
            else:
                numCount[each] += 1
        freq = set()
        for eachKey in numCount:
            if numCount[eachKey] not in freq:
                freq.add(numCount[eachKey])
            else:
                return False
        return True
class Solution:
    def intersect(self, nums1, nums2) :
        dic = dict()

        for each in nums1:
            if each in dic:
                dic[each][0] += 1
            else:
                dic[each] = [1,0]
        
        for each in nums2:
            if each in dic:
                dic[each][1] += 1
            else:
                dic[each] = [0,1]

        res = []
        for each in dic:
            n = min(dic[each])
            if n != 0:
                for i in range(0,n):
                    res.append(each)
        
        return res

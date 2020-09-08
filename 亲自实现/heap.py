class heap(object):
    # 小根堆
    def __init__(self,nums : list):
        self.array = nums
        self.maxIndex = len(self.array) - 1
        self.buildHeap()

    def buildHeap(self):
        for i in range((self.maxIndex-1)//2,-1,-1):
            self.heapify(i)

    def heapify(self,parent):
        lChild = 2 * parent + 1
        rChild = 2 * parent + 2
        if rChild > self.maxIndex:
            rChild = lChild
        if self.array[lChild] < self.array[rChild]:
            if self.array[lChild] < self.array[parent]:
                temp = self.array[lChild]
                self.array[lChild] = self.array[parent]
                self.array[parent] = temp
        else: 
            if self.array[rChild] < self.array[parent]:
                temp = self.array[rChild]
                self.array[rChild] = self.array[parent]
                self.array[parent] = temp


    def fix(self):
        index = (self.maxIndex-1)//2
        while index >= 0:
            self.heapify(index)
            index = (index-1)//2

    def push(self,elm):
        self.array.append(elm)
        self.maxIndex += 1
        self.fix()

    def pop(self):
        if self.array == []:
            return None
        res = self.array.pop(0)
        self.maxIndex -= 1
        if self.maxIndex >= 0:
            temp = self.array.pop()
            self.array.insert(0,temp)
            self.fix()
        return res


nums = list(range(12,0,-1))
hp = heap(nums)
for i in range(12,0,-1):
    print(hp.pop())

for i in range(12,0,-1):
    print(hp.push(i))

for i in range(12,0,-1):
    print(hp.pop())
# 将 a 映射为 0，b 映射为 1，以此类推
# 对于 26 个字母而言，取 31 为模比较合适

# 映射函数
def char2int(c):
    return ord(c)-ord('a')

# 加密函数
def encrypt(s): # s 需要是一个 list，每一个元素都是字符
    base = 31
    res = 0
    for i,each in enumerate(s):
        res += char2int(each)*base**i
    return res

encrypt(['a','b','c','a'])

# 这个只是最简单的情况，复杂情况还需考虑取模

for each in [1,2,3]:
    if each == 4:
        break
else:
    print("22")
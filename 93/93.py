class Solution:
    def restoreIpAddresses(self, s: str):
        if len(s)<4 or len(s)>12:
            return []
        res = []
        for i in range(1,4):
            curStack = []
            temp = s[0:i]
            if s[0] == '0' and i>1: # 首位为零的话，这一位必须是 0
                break # 如果不满足就跳出本层循环，只有上层可以解决这个问题
            if len(s[i:]) > 9:
                continue
            if int(temp) <=255 and 3<=len(s[i:]):
                curStack.append(temp)
                for j in range(i+1,i+4):
                    temp = s[i:j]
                    if s[i] == '0' and j-i>1: # 首位为零的话，这一位必须是 0
                        break  # 如果不满足就跳出本层循环，只有上层可以解决这个问题
                    if len(s[j:]) > 6:
                        continue
                    
                    if int(temp) <=255 and 2<=len(s[j:]):
                        curStack.append(temp)
                        for k in range(j+1,len(s)):
                            temp1 = s[j:k]
                            if s[j] == '0' and k-j>1: # 首位为零的话，这一位必须是 0
                                continue # 由于本层循环确定了最后两位，因此可以在本层解决这个问题
                            temp2 = s[k:]
                            if s[k] == '0' and (len(s)-k)>1:
                                continue

                            if int(temp1) <=255 and int(temp2)<=255:
                                curStack.append(temp1) 
                                curStack.append(temp2)
                                res.append(".".join(curStack))
                                curStack.pop()
                                curStack.pop()   
                        curStack.pop()  
                    else:
                        break
                curStack.pop()
                        

            else:
                break

        return res            
           

s = Solution()
s.restoreIpAddresses("101023")
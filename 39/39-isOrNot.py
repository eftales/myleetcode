class Solution:
    def combinationSum(self, candidates, target: int) :
        calcul = dict() # key 代表需要被分解的数，val 表示可以怎么分解
        def dfs(n,path):
            if n not in calcul:
                calcul[n] = []
                for eachCandi in candidates:
                    if not path:
                        path.append(eachCandi)
                    else:
                        if eachCandi < path[-1] : # 必须是升序序列
                            continue
                        else:
                            path.append(eachCandi)
                    if  (n-eachCandi ) > 0:
                        calcul[n].append([eachCandi,n-eachCandi])
                        success = dfs(n-eachCandi,path)
                        if not success:
                            calcul[n].pop()
                    elif (n-eachCandi ) == 0:
                        calcul[n].append([eachCandi,n-eachCandi])
                    path.pop()

            if len(calcul[n]) == 0:
                return False
            else:
                return True
        
                

        

        return dfs(target,[])
s=Solution()

print(s.combinationSum(candidates = [2,3,6,7], target = 1))



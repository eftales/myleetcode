class Solution:
    def videoStitching(self, clips, T: int) -> int:
        F = [-1] * (T+1)
        clips.sort()
        zero = clips[0]
        for i in range(zero[0],min(T+1,zero[1]+1)): # 第一段素材的 end 可能比所需长度要长
            F[i] = 1
        if F[0] == -1:
            return -1  # 视频素材不包含 0 时刻
        for i in range(1,len(clips)):
            begin = clips[i][0]
            if begin > T: # 冗余的视频素材
                break
            end = clips[i][1] if clips[i][1] <= T  else T # 过长的视频素材
            
            if F[begin] == -1: 
                return -1
            elif F[end] != -1:
                continue
            else:
                baseNum = F[begin] if begin != 0 else 0
                for j in range(begin+1,end+1): # dp 中最耗时的地方
                    if F[j] == -1:
                        F[j] = baseNum + 1
                if F[-1] != -1:
                    return F[-1]
        return F[-1]
class Solution:
    def videoStitching(self, clips, T: int) -> int:
        count = 0
        i = 0
        boundry = 0
        nextBoundry = 0
        clips.sort()

        while True:
            while i<len(clips) and clips[i][0] <= boundry:
                nextBoundry = max(nextBoundry,clips[i][1])
                i += 1
            if nextBoundry <= boundry:
                return -1
            boundry = nextBoundry
            count += 1
            if boundry >= T:
                return count
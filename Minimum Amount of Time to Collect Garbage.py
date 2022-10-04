class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        mins = [0,0,0,0,0,0]
        ts = sum(travel)
        for i in range(len(garbage)-1,-1,-1):
            mins[0] += garbage[i].count('G')
            mins[1] += garbage[i].count('M')
            mins[2] += garbage[i].count('P') 
            if garbage[i].count('G') > 0 and mins[3]==0:
                mins[3] = ts 
            if garbage[i].count('M') > 0 and mins[4] == 0:
                mins[4] = ts 
            if garbage[i].count('P') > 0 and mins[5] == 0:
                mins[5] = ts 
            ts -= travel[i-1] 
        return sum(mins)

import math
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        for i in queries:
            x,y,r = i[0],i[1],i[2]
            count = 0
            for j in points:
                xf,yf = j[0],j[1]
                if math.sqrt(math.pow(xf-x,2)+math.pow(yf-y,2)) <= r:
                    count += 1
            res.append(count)
        return res
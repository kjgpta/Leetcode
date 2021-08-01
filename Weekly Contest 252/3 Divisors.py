class Solution:
    def isThree(self, n: int) -> bool:
        cou = 0
        for i in range(1,n+1):
            if n%i == 0:
                cou += 1
            if cou > 3:
                return False
        if cou == 3:
            return True
        else:
            return False
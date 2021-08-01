class Solution:
    def minimumPerimeter(self, x: int) -> int:
        z = 1
        while True:
            b = int(z/2)
            if b * b * b * 4 + b * b * 6 + b * 2 >= x:
                return z*4
            else:
                z += 1
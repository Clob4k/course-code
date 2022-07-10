class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            ret = int(str(x)[::-1])
        elif x < 0:
            ret = int(str(x)[:0:-1]) * -1
        else:
            return 0
        if ret > 2147483647 or ret < -2147483648:
            return 0
        return ret
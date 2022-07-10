class Solution:
    def isPalindrome(self, int):
        self.int = int
        if int < 0:
            return False
        conv = str(int)
        conv = conv[::-1]
        if conv == str(int):
            return True
        else:
            return False
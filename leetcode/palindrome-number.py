class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringNum = str(x)
        for i in range(len(stringNum) // 2):
            if stringNum[i] != stringNum[len(stringNum) - i - 1]:
                return False
        return True
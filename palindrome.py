class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            var = x
            temp = 0
            for i in range(0,len(str(x))):
                temp = (temp*10) + var%10
                var = var // 10
        if (temp == x):
            return True
        else:
            return False

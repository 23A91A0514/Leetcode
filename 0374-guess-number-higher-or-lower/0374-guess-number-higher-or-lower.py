# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

# The guess API is already defined for you.
# def guess(num: int) -> int:

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n

        while low <= high:
            mid = (low + high) // 2  # Prevents overflow
            res = guess(mid)
            if res == 0:
                return mid
            elif res == -1:
                high = mid - 1
            else:  # res == 1
                low = mid + 1

        
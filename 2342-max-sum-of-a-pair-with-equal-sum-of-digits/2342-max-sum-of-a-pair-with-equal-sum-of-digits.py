class Solution(object):
    def maximumSum(self, nums):
        d = {}
        maxi = -1

        for num in nums:
            s = sum(int(x) for x in str(num))

            if s in d:
                maxi = max(maxi, d[s] + num)
                d[s] = max(d[s], num)
            else:
                d[s] = num

        return maxi
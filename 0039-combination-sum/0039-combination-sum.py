class Solution(object):
    def combinationSum(self, candidates, target):
        ans = [[]]

        for num in candidates:
            new = []

            for x in ans:
                total = sum(x)

                while total + num <= target:
                    x = x + [num]
                    new.append(x)
                    total += num

            ans += new

        result = []

        for x in ans:
            if sum(x) == target:
                result.append(x)

        return result
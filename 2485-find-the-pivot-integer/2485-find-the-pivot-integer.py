class Solution:
    def pivotInteger(self, n: int) -> int:
        total = n * (n + 1) // 2
        root = int(total ** 0.5)

        return root if root * root == total else -1
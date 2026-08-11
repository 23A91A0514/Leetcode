class MyHashSet:

    def __init__(self):
        # Pre-allocate an array for all possible keys up to 10^6
        self.data = [False] * 1000001

    def add(self, key: int) -> None:
        self.data[key] = True

    def remove(self, key: int) -> None:
        self.data[key] = False

    def contains(self, key: int) -> bool:
        return self.data[key]
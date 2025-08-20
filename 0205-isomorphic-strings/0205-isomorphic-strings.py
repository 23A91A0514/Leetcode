class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_mapped = set()

        for char_s, char_t in zip(s, t):
            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False
            else:
                if char_t in t_mapped:
                    return False
                s_to_t[char_s] = char_t
                t_mapped.add(char_t)

        return True

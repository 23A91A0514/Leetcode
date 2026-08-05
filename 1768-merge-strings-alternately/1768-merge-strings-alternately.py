class Solution:

  def mergeAlternately(self, word1: str, word2: str) -> str:
    s = []
    n1, n2 = len(word1), len(word2)
    for i in range(max(n1, n2)):
      if i < n1:
        s.append(word1[i])
      if i < n2:
        s.append(word2[i])
    return "".join(s)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        frequencyTable = defaultdict(int)

        for i in s:
            frequencyTable[i] += 1
        
        for j in t:
            frequencyTable[j] -= 1

            if frequencyTable[j] <0:
                return False
        return True

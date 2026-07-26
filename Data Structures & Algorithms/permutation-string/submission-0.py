class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        for i in range(len(s2) - n + 1):
            sub = s2[i:i+n]      
            if sorted(sub) == sorted(s1):
                return True
        return False
            
            
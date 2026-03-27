class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = [str(i) for i in magazine]
        for i in ransomNote:
            if i not in magazine:
                return False
            magazine.remove(i)

        return True

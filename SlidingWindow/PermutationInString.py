class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): # if the length of s1 is greater we cant find match obviously
            return False

        s1Count, s2Count = [0] * 26, [0] * 26 # hasmap for both the strings
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1 # frequency of first window in s2

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0) # Count how many characters already match
            # matches = 26 means perfect match → permutation found

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a') # add new character (right side)
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
            
            # Remove old character (left side)
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26

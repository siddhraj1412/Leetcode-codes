# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
 

# Constraints:

# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer than s2, no permutation of s1 can exist in s2
        if len(s1) > len(s2):
            return False

        # Create frequency arrays for 26 lowercase English letters
        # s1Count -> frequency of each character in s1
        # s2Count -> frequency of characters in current window of s2
        s1Count = [0] * 26
        s2Count = [0] * 26

        # Fill frequency counts:
        # - Entire s1
        # - First window of s2 (same length as s1)
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # 'matches' tells how many characters (out of 26)
        # have the SAME frequency in s1Count and s2Count
        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1
        # If matches == 26 → all characters match → permutation found

        # Left pointer of the sliding window
        l = 0

        # Start sliding the window from index len(s1) to end of s2
        for r in range(len(s1), len(s2)):

            # If all 26 characters match, permutation exists
            if matches == 26:
                return True

            # ============================
            # ADD new character to window
            # ============================
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1

            # If after adding, counts become equal → gained a match
            if s1Count[index] == s2Count[index]:
                matches += 1
            # If it was equal before, but now exceeded → lost a match
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # ===============================
            # REMOVE old character from window
            # ===============================
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1

            # If after removing, counts become equal → gained a match
            if s1Count[index] == s2Count[index]:
                matches += 1
            # If it was equal before, but now reduced → lost a match
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1

            # Move the left pointer forward
            l += 1

        # Final check for the last window
        return matches == 26

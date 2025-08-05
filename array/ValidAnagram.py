# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false


# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Initialize a frequency array of size 26 (for each letter 'a' to 'z')
        checkArr = [0] * 26

        # Count frequency of each character in string s
        for char in s:
            index = ord(char) - ord('a')  # Get index between 0-25
            checkArr[index] += 1

        # Subtract frequency based on characters in string t
        for char in t:
            index = ord(char) - ord('a')  # Get index between 0-25
            checkArr[index] -= 1

        # If any count is not 0, then s and t are not anagrams
        for count in checkArr:
            if count != 0:
                return False

        # If all counts are 0, then s and t are anagrams
        return True


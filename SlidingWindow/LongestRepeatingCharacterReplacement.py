# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        count={}
        res=0
        maxf=0
        for r in range(len(s)):
            count[s[r]]=1+count.get(s[r],0)
            # adding char count to the hashmap
            maxf=max(maxf,count[s[r]])
            
            # window is valid or not
            while (r-l+1)-maxf > k:
                # if its not valid it will enter loop 
                count[s[l]]-=1 # reducing count of the left pointer
                l+=1 # change left pointer position
            res=max(res,r-l+1) # check if max is res or current window length
        return res

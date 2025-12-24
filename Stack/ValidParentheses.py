# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

# Example 5:

# Input: s = "([)]"

# Output: false

 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        h={")" : "(", "]" : "[", "}" : "{" }
        s1=[]
        for c in s:
            if c in h: # to check if its close bracket
                if s1 and s1[-1]==h[c]: # if it is then check if s is not empty and its equal to top of stack value
                    s1.pop()
                else: # if any condition not true return false
                    return False
            else:
                s1.append(c)
        return not s1 # cause it can store as many open bracket as possible and if the s is empty than it means we have matched all the parentheses

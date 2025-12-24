# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9
 

# Constraints:

# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105

class Solution:
    def trap(self, height: List[int]) -> int:

        if not height: return 0 # if height is empty
        
        l,r=0,len(height)-1
        
        lmax,rmax=height[l],height[r] # to get max height so we can know how much water it can have
        res=0
        
        while l<r:
          # only interating when the lmax is less than rmax
          if lmax<rmax:
                l+=1                    
                lmax=max(lmax,height[l]) 
                res+=lmax-height[l] # to check how much water it can store from left side
            else:
                r-=1
                rmax=max(rmax,height[r])
                res+=rmax-height[r] # same as right side
        return res

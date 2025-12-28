# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

 

# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols=len(matrix),len(matrix[0])
        top,bot=0,rows-1
        while top<=bot:
            row=(top+bot)//2
            if target>matrix[row][-1]:
                # which means target value is greater than the last element of the row than we have to shift out top row
                top=row+1
            elif target<matrix[row][0]:
                # which means target value is less than the first element of the row than we have to shift out bottom row
                bot=row-1
            else:
                # in this case we have found the row where the target value should be so break the loop
                break
        
        if not(top<=bot):
            # it shows that non of the rows contain our target value
            return False

        row=(top+bot)//2
        l,r=0,cols-1
        
        while l<=r:
            m=(l+r)//2
            if target>matrix[row][m]:
                # which means we have to shift our middle value upper side
                l=m+1
            elif target<matrix[row][m]:
                # which means we have to shift our middle value lower side
                r=m-1
            else:
                return True
                # which means we have find the value
        return False # which means there's no target value in our matrix

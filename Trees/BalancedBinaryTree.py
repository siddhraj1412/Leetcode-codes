# Given a binary tree, determine if it is height-balanced.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:


# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left = self.height(root.left)
        right = self.height(root.right)
        if abs(left - right) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.height(root.left), self.height(root.right))


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def h(root):
            if not root:
                return [True,0]
            # A node is balanced if:
            # Left subtree is balanced
            # Right subtree is balanced
            # Height difference ≤ 1
            left=h(root.left)
            right=h(root.right)
            balanced=left[0] and right[0] and abs(left[1]-right[1])<=1

            # Height of the current node = 1 + max(leftHeight, rightHeight)
            return [balanced,1+max(left[1],right[1])]
        return h(root)[0]

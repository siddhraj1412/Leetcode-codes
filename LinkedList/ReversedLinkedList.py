# Given the head of a singly linked list, reverse the list, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
 

# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

-> iterative 
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev will store the previous node (initially None because the new tail points to nothing)
        # curr will start from the head of the linked list
        prev, curr = None, head
        
        # Loop until we reach the end of the linked list
        while curr:
            # Save the next node before breaking the link
            # This prevents losing access to the remaining list
            nxt = curr.next
            
            # Reverse the current node's pointer
            # Instead of pointing to the next node, it points to the previous node
            curr.next = prev
            
            # Move prev one step forward
            # prev now becomes the current node
            prev = curr
            
            # Move curr one step forward using the saved next node
            curr = nxt
            
        # After the loop, prev will be pointing to the new head of the reversed list
        return prev

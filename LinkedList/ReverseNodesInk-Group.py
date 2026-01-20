# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Example 2:


# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
 

# Constraints:

# The number of nodes in the list is n.
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000
 

# Follow-up: Can you solve the problem in O(1) extra memory space?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        groupPrev=dummy

        while True:
            kth=self.getK(groupPrev,k)
            # if its empty which means we have reached end of the list so we have to break loop 
            if not kth:
                break
            groupNext=kth.next

            prev,cur=kth.next,groupPrev.next

            while cur!=groupNext:
                temp=cur.next
                cur.next=prev
                prev=cur
                cur=temp

            tmp=groupPrev.next
            groupPrev.next=kth
            groupPrev=tmp
        return dummy.next

    def getK(self,cur,k):
        while cur and k>0:
            cur=cur.next
            k-=1
        return cur

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None or head.next.next is None:
            return
        
        middle = self.findMiddle(head)

        temp = middle.next
        middle.next = None

        head2 = self.reverse(temp)


        curr = head

        # Time - O(N) (Total as well)
        while head and head2:
            head = head.next

            curr.next = head2
            curr = curr.next

            head2 = head2.next

            curr.next = head
            curr = curr.next
        



    #O(N)
    def reverse(self,head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

   #O(N)
    def findMiddle(self,head: ListNode) -> ListNode:
        slow = head
        fast = head.next #THIS IS THE TRICK!!
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
    



    
    




        
        
        
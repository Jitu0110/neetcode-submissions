# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)

            if kth is None:
                break

            groupNext = kth.next

            # Reverse group
            prev = groupNext # Usually start with Null. But here making it groupNext!!
            curr = groupPrev.next #1

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Reconnect reversed group (By updating groupPrev pointer)
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next

    def getKth(self, node, k):
        while node is not None and k > 0:
            node = node.next
            k -= 1

        return node
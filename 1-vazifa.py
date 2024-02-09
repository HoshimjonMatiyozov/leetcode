class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head.next:
            return None

        left = head
        right = head

        while n > 0:
            right = right.next
            n -= 1

        if not right:
            return head.next

        while right.next:
            left = left.next
            right = right.next

        left.next = left.next.next

        return head
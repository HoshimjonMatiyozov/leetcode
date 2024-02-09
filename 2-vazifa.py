class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head 

        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        
        prev, curr = None, slow 

         
        while curr:
            nxt = curr.next 
            curr.next = prev 
            prev = curr
            curr = nxt 
        
        first_half, reversed_half = head, prev 

        
        while first_half and reversed_half:
            if first_half.val != reversed_half.val:
                return False 
            
            first_half = first_half.next 
            reversed_half = reversed_half.next 
        
        return True 

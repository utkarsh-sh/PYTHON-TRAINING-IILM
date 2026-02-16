class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sp = fp = head
        while fp:
            sp = sp.next
            if fp.next == None:
                return False
            fp = fp.next.next

            if sp == fp:
                return True

        return False
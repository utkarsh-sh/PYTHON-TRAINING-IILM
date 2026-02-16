class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        d = {}
        while headA:
            d[headA] = -1
            headA = headA.next
        while headB:
            if headB in d:
                return headB
            headB = headB.next
        return None
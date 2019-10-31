from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverse(self, start, end):
        newhead=ListNode(0); newhead.next=start
        while newhead.next!=end:
            tmp=start.next
            start.next=tmp.next
            tmp.next=newhead.next
            newhead.next=tmp
        return [end, start]
    def reverseKGroup(self, head, k):
        if head==None:
            return None
        nhead=ListNode(0)
        nhead.next=head
        start=nhead
        while start.next:
            end=start
            for i in range(k-1):
                end=end.next
                if end.next==None:
                    return nhead.next
            res=self.reverse(start.next, end.next)
            start.next=res[0]
            start=res[1]
        return nhead.next

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

x = Solution()
ans = x.reverseKGroup(n1, 2)
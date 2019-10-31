from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        point = dummy
        while point.next and point.next.next:
            swap1 = point.next
            swap2 = swap1.next
            point.next = swap2
            swap1.next = swap2.next
            swap2.next = swap1
            point = swap1
        return dummy.next

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)

n1.next = n2
n2.next = n3
n3.next = n4

x = Solution()
ans = x.swapPairs(n1)

while ans:
    print(ans.val)
    ans = ans.next
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        nodelist = []
        while head.next:
            nodelist.append(head)
            head = head.next
        nodelist.append(head)
        nodelist.reverse()
        idx = 0
        while idx < len(nodelist)-1:
            nodelist[idx].next = nodelist[idx+1]
            idx += 1
        nodelist[-1].next = None
        
        return head

X = Solution()

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

X.reverseList(n1)
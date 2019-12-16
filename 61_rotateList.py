# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode: 
        if not head or not head.next:
            return head

        n = 1
        tmpNode = head
        while tmpNode.next:
            n += 1
            tmpNode = tmpNode.next
        tmpNode.next = head
        m = n - k%n
        for i in range(m):
            tmpNode = tmpNode.next
        newhead = tmpNode.next
        tmpNode.next = None
        # print(newhead.val)
        return newhead

x = Solution()

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
k = 2
x.rotateRight(n1, k)

n1 = ListNode(0)
n2 = ListNode(1)
n3 = ListNode(2)
n1.next = n2
n2.next = n3
k = 4
x.rotateRight(n1,k)
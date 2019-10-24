# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        tmpNode = ListNode(0)
        res = tmpNode
        while l1 and l2:
            #print("l1: "+ str(l1.val)+", l2: "+str(l2.val))
            if l1.val < l2.val:
                tmpNode.next = l1
                l1 = l1.next
            else:
                tmpNode.next = l2
                l2 = l2.next
            tmpNode = tmpNode.next
        if l1 == None:
            tmpNode.next = l2
        else:
            tmpNode.next = l1
        return res.next # without the first 0 at the declaration

x = Solution()

a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(4)
b1 = ListNode(1)
b2 = ListNode(3)
b3 = ListNode(4)
a1.next = a2
a2.next = a3
b1.next = b2
b2.next = b3

ans = x.mergeTwoLists(a1, b1)
while ans:
    print(ans.val)
    ans = ans.next
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        theHead = head
        while head.next:
            if head.val == head.next.val:
                if head.next.next:
                    head.next = head.next.next
                    continue
                else:
                    head.next = None
                    break
            head = head.next
        return theHead
    
X = Solution()

n1 = ListNode(1)
n2 = ListNode(1)
n3 = ListNode(2)
n1.next = n2
n2.next = n3
n = X.deleteDuplicates(n1)
while n:
    print(n.val,end="->")
    n = n.next
print()

n1 = ListNode(1)
n2 = ListNode(1)
n3 = ListNode(2)
n4 = ListNode(3)
n5 = ListNode(3)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n = X.deleteDuplicates(n1)
while n:
    print(n.val,end="->")
    n = n.next
print()

nList = [1,1,2,3,3,4,1,2,3,1,2,4,5,2,1,20,1,1,1,2,3,4,6,7,5,12,12]
head = ListNode(nList[0])
nxt = ListNode(nList[1])
head.next = nxt
for n in nList[2:]:
    nxt.next = ListNode(n)
    nxt = nxt.next
n = X.deleteDuplicates(head)
while n:
    print(n.val, end="->")
    n = n.next
print()

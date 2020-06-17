# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        theHead = head
        markedList = []
        if not head:
            return
        while head.next:
            if head.val == head.next.val:
                markedList.append(head.val)
                if head.next.next:
                    head.next = head.next.next
                    continue
                else:
                    head.next = None
                    break
            head = head.next
        head = theHead # start over for finding the heading duplicated elements
        while head: # remove the heading duplicated elements
            if head.val in markedList:
                head = head.next
                # print(head.val)
            else:
                break
        theHead = head # reset head for start over agin to find other duplicated elements
        while head: # remove the duplicated elements in the rest of list
            if head.next:
                if head.next.val in markedList:
                    if head.next.next:
                        head.next = head.next.next
                        continue
                    else:
                        head.next = None
                        break
            head = head.next
        return theHead
    
X = Solution()

nList = [1,2,3,3,4,4,5]
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

nList = [1,1,1,2,3]
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
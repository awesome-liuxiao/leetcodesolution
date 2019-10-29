from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        res = []
        if lists == []:
            return None
        for l in lists:
            while l:
                res.append(l.val)
                l = l.next
        res.sort()
        if res == []:
            return None
        tmpNode = ListNode(res.pop(0))
        headNode = tmpNode
        for e in res:
            tmpNode.next = ListNode(e)
            tmpNode = tmpNode.next
        return headNode
        # length = len(lists)
        # if length == 1:
        #     return lists[0]
        # if length == 0:
        #     return None
        # def mergeTwoLits(l1: ListNode, l2: ListNode):
        #     tmpNode = ListNode(0)
        #     res = tmpNode
        #     while l1 and l2:
        #         if l1.val < l2.val:
        #             tmpNode.next = l1
        #             l1 = l1.next
        #         else:
        #             tmpNode.next = l2
        #             l2 = l2.next
        #         tmpNode = tmpNode.next
        #     if l1 == None:
        #         tmpNode.next = l2
        #     else:
        #         tmpNode.next = l1
        #     return res.next
        # while length > 1:
        #     k = int((length+1) / 2)
        #     for i in range(int(length/2)):
        #         lists[i] = mergeTwoLits(lists[i], lists[i+k])
        #     n = k
        #     return lists[0]

n1 = ListNode(1)
n2 = ListNode(4)
n3 = ListNode(5)
n4 = ListNode(1)
n5 = ListNode(3)
n6 = ListNode(4)
n7 = ListNode(2)
n8 = ListNode(6)

n1.next = n2
n2.next = n3
n4.next = n5
n5.next = n6
n7.next = n8

x = Solution()
ans = x.mergeKLists([n1,n4,n7])

while ans:
    print(ans.val)
    ans = ans.next
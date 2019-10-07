class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = [str(l1.val)]
        s2 = [str(l2.val)]
        while(l1.next):
            l1 = l1.next
            s1.insert(0,str(l1.val))
        while (l2.next):
            l2 = l2.next
            s2.insert(0, str(l2.val))

        ss1 = ''.join(s1)
        ss2 = ''.join(s2)
        lsum = list(str(int(ss1) + int(ss2)))
        lsum.reverse()
        res = []
        for e in lsum:
            res.append(ListNode(int(e)))
            i=0
        for node in range(len(res)-1):
            res[i].next = res[i+1]
            i += 1
        # print(res[0].next.val)
        return res[0]
x = Solution()

node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)
node4 = ListNode(5)
node5 = ListNode(6)
node6 = ListNode(4)

node1.next = node2
node2.next = node3
node4.next = node5
node5.next = node6
x.addTwoNumbers(node1, node4)

# coding:utf-8

# 寻找两个链表的第一个公共结点

'''
主要考查的是时间和空间效率的平衡。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        pass


def test():
    head1 = ListNode(1)
    p1 = ListNode(2)
    p2 = ListNode(3)
    head1.next = p1
    p1.next = p2

    head2 = ListNode(4)
    h1 = ListNode(5)
    h2 = ListNode(1)
    head2.next = h1
    h1.next = h2

    a = Solution()
    b = a.FindFirstCommonNode(head1, head2)
    while b:
        print b.val
        b = b.next

if __name__ == "__main__":
    test()
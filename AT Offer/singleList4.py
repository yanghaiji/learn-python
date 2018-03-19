# coding:utf-8

# 反转链表

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        result = None
        while pHead:
            temp = pHead.next
            pHead.next = result
            result = pHead
            pHead = temp
        return result
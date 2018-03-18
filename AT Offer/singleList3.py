# coding:utf-8

# 合并两个排序的链表
from singleLinkedList import List

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        result = temp = ListNode(0)
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                temp.next = pHead1
                pHead1 = pHead1.next
            else:
                temp.next = pHead2
                pHead2 = pHead2.next
            temp = temp.next
        temp.next = pHead1 or pHead2
        return result.next
# coding:utf-8

# 链表中倒数第K个结点
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if k <= 0 or head == None:
            return
        tempNode = head
        temp = 0
        beforeNode = head
        while tempNode:
            tempNode = tempNode.next
            temp += 1
            if temp > k:
                beforeNode = beforeNode.next
        if temp < k:
            return
        return beforeNode
            

# coding:utf-8

# 链表中倒数第K个结点
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        tempNode = head
        tempList = []
        while tempNode:
            tempList.append(tempNode)
            tempNode = tempNode.next
        if k > len(tempList) or k <1:
            return
        return tempList[-k]

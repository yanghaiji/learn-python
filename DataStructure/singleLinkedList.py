#coding:utf-8

#使用Python编写链表

#定义节点类Node
class Node():
    #data表示节点保存的数据，_next表示下一个节点的对象
    def __init__(self, data):
        self.data = data
        self._next = None

    # 输出节点的数据域
    def __printdata__(self):
        return self.data

# 定义链表类
class List(object):
    # 初始化链表
    def __init__(self):
        self.head = None
        self.length = 0

    #判断链表是否为空
    def isEmpty(self):
        return self.head == None

    # 在链表尾增加一个元素
    def appendNode(self, dataNode):
        tempNode = Node(dataNode)
        #判断是否为头结点
        if self.isEmpty():
            self.head = tempNode
            self.length += 1
        else:
             node = self.head
             while node._next:
                 node = node._next
             node._next = tempNode
             self.length += 1

    # 判断结点元素是否存在于链表
    def searchNode(self, item):
        tempNode = self.head
        foundNode = False
        while tempNode._next and not foundNode:
            if tempNode.data == item:
                foundNode = True
            tempNode = tempNode._next
        return foundNode

    # 删除链表中的某个结点
    def deleteNode(self, item):
        dataNode = Node(item)
        preNode = None
        tempNode = self.head
        while tempNode._next:
            if tempNode.data == dataNode.data:
                if preNode:
                    preNode._next = tempNode._next
                else:
                    self.head = tempNode._next
                break
            else:
                preNode = tempNode
                tempNode = tempNode._next


if __name__ == "__main__":
    singleLinkedList = List()
    for item in range(10):
        singleLinkedList.appendNode(item)
    print singleLinkedList.searchNode(8)
    print singleLinkedList.deleteNode(8)
    print singleLinkedList.searchNode(8)


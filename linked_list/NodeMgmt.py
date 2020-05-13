class Node:
    def __init__(self, data, next = None, prev=None):
        self.data = data
        self.prev = prev
        self.next = next


class LinkedList:
    def __init__(self, data):
        newNode = Node(data)
        self.head = newNode

    def add(self, data):
        node = self.head
        while node.next:
            node = node.next
        newNode = Node(data)
        node.next = newNode
        return True

    def delete(self, data):
        node = self.head
        if node.data == data:
            print('First value is deleted : {} '.format(node.data))
            self.head = node.next
            del node
            if self.head == None:
                print('Linked list is empty')
            return True
        else:
            while node.next.data != data:
                if node.next == None:
                    print('Warning : There is no value {} in this LinkedList'.format(data))
                    return False
                node = node.next
            if node.next.next == None:
                print('Last value is deleted : {} '.format(node.next.data))
                node.next = None
                return True
            else:
                print('Value is deleted : {} '.format(node.next.data))
                node.next = node.next.next

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

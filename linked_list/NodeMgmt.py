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


    def search(self, data):
        node = self.head

        while node.data != data and node is not None:
            node = node.next
        if node is None:
            print('Value {} is not in Linked list'.format(data))
            return False
        return node.data



class DoubleLinkedList:
    def __init__(self, data):
        newNode = Node(data)
        self.head = newNode
        self.tail = newNode


    def add(self, data):
        node = self.head
        while node.next:
            node = node.next
        newNode = Node(data)
        self.tail = newNode
        node.next = newNode
        newNode.prev = node


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
                self.tail = node
            else:
                print('Value is deleted : {} '.format(node.next.data))
                node.next = node.next.next
                node.next.prev = node
            return True


    def desc(self, from_tail = False):
        if not from_tail:
            node = self.head
            while node:
                print(node.data)
                node = node.next
        else:
            node = self.tail
            while node:
                print(node.data)
                node = node.prev
        return


    def search(self, data, from_tail=False):
        if not from_tail:
            node = self.head
            while node.data !=data and node.next is not None:
                node = node.next
            if node is None:
                print('Value {} is not in Double Linked list'.format(data))
                return False
            return node
        else:
            node = self.tail
            while node.data !=data and node.prev is not None:
                node = node.prev
            if node is None:
                print('Value {} is not in Double Linked list'.format(data))
                return False
            return node


    def insert_before(self, data, node_value):
        if self.head == None:
            self.head = Node(data)
            return True

        node = self.head
        if node.data == node_value:
            newNode = Node(data)
            newNode.next = node
            node.prev = newNode
            self.head = newNode
            return True

        while node.next is not None and node.next.data != node_value :
            node = node.next
            if node.next is None:
                print('Value {} is not in Double Linked list'.format(node_value))
                return False

        newNode = Node(data)
        newNode.prev = node
        newNode.next = node.next
        node.next = newNode
        newNode.next.prev = newNode
        return True
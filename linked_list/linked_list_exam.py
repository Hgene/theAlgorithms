
from linked_list.NodeMgmt import Node, LinkedList

linked_list1 = LinkedList(0)
for i in range(1,5):
    linked_list1.add(i)
linked_list1.desc()

linked_list1.delete(0)
linked_list1.desc()

linked_list1.delete(4)
linked_list1.desc()

linked_list1.delete(2)
linked_list1.desc()
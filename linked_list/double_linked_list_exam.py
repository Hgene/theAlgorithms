from linked_list.NodeMgmt import Node, LinkedList, DoubleLinkedList

double_linked_list1 = DoubleLinkedList(0)

for i in range(1,5):
    double_linked_list1.add(i)

double_linked_list1.desc()
double_linked_list1.desc(from_tail=True)

print('Search_value is 2, and find value is {}'.format(double_linked_list1.search(2).data))
print('Search_value is 2, and find value is {}'.format(double_linked_list1.search(2, from_tail=True).data))
double_linked_list1.delete(0)
double_linked_list1.desc()

double_linked_list1.delete(4)
double_linked_list1.desc()

double_linked_list1.delete(2)
double_linked_list1.desc()

double_linked_list1.insert_before(2, 3)
double_linked_list1.desc()

double_linked_list1.insert_before(0, 1)
double_linked_list1.desc()

double_linked_list1.insert_before(4, 4)
double_linked_list1.desc()
class LinkedList:
    head = None

    class Node:
        element = None
        next_node = None

        def __init__(self, element, next_node = None):
            self.element = element
            self.next_node = next_node

    def append(self, element):
        if not self.head:
            self.head = self.Node(element)
            return element
        node = self.head

        while node.next_node:
            node = node.next_node

        node.next_node = self.Node(element)


    def insert_node(self, index, element):
        node = self.head
        pre_node = self.head

        for i in range(index):
            pre_node = node
            node = node.next_node

        pre_node.next_node = self.Node(element, next_node = node)

        return element

    def get_node(self, index):
        node = self.head
        pre_node = self.head

        for i in range(index):
            pre_node = node
            node = node.next_node
        return node.element

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next_node

        node = self.head
        pre_node = node

        for i in range(index):
            pre_node = node
            node = node.next_node

        pre_node.next = node.next_node
        element = node.element

        del node

        return element

    def assign(self, index, element):
        node = self.head

        for _ in range(index):
            node = node.next_node

        node.element = element

    def out(self):
        node = self.head

        while node.next_node:
            print(node.element)
            node = node.next_node
        print(node.element)

    def delete_duplicates(self):
        node = self.head
        while node and node.next_node != None:
            if node.next_node.element == node.element:
                node.next = node.next.next
            else:
                node = node.next_node
        print(self.head)


linked_list = LinkedList()

linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
# linked_list.append(57)
# linked_list.append(78)
# linked_list.append(77)
# linked_list.append(8)

linked_list.insert_node(3, 666)

linked_list.append(50)
linked_list.append(60)

print('\n')
print(linked_list.get_node(3))
print('\n')

linked_list.assign(3, 777)

linked_list.delete_duplicates()

linked_list.out()

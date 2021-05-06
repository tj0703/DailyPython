class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.numNodes = 0

    def insert_start(self, data):

        self.numNodes += 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.nextNode = self.head
            self.head = new_node

    def insert_end(self, data):

        self.numNodes += 1
        new_node = Node(data)

        actual_node = self.head

        while actual_node.nextNode is not None:
            actual_node = actual_node.nextNode

        actual_node.nextNode = new_node

    def traverse(self):

        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.nextNode

    def size_of_list(self):
        return self.numNodes

    def find_middle_node(self):

        # size_list = self.size_of_list()
        # mid_node = size_list/2
        #
        # if size_list != 0:
        #     actual_node = self.head
        #     while actual_node.nextNode is not None and mid_node > 0:
        #         actual_node = actual_node.nextNode
        #         mid_node -= 1
        #
        #     print(actual_node.data)

        fast_pointer = self.head
        slow_pointer = self.head

        while fast_pointer.nextNode and fast_pointer.nextNode.nextNode:
            fast_pointer = fast_pointer.nextNode.nextNode
            slow_pointer = slow_pointer.nextNode

        print(slow_pointer.data)

    def reverse_list(self):

        current_node = self.head
        pre_node = None
        next_node = None

        while current_node is not None:
            next_node = current_node.nextNode
            current_node.nextNode = pre_node
            pre_node = current_node
            current_node = next_node

        self.head = pre_node


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_start(1)
    ll.insert_end(2)
    ll.insert_start(3)
    ll.insert_end(4)
    ll.insert_start(5)
    ll.insert_end(6)
    ll.traverse()
    ll.reverse_list()
    ll.traverse()
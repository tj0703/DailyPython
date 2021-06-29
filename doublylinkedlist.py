import time


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):

        new_node = Node(data)

        #when the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        #there is at least 1 item in the list, inserting new item at the end
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

        #traverse the list in forward direction
    def traverse_f(self):

        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next

        #traverse the list in backward direction
    def traverse_b(self):

        actual_node = self.tail

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.previous


if __name__ == '__main__':
    dl = DoublyLinkedList()
    now1 = time.time()
    for i in range(0, 50000):
        dl.insert(1)
    print(f"time required: {str(time.time()-now1)}")

    now2 = time.time()
    array = []
    for i in range(0, 50000):
        array.append(1)
    print(f"time required for appending array: {str(time.time()-now2)}")
from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        elif self.storage.length == self.capacity:
            curr_head = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)

            if curr_head == self.current:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        self.storage.print()

        first_node = self.current
        list_buffer_contents.append(first_node.value)

        if first_node.next:
            next_node = first_node.next
        else:
            next_node = self.storage.head

        while next_node is not first_node:
            list_buffer_contents.append(next_node.value)
            if next_node.next:
                next_node = next_node.next
            else:
                next_node = self.storage.head

        return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

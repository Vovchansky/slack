class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next_item = None
        self.prev_item = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, item):
        if isinstance(item, Node):
            if self.head is None:
                self.head = item
                item.prev_item = None
                item.next_item = None
                self.tail = item
            else:
                self.tail.next_item = item
                item.prev_item = self.tail
                self.tail = item

    def pop(self):
        old_tail = self.tail
        new_tail = self.tail.prev_item
        new_tail.next_item = None
        old_tail.prev_item = None
        self.tail = new_tail

    def unshift(self, elem):
        if self.head is None:
            self.head = elem
            self.tail.prev_item = self.head
        else:
            temp = self.head
            self.head = Node(elem)
            self.head.next_item = temp

    def shift(self):
        if self.head.next_item is not None:
            self.head = self.head.next_item
        else:
            self.tail = None

    def len(self):
        count = 0
        curr_node = self.head
        while curr_node is not None:
            count = count + 1
            curr_node = curr_node.next_item
        return count

    def delete(self, elem):
        curr_node = self.head
        while curr_node is not None:
            if curr_node.elem == elem:
                if curr_node.prev_item is not None:
                    if curr_node.next_item is not None:
                        new_prev = curr_node.prev_item
                        new_next = curr_node.next_item
                        new_prev.next_item = new_next
                        new_next.prev_item = new_prev
                    else:
                        self.pop()
                else:
                    self.shift()
            curr_node = curr_node.next_item

    def contains(self, elem):
        curr_node = self.head
        while curr_node is not None:
            if curr_node.elem == elem:
                return True
            curr_node = curr_node.next_item
        return False

    def first(self):
        return self.head.elem

    def last(self):
        return self.tail.elem

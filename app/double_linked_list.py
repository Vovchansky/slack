"""DoubleLinkedList realization"""


class Item:  # pylint: disable=too-few-public-methods
    """Initialization of class Item"""

    def __init__(self, elem=None):
        self.elem = elem
        self.next_item = None
        self.prev_item = None


class DoubleLinkedList:
    """Initialization of class DoubleLinkedList"""

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        curr_node = self.head
        to_print = []
        while curr_node is not None:
            to_print.append(curr_node.elem)
            curr_node = curr_node.next_item
        return str(to_print)

    def push(self, elem=None):
        """Add an elemant to the end of the list"""
        if elem is None:
            raise ValueError('Cannot add None item to the end of the list')
        else:
            if not isinstance(elem, Item):
                elem = Item(elem)
            if self.head is None:
                self.head = elem
            else:
                self.tail.next_item = elem
                elem.prev_item = self.tail
            self.tail = elem

    def pop(self):
        """Remove an element from the end of the list"""
        if self.head is None:
            raise ValueError('Cannot add pop item from the empty list')
        else:
            if self.head == self.tail:
                self.head = None
            else:
                new_tail = self.tail.prev_item
                new_tail.next_item = None
                self.tail = new_tail

    def unshift(self, elem=None):
        """Add an element to the beginning of the list"""
        if elem is None:
            raise ValueError('There is nothing to add to the list')
        else:
            if not isinstance(elem, Item):
                elem = Item(elem)
            if self.head is None:
                self.head = elem
                self.tail = elem
            else:
                new_head = elem
                self.head.prev_item = new_head
                new_head.next_item = self.head
                self.head = new_head

    def shift(self):
        """Remove an element from the beginning of the list"""
        if self.len() == 0:
            raise ValueError('There is nothing to delete from the beginning of the list')
        else:
            if self.head.next_item is not None:
                old_head = self.head
                new_head = self.head.next_item
                new_head.prev_item = None
                old_head.next_item = None
                self.head = new_head
            else:
                self.tail = None
                self.head = None

    def len(self):
        """Return the length of the list"""
        count = 0
        curr_node = self.head
        while curr_node is not None:
            count = count + 1
            curr_node = curr_node.next_item
        return count

    def delete(self, elem=None):
        """Remove an element from the list"""
        if elem is None or self.len() == 0:
            raise ValueError('There is nothing to delete')
        else:
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

    def contains(self, elem=None):
        """Check if if an element is on the list"""
        if elem is None:
            raise ValueError('Cannot search for an element = None item to a list')
        else:
            curr_node = self.head
            while curr_node is not None:
                if curr_node.elem == elem:
                    return True
                curr_node = curr_node.next_item
            return False

    def first(self):
        """Return the first item of the list"""
        return self.head.elem

    def last(self):
        """Return the last item of the list"""
        return self.tail.elem

"""Unittest class"""
import unittest
from double_linked_list import DoubleLinkedList


class TestDoubleLinkedList(unittest.TestCase):
    """Initialization of unittest class"""
    d_linked_list = None

    def setUp(self):
        """We need it to reinitialize the list before each test"""
        self.d_linked_list = DoubleLinkedList()

    def test_init(self):
        """Initialization test"""
        self.assertEqual(self.d_linked_list.head, None, "Initial HEAD should be None")
        self.assertEqual(self.d_linked_list.tail, None, "Initial TAIL should be None")
        self.assertEqual(self.d_linked_list.len(), 0, "Initial length should be zero")

    def test_unshiift_exceptions(self):
        """Empty unshift() test"""
        with self.assertRaises(ValueError):
            self.d_linked_list.unshift()

    def test_contains_exceptions(self):
        """Empty list contains() test"""
        with self.assertRaises(ValueError):
            self.d_linked_list.contains()

    def test_shift_from_empty_list(self):
        """Empty list shift() test"""
        with self.assertRaises(ValueError):
            self.d_linked_list.shift()

    def test_pop_from_empty_list(self):
        """Empty list pop() test"""
        with self.assertRaises(ValueError):
            self.d_linked_list.pop()

    def test_delete_from_empty_list(self):
        """Empty list delete() test"""
        with self.assertRaises(ValueError):
            self.d_linked_list.delete()

    def test_delete_none(self):
        """Empty delete from the initialized list test"""
        self.d_linked_list.unshift(2)
        with self.assertRaises(ValueError):
            self.d_linked_list.delete()

    def test_delete(self):
        """Different delete() tests"""
        self.d_linked_list.unshift(2)
        self.d_linked_list.unshift(3)
        self.assertEqual(str(self.d_linked_list), '[3, 2]', "List should be printed as [3, 2]")
        self.assertEqual(self.d_linked_list.len(), 2, "List should be length=2")
        self.d_linked_list.delete(2)
        self.assertEqual(str(self.d_linked_list), '[3]', "List should be printed as [3]")
        self.d_linked_list.unshift(4)
        self.assertEqual(str(self.d_linked_list), '[4, 3]', "List should be printed as [4, 3]")
        self.d_linked_list.delete(3)
        self.d_linked_list.delete(4)
        self.assertEqual(str(self.d_linked_list), '[]', "List should be printed as []")

    def test_len(self):
        """Different len() tests"""
        self.assertEqual(self.d_linked_list.len(), 0, "Empty list is of length zero")
        self.d_linked_list.unshift(1)
        self.assertEqual(self.d_linked_list.len(), 1, "List with one element is of length=1")
        self.d_linked_list.unshift(2)
        self.assertEqual(self.d_linked_list.len(), 2, "List with two elements is of length=2")
        self.d_linked_list.unshift(3)
        self.assertEqual(self.d_linked_list.len(), 3, "List with three elements is of length=3")
        self.d_linked_list.unshift(4)
        self.assertEqual(self.d_linked_list.len(), 4, "List with four elements is of length=4")

    def test_list(self):
        """Some more tests"""
        self.assertEqual(str(self.d_linked_list), '[]', "List should be printed as [] when empty")
        self.d_linked_list.unshift(1)
        self.assertEqual(str(self.d_linked_list), '[1]', "List should be printed as [1]")
        self.d_linked_list.unshift(2)
        self.assertEqual(str(self.d_linked_list), '[2, 1]', "List should be printed as [2, 1]")
        self.d_linked_list.unshift(3)
        self.assertEqual(str(self.d_linked_list), '[3, 2, 1]', "List should be [3, 2, 1]")
        self.d_linked_list.unshift(5)
        self.assertEqual(str(self.d_linked_list), '[5, 3, 2, 1]', "List should be [5, 3, 2, 1]")
        self.d_linked_list.unshift(4)
        self.assertEqual(str(self.d_linked_list), '[4, 5, 3, 2, 1]', "List [4, 5, 3, 2, 1]")

    def first(self):
        """First element of the list tests"""
        self.assertEqual(self.d_linked_list.first(), None, "Should return None when initialized")
        self.d_linked_list.unshift(1)
        self.d_linked_list.unshift(5)
        self.assertEqual(self.d_linked_list.first(), 5, "Should return 5 if the List is [5, 1]")

    def last(self):
        """Last element of the list tests"""
        self.assertEqual(self.d_linked_list.last(), None, "Should return None when initialized")
        self.d_linked_list.unshift(18)
        self.d_linked_list.unshift(7)
        self.assertEqual(self.d_linked_list.last(), 18, "Should return 18 if the List is [7, 18]")


if __name__ == '__main__':
    unittest.main()

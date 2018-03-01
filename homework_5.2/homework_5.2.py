
import unittest

from typing import Iterable


class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None  # type: LinkedListNode


class LinkedList:

    def __init__(self, values: Iterable):
        previous = None
        self.head = None
        for value in values:
            current = LinkedListNode(value)
            if previous:
                previous.next = current
            self.head = self.head or current
            previous = current

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    # def reverse(self) -> None:
    #     raise NotImplementedError

    def reverse(self):
        current = self.head
        previous = None     # = None, т.к. нет узла перед head

        while current:
            next = current.next
            current.next = previous     # None в первой итерации
            previous = current          # Используется в след.итерации
            current = next              # Переход к след.узлу
        self.head = previous
        return self

linked_list = LinkedList([1, 2, 3])
print(list(linked_list))
print(list(linked_list.reverse()))

class LinkedListTestCase(unittest.TestCase):

    def test_reverse(self):
        cases = dict(
            empty=dict(
                items=[],
                expected_items=[],
            ),
            single=dict(
                items=[1],
                expected_items=[1],
            ),
            double=dict(
                items=[1, 2],
                expected_items=[2, 1],
            ),
            triple=dict(
                items=[1, 2, 3],
                expected_items=[3, 2, 1],
            ),
        )
        for case, data in cases.items():
            with self.subTest(case=case):
                linked_list = LinkedList(data['items'])
                linked_list.reverse()
                self.assertListEqual(
                    data['expected_items'],
                    list(linked_list),
                )

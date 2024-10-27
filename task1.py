class Node:
    def __init__(self, data):
        self.data = data  # Дані вузла
        self.next = None  # Посилання на наступний вузол

class LinkedList:
    def __init__(self):
        self.head = None  # Початковий вузол списку

    def append(self, data):
        # Додає новий вузол в кінець списку
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def reverse(self):
        # Реверсує список, змінюючи посилання між вузлами
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insertion_sort(self):
        # Сортує список методом вставок
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            sorted_list = self._sorted_insert(sorted_list, current)
            current = next_node
        self.head = sorted_list

    def _sorted_insert(self, head, node):
        # Вставляє вузол у відсортований список
        if not head or node.data < head.data:
            node.next = head
            return node
        current = head
        while current.next and current.next.data < node.data:
            current = current.next
        node.next = current.next
        current.next = node
        return head

    @staticmethod
    def merge_sorted(list1, list2):
        # Об'єднує два відсортовані списки в один
        dummy = Node(0)
        tail = dummy
        while list1 and list2:
            if list1.data < list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2
        return dummy.next

    def to_list(self):
        # Перетворює список у звичайний Python список
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

# Приклад використання
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(3)
    ll.append(1)
    ll.append(2)
    print("Original list:", ll.to_list())

    ll.reverse()
    print("Reversed list:", ll.to_list())

    ll.insertion_sort()
    print("Sorted list:", ll.to_list())

    ll1 = LinkedList()
    ll1.append(1)
    ll1.append(3)
    ll1.append(5)

    ll2 = LinkedList()
    ll2.append(2)
    ll2.append(4)
    ll2.append(6)

    merged_head = LinkedList.merge_sorted(ll1.head, ll2.head)
    merged_list = LinkedList()
    merged_list.head = merged_head
    print("Merged sorted list:", merged_list.to_list())
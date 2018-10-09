class Element:
    def __init__(self, value, next_el=None):
        self.value = value
        self.next_el = next_el

    def __repr__(self):
        return str(self.value)


class SingleLinkedList:
    def __init__(self, values: list = None):
        self.head = None
        if values:
            prev_elem = None
            for value in values:
                element = Element(value=value)
                if not self.head:
                    self.head = element
                if prev_elem:
                    prev_elem.next_el = element
                prev_elem = element

    def __repr__(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next_el
        return '->'.join(str(value) for value in values)

    # O(n) if last element is not known
    # O(1) if we know the last element
    def append_end(self, value):
        if self.head:
            current = self.head
            while current.next_el:
                current = current.next_el
            current.next_el = Element(value)
        else:
            self.head = Element(value)

    # O(1)
    def append_start(self, value):
        element = Element(value=value)
        if self.head:
            element.next_el = self.head
        self.head = element

    # O(1) + (__getitem__)
    def insert(self, value, idx):
        prev_elem = self.__getitem__(idx - 1)
        new_element = Element(value, next_el=prev_elem.next_el)
        prev_elem.next_el = new_element

    # O(n)
    # replace it with __getitem__
    def __getitem__(self, idx):
        current_element = self.head
        counter = 0
        while current_element:
            if counter == idx:
                return current_element
            else:
                counter += 1
                current_element = current_element.next_el
        raise IndexError

    # O(n)
    def search(self, value):
        idx = 0
        current_element = self.head
        while current_element:
            if current_element.value == value:
                return idx
            else:
                idx += 1
                current_element = current_element.next_el
        return 0

    def delete(self, value):
        if self.head and self.head.value == value:
            self.head = self.head.next_el
            return 1

        current = self.head
        while current:
            if current.next_el and current.next_el.value == value:
                current.next_el = current.next_el.next_el
                return 1
            else:
                current = current.next_el
        return 0

    def delete_first(self):
        if self.head:
            result = self.head.value
            self.head = self.head.next_el
        else:
            result = None
        return result

    def __len__(self):
        counter = 0
        current = self.head
        while current:
            counter += 1
            current = current.next_el
        return counter

    @property
    def aslist(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next_el
        return result


def test():
    assert SingleLinkedList([]).aslist == []
    linked_list = SingleLinkedList([1, 2, 3, 4])
    assert str(linked_list) == "1->2->3->4"
    assert len(linked_list) == 4
    linked_list.append_start(10)
    assert linked_list.aslist == [10, 1, 2, 3, 4]
    linked_list.append_end(15)
    assert linked_list.aslist == [10, 1, 2, 3, 4, 15]
    linked_list.insert(20, 2)
    assert linked_list.aslist == [10, 1, 20, 2, 3, 4, 15]
    assert linked_list[2].value == 20
    assert linked_list.search(15) == len(linked_list) - 1
    assert linked_list.delete(15)
    assert linked_list.delete(20)
    assert linked_list.delete(10)
    assert not linked_list.delete(42)
    assert len(linked_list) == 4


if __name__ == '__main__':
    test()

from lists import SingleLinkedList


class Stack:
    def __init__(self, top=None):
        if top:
            self.linked_list = SingleLinkedList(values=[top])
        else:
            self.linked_list = SingleLinkedList()

    # O(1)
    def push(self, value):
        self.linked_list.append_start(value)

    # O(1)
    def peek(self):
        if self.linked_list.head:
            return self.linked_list.head.value
        else:
            return None

    # O(1)
    def pop(self):
        return self.linked_list.delete_first()

    def __repr__(self):
        return str(self.linked_list)


class ArrayStack:
    def __init__(self, top=None):
        self.stack = []
        if top:
            self.stack.append(top)

    def push(self, value):
        self.stack.append(value)

    def peel(self):
        return self.stack[-1]

    def pop(self):
        return self.stack.pop()

    def __repr__(self):
        return str(self.stack)


def test():
    stack = Stack()
    assert not str(stack)
    assert stack.peek() is None
    assert stack.pop() is None

    stack = Stack(top=1)
    assert stack.peek() == 1
    stack.push(2)
    assert stack.peek() == 2
    assert stack.pop() == 2
    assert stack.peek() == 1
    assert stack.pop() == 1
    assert stack.peek() is None


if __name__ == '__main__':
    test()

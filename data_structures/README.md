## Lists

**List** or **sequence** - is an abstract data type that represents countable number of ordered values

### Arrays

**Array** is a list which have an index. Properties:

- Fast search by index
- Week adding or deleting - worst case - `O(n)`

### Linked lists

In **linked lists** each element points to the next one and sometimes to the previous one.

- Easy to insert or delete an element - we only need to change reference
- Slow indexing

## Stacks

**Stack** serves as a collection of elements, with such principal operations:

- *push* - add element to collection
- *pop* - remove most recently added element
- L.I.F.O order - last in, first out
- peek - get access to the top without modifying the stack

Stacks can be implemented as arrays or as linked lists.

## Queues

**Queue** in which the entities in the collection are kept in order:

- *enqueue* - add element to the end
- *dequeue* - get and remove element from the front
- F.I.F.O order - first in, first out

In python implemented at the [collection.dequeue](https://docs.python.org/3/library/collections.html#collections.deque)

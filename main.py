class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return str(self.data)


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


class Queue:
    def __init__(self) -> None:
        self.LinkedList = LinkedList()

    def __str__(self) -> str:
        nodes = [str(x) for x in self.LinkedList]
        return "\n".join(nodes)

    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False

    def enqueue(self, new_node):
        if self.LinkedList.head is None:
            self.LinkedList.head = new_node
            self.LinkedList.tail = new_node
        else:
            self.LinkedList.tail.next = new_node
            self.LinkedList.tail = new_node

    def dequeue(self):
        if self.LinkedList.head is None:
            return "Queue is empty"
        else:
            temp_node = self.LinkedList.head
            if self.LinkedList.head == self.LinkedList.tail:
                self.LinkedList.head = None
                self.LinkedList.teal = None
            else:
                self.LinkedList.head = self.LinkedList.head.next
            return temp_node

    def peek(self):
        if self.LinkedList.head is None:
            return "Queue is empty"
        else:
            return f"\n{self.LinkedList.head}\n"

    def delete(self):
        self.LinkedList.head = None
        self.LinkedList.tail = None


# Create a schedule (queue)
schedule = Queue()

# Add some tasks (nodes) in schedule
schedule.enqueue(Node("1) Start learning basic syntax of Python"))
schedule.enqueue(Node("2) Then look through data structures and algorithms"))
schedule.enqueue(Node("3) Search other advanced topics"))
print(schedule)

# Delete first task
schedule.dequeue()

# Show the main (first) task in schedule
main_topic = schedule.peek()
print(main_topic)

print(schedule)

# Clean all queue
schedule.delete()
print(schedule)

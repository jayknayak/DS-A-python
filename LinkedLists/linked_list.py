# Includes the following implementations:
# 1. CRUD on a LinkedList: insert_new_head, insert_node_at_end, insert_node_after_given_node, delete_node, print_linked_list
# 2. Reversing a LinkedList: print_reverse_linked_list, reverse_linked_list, reverse_linked_list_iterative
# 3. Comparing two LinkedLists: compare_lists
# 4. Cycle detection: has_cycle

class LinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_new_head(self, node_data):
        current_head = self.head
        if not current_head:
            return
        new_head = LinkedListNode(node_data)
        new_head.next = current_head
        self.head = new_head

    def insert_node_at_end(self, node_data):
        new_node = LinkedListNode(node_data)
        if not self.head:
            self.head = new_node
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = new_node

    def insert_node_after_given_node(self, prev_node_data, node_data):
        current_node = self.head
        while current_node and current_node.data is not prev_node_data:
            current_node = current_node.next
        if not current_node:
            print(f'Given node data:{prev_node_data} was not found in this linked list.')
            return
        new_node = LinkedListNode(node_data)
        new_node.next = current_node.next
        current_node.next = new_node

    def delete_node(self, node_data):
        current_node = self.head
        if current_node.data == node_data:
            self.head = current_node.next
        else:
            while current_node and current_node.next:
                if current_node.next.data == node_data:
                    break
                current_node = current_node.next
            if not current_node or not current_node.next:
                print(f'Given node data:{node_data} was not found in this linked list.')
                return
            delete_node = current_node.next
            current_node.next = delete_node.next

    def print_linked_list(self):
        node = self.head
        if node is not None:
            while node:
                print(node.data, end=' -> ')
                node = node.next
            print('null')


linked_list = LinkedList()
linked_list.insert_node_at_end(1)
linked_list.insert_node_at_end(2)
linked_list.insert_node_at_end(3)
linked_list.insert_node_at_end(4)
linked_list.insert_new_head(0)
linked_list.insert_node_after_given_node(1, 2.5)
linked_list.print_linked_list()
linked_list.delete_node(0)
print('Linked List after delete operation:')
linked_list.print_linked_list()


def print_reverse_linked_list(node):
    if not node:
        return
    print_reverse_linked_list(node.next)
    print(node.data)


def reverse_linked_list(head, acc=None):
    if not head:
        return acc
    next_node = head.next
    head.next = acc
    return reverse_linked_list(next_node, head)


def reverse_linked_list_iterative(head):
    prev_node = None
    while head:
        next_node = head.next
        head.next = prev_node
        prev_node = head
        head = next_node
    return prev_node


def print_linked_list(head):
    while head:
        print(head.data, end=' -> ')
        head = head.next
    print('null')


print('Linked List after recursive reverse operation:')
reversed_head = reverse_linked_list(linked_list.head)
print_linked_list(reversed_head)
print('Linked List after iterative reverse operation:')
reversed_head_iterative = reverse_linked_list_iterative(reversed_head)
print_linked_list(reversed_head_iterative)


def compare_lists(llist1, llist2):
    while llist1 and llist2:
        if llist1.data != llist2.data:
            return 0
        llist1 = llist1.next
        llist2 = llist2.next
    if llist1 or llist2:
        return 0
    return 1


# Two-pointer method solution (AKA Floyd's Tortoise and Hare Algorithm)
def has_cycle(head):
    if not head or not head.next:
        return 0
    slow = head
    fast = head.next
    while slow != fast:
        if not fast or not fast.next:
            return 0
        slow = slow.next
        fast = fast.next.next
    return 1

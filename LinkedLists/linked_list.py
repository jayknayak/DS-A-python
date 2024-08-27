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
linked_list.print_linked_list()


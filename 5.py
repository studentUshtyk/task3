class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_node(node):
    
    node.val = node.next.val
    node.next = node.next.next

def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


head = ListNode(4)
node_to_delete = ListNode(5)
head.next = node_to_delete
head.next.next = ListNode(1)
head.next.next.next = ListNode(9)


delete_node(node_to_delete)

print_list(head) 

head2 = ListNode(4)
head2.next = ListNode(5)
node_to_delete2 = head2.next.next = ListNode(1)
head2.next.next.next = ListNode(9)

delete_node(node_to_delete2)

print_list(head2)

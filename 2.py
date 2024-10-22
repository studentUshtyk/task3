class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_duplicates(head):
    if not head:
        return head
    
    current = head
    

    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    
    return head

def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

head1 = ListNode(1, ListNode(1, ListNode(2)))

new_head1 = delete_duplicates(head1)

print_list(new_head1) 

head2 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))

new_head2 = delete_duplicates(head2)

print_list(new_head2)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorder_list(head):
    if not head or not head.next:
        return
    
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    first_half = head
    second_half = slow.next
    slow.next = None

    prev = None
    curr = second_half
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    second_half = prev  


    first_curr = first_half
    second_curr = second_half
    while second_curr:
   
        temp1 = first_curr.next
        temp2 = second_curr.next
        
      
        first_curr.next = second_curr
        second_curr.next = temp1
        
       
        first_curr = temp1
        second_curr = temp2


def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)

reorder_list(head1)
print_list(head1)  


head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = ListNode(3)
head2.next.next.next = ListNode(4)
head2.next.next.next.next = ListNode(5)

reorder_list(head2)
print_list(head2) 

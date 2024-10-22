class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def double_linked_list(head):

    digits = []
    current = head


    while current:
        digits.append(current.val)
        current = current.next
    
    carry = 0
    n = len(digits)

    for i in range(n - 1, -1, -1): 
        total = digits[i] * 2 + carry
        digits[i] = total % 10  
        carry = total // 10   


    if carry > 0:
        digits.insert(0, carry)


    new_head = None
    current = None

    for digit in digits:
        new_node = ListNode(digit)
        if new_head is None:
            new_head = new_node
            current = new_node
        else:
            current.next = new_node
            current = new_node

    return new_head

def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


head1 = ListNode(1)
head1.next = ListNode(8)
head1.next.next = ListNode(9)

result1 = double_linked_list(head1)
print("Результат для [1, 8, 9]:")
print_list(result1)  # Виведе: 3 -> 7 -> 8 -> None


head2 = ListNode(9)
head2.next = ListNode(9)
head2.next.next = ListNode(9)


result2 = double_linked_list(head2)
print("Результат для [9, 9, 9]:")
print_list(result2)  # Виведе: 1 -> 9 -> 9 -> 8 -> None

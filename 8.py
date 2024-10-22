class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_k_group(head, k):
    def reverse_linked_list(head, k):
        prev, curr = None, head
        while k > 0:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            k -= 1
        return prev

    dummy = ListNode(0) 
    dummy.next = head
    prev_group_end = dummy

    while True:
        kth_node = prev_group_end
        for _ in range(k):
            kth_node = kth_node.next
            if not kth_node:
                return dummy.next 
        
        group_start = prev_group_end.next
        next_group_start = kth_node.next

        kth_node.next = None
        reversed_group = reverse_linked_list(group_start, k)

        prev_group_end.next = reversed_group
        group_start.next = next_group_start

        prev_group_end = group_start

def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Приклад 1: head = [1, 2, 3, 4, 5], k = 2
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result = reverse_k_group(head, 2)
print("Результат для прикладу 1:")
print_list(result)  # Виведе: 2 -> 1 -> 4 -> 3 -> 5 -> None

# Приклад 2: head = [1, 2, 3, 4, 5], k = 3
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result = reverse_k_group(head, 3)
print("Результат для прикладу 2:")
print_list(result)  # Виведе: 3 -> 2 -> 1 -> 4 -> 5 -> None

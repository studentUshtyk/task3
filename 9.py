class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head: ListNode, x: int) -> ListNode:
    less_head = ListNode(0) 
    greater_head = ListNode(0)  
    less = less_head
    greater = greater_head

    current = head
    while current:
        if current.val < x:
            less.next = current
            less = less.next
        else:
            greater.next = current
            greater = greater.next
        current = current.next

    greater.next = None
    less.next = greater_head.next 

    return less_head.next

head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
x = 3

new_head = partition(head, x)

while new_head:
    print(new_head.val, end=" -> ")
    new_head = new_head.next
# Вивід: 1 -> 2 -> 2 -> 4 -> 3 -> 5 -> 

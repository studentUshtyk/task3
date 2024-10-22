class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    slow = head  # Повільний покажчик
    fast = head  # Швидкий покажчик

    while fast and fast.next:
        slow = slow.next          # повільний покажчик на один вузол
        fast = fast.next.next     # швидкий покажчик на два вузли

        if slow == fast:          # якщо вони зустрічаються, є цикл
            return True

    return False                 # якщо швидкий покажчик досягає кінця, циклу немає


def print_list(node):
    visited = set()
    while node:
        if node in visited:
            print("Cycle detected")
            return
        visited.add(node)
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# список з циклом: 3 -> 2 -> 0 -> -4
head1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

head1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # цикл, з'єднуючи -4 з 2

print(has_cycle(head1))

# список без циклу: 1 -> 2
head2 = ListNode(1)
head2.next = ListNode(2)

print(has_cycle(head2)) 

# Створюємо список з одним елементом без циклу: 1
head3 = ListNode(1)

print(has_cycle(head3))

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

def merge_k_lists(lists):
    min_heap = []
    
    for index, lst in enumerate(lists):
        if lst:  
            heapq.heappush(min_heap, lst)

    dummy = ListNode(0)
    current = dummy

    while min_heap:
        min_node = heapq.heappop(min_heap)
        current.next = min_node
        current = current.next
        
        if min_node.next:
            heapq.heappush(min_heap, min_node.next)

    return dummy.next

def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

list3 = ListNode(2)
list3.next = ListNode(6)

lists = [list1, list2, list3]
result = merge_k_lists(lists)
print("Результат для прикладу 1:")
print_list(result)  # Виведе: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6 -> None

result_empty = merge_k_lists([])
print("Результат для прикладу 2:")
print_list(result_empty)  # Виведе: None

list_empty = [None]
result_single_empty = merge_k_lists(list_empty)
print("Результат для прикладу 3:")
print_list(result_single_empty)  # Виведе: None

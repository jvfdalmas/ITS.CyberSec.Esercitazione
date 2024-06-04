class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverse_list(head: ListNode) -> list[int]:
    current = head
    risult = []
    risult.append(current.val)
    while current.next is not None:
        current = current.next
        risult.append(current.val)
    
    risult.reverse()
    return risult
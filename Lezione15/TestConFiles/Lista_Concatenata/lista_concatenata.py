class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, val):
        node = Node(val)

        if self.head == None:
            self.head = node
            return 
        else:
            curr = self.head

        while True:
            if curr.next == None:
                curr.next = node
                return
            else:
                curr = curr.next

    def print(self):
        curr = self.head

        while True:
            if curr != None:
                print(curr.val, " -> ", end="")
                curr = curr.next 
            else:
                print("None")
                break

linkedlist = LinkedList()
linkedlist.insert(0)
linkedlist.insert(1)
linkedlist.insert(2)
linkedlist.insert(3)
linkedlist.print()

def reversed_linked_list(node: Node) -> str: 
    curr = node
    if curr != None:
        helper = str(reversed_linked_list(curr.next)), " -> ", str(curr.val)
        return "".join(helper)
    
print(reversed_linked_list(linkedlist.head))



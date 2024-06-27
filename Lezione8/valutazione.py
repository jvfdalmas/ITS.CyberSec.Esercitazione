""" Question 1 -  Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

- push(x: int) -> None: Pushes element x to the top of the stack.
- pop() -> None Removes the element on the top of the stack and returns it.
- pop() -> None Returns the element on the top of the stack.
- empty() -> None Returns true if the stack is empty, false otherwise."""

print("Soluzione - Question 1:")

class Queue:
    def __init__(self):
        pass

class MyStack:
    def __init__(self):
        self.stack = []
    
    def push(self, x: int) -> None:
        self.stack.append(x) 
    
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]  
        else:
            return False  
    
    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()  
        else:
            return False  
            
    def empty(self) -> bool:
        return len(self.stack) == 0  
        
mystack = MyStack()
mystack.push(1)
mystack.push(2)
print(mystack.top())    # Output: 2
print(mystack.pop())    # Output: 2
print(mystack.empty())  # Output: False
print(mystack.pop())    # Output: 1
print(mystack.empty())  # Output: True

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

""""Question 2 - You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively. Write a function to merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n."""


print("Soluzione - Question 2:")

def merge(nums1, m, nums2, n):
    while 0 in nums1:
        nums1.remove(0)
        e = nums2.pop()
        nums1.append(e)
    nums1.sort()


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""Question 3 - Given a string s which consists of lowercase or uppercase letters, write a function that returns the length of the longest palindrome that can be built with those letters. Letters are case sensitive, for example, "Aa" is not considered a palindrome here."""

print("Soluzione - Question 3:")

def longest_palindrome(s: str) -> int:

    if len(s) == len(set(s)):
        return 1

    s = list(s)
    s.sort()
    counter = 0

    while len(s) > 0:
        e = s.pop()
        if len(s) > 0 and e == s[-1]:
            counter += 2
            s.pop()
        else:
            if len(s) == len(set(s)):
                return counter + 1
                
    return counter

print(longest_palindrome("abccccdd")) # 7
print(longest_palindrome("abccccba")) # 8
print(longest_palindrome("abcabcabc")) # 7

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

""" Question 4 - Given head, the head of a linked list, determine if the linked list has a cycle in it. There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter. Return true if there is a cycle in the linked list. Otherwise, return false.
 
Model the Node and Linked List concepts using classes."""

print("Soluzione - Question 4:")

class Node:
    
    def __init__(self, value, next = None):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def append(self, value):
        node = Node(value)
        
        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            
            while current_node.next:
                current_node = current_node.next

            current_node.next = node
            return
    
    def get_node(self, n):

        current_node = self.head

        while current_node:
            if current_node.value == n:
                return current_node
            else:
                current_node = current_node.next

        return None
        
def has_cycle(head: Node) -> bool:
    
    current_node = head
    memo = []
    
    while current_node:
        if current_node.next is None:
            return False
        else:
            if current_node in memo:
                return True
            else:
                memo.append(current_node)
                current_node = current_node.next

ll1 = LinkedList()
for i in range(5):
    ll1.append(i)

node1 = ll1.get_node(1)  # Node with value 1
node4 = ll1.get_node(4)  # Node with value 4

node4.next = node1  # Creating a cycle

print(has_cycle(ll1.head))

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

""" Question 5 - Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', write a function to determine if the input string is valid.

An input string is valid if: 

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type."""

print("Soluzione - Question 5:")

def is_valid_parenthesis(s: str) -> bool:
    if len(s) % 2 != 0:
        return False
    
    stack = []
    control = {'(': ')', '{': '}', '[': ']'}
    
    for char in s:
        if char in control:
            stack.append(char)
        else:
            if not stack or control[stack.pop()] != char:
                return False
    
    return len(stack) == 0
    
    
print(is_valid_parenthesis("()")) # True
print(is_valid_parenthesis("(]")) # False
print(is_valid_parenthesis("([)]")) # False
print(is_valid_parenthesis("()[]{}")) # True

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

""" Question 6 -  Given the head of a singly linked list, return true if it is a palindrome. Model the Node and Linked List concepts using classes."""

print("Soluzione - Question 6:")

class Node:

    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None
    
    def append(self, value):
        node = Node(value)

        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            return

def is_palindrome(head: Node) -> bool:
    memo: dict = {}
    current: Node = head
    counter: int = 0

    while current:
        if current.value in memo:
            memo[current.value] += 1
        else:
            memo[current.value] = 1
        current = current.next
    
    for value in memo.values():
        if value % 2 != 0:
            counter += 1

    if len(memo) % 2 != 0:
        if counter == 0 or counter == 1:
            return True
        else:
            return False
    else:
        if counter == 0:
            return True
        else:
            return False

    

ll1 = LinkedList()
for value in [1, 2, 3, 2, 1]:
    ll1.append(value)
print(is_palindrome(ll1.head))  # True

ll2 = LinkedList()
for value in [1, 2, 3, 4, 5]:
    ll2.append(value)
print(is_palindrome(ll2.head)) # False
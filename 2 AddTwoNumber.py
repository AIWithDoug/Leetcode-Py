# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total_sum = val1 + val2 + carry
            digit = total_sum % 10
            carry = total_sum // 10
            new_node = ListNode(digit)
            current.next = new_node
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy_head.next
    
# setup a dummy, a current to track to location as we cant jump to a certain index.
# and a carry so we know whats leftover.

# while we have digits left in l1, l2 or in the carry
# get the value from l1 and l2, if empty it has to be 0
# or it will try and add None which will error

# add them all together, % by 10 to get the left over.
# insert the new number (leftover) into the ListNode as a new
# number, set current.next to the new_node we just made to make
# sure it is the next in the list and not skipped

# repeat until the lists are done and return dummy_head.next
# we do that instead of just dummy_head, as its 0 by default
# we do not want that to be includedß
        
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        fast = slow = dummy
        # Creiamo una distanza di n+1
        for _ in range(n + 1):
            fast = fast.next
        # Spostiamo entrambi fino alla fine
        while fast:
            fast = fast.next
            slow = slow.next
        # Eliminiamo il nodo successivo a slow
        slow.next = slow.next.next
        # Restituiamo la nuova head
        return dummy.next

        

"""
  A linked list is given such that each node contains an additional 
  random pointer which could point to any node in the list or null.
  Return a deep copy of the list.
"""


# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head is None:
            return None
        
        # 1.iteration: copy each node and insert the new
        #   node to the original list in an alternative way
        p = head
        while p:
            originalNext = p.next
            p.next = RandomListNode(p.label)
            p.next.next = originalNext
            p = originalNext

        # the head of the copied list
        newHead = head.next
        
        # 2. iteration: copy the random link
        p = head
        while p:
            # copy the random pointer if it is not null
            if p.random:
                p.next.random = p.random.next
            originalNext = p.next.next
            p = originalNext
            
        # 3. iteration: restore the original order
        p = head
        while p:
            originalNext = p.next.next
            if originalNext:
                p.next.next = originalNext.next
            p.next = originalNext
            p = originalNext

        return newHead
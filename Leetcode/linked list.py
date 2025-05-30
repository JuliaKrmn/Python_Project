# https://leetcode.com/problems/add-two-numbers/description/


class ListNode(object):
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def __iter__(self):
        current = self.head
        while current:
            yield current.val
            current = current.next

# l1 = ListNode(val=2, next= ListNode(val= 4, next= ListNode(val= 3, next= None)))
# l2 = ListNode(val=5, next= ListNode(val= 6, next= ListNode(val= 4, next= None)))

# print(type(l1))

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)

for val in ll:
    print(val)


print(ll)
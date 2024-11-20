# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sorted_list = []
        pointer1 = list1
        pointer2 = list2

        if list1 == None and list2 == None:
            return None

        elif list1 != None and list2 == None:
            head_val = pointer1.val
            next_nodes = pointer1.next
            sorted_linked_list = ListNode(head_val, next_nodes)
            
            return sorted_linked_list

        elif list1 == None and list2 != None:
            head_val = pointer2.val
            next_nodes = pointer2.next
            sorted_linked_list = ListNode(head_val, next_nodes)
            
            return sorted_linked_list

        else:
            head = ListNode()
            current = head

            while list1 and list2:
                if list1.val < list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
                current = current.next


            current.next = list1 or list2

            return head.next

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
            while pointer1 != None:
                pointer2 = list2
                while pointer2 != None:
                    if pointer2.val <= pointer1.val:
                        sorted_list.append(pointer2.val)
                        list2 = list2.next
                    else:
                        break

                    pointer2 = pointer2.next

                sorted_list.append(pointer1.val)
                pointer1 = pointer1.next

            if pointer1 == None:
                while pointer2 != None:
                    sorted_list.append(pointer2.val)
                    pointer2 = pointer2.next
            
            if len(sorted_list) > 0:
                for i, elem in enumerate(sorted_list[-1::-1]):
                    if i == 0:
                        sorted_linked_list = ListNode(elem, None)
                    
                    else:
                        sorted_linked_list = ListNode(elem, previous_node)
                    previous_node = sorted_linked_list

            return sorted_linked_list


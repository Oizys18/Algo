"""
04/23/2021 17:49	Accepted	64 ms	14.5 MB	python3
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        anslist = ListNode()
        save = 0
        ans = anslist
        while l1 or l2:
            temp = 0
            if l1: temp += l1.val
            if l2: temp += l2.val
            if save: temp += save
            save = 0
            
            if temp > 9:
                save += 1 
                ans.val += temp%10
            else:
                ans.val += temp

            if l1.next or l2.next:
                if l1.next != None: 
                    l1 = l1.next
                else:
                    l1.val = 0
                if l2.next != None: 
                    l2 = l2.next
                else:
                    l2.val = 0
                ans.next = ListNode()
                ans = ans.next
            else:
                if save:
                    ans.next = ListNode()
                    ans = ans.next
                    ans.val = save
                break
            
        return anslist
        
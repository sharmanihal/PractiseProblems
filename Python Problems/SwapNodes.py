class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None :
            return head
        return self.solve(head,None)
    def solve(self,head:Optional[ListNode],prev)-> Optional[ListNode]:
        if head==None or head.next==None:
            return
        temp=head.next
        temp1= temp.next
        temp.next=head
        head.next=temp1
        if prev!=None:
            prev.next=temp
            prev=head
        else:
            prev=head
        head=temp
        self.solve(temp1,prev)
        return head

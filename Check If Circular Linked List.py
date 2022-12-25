'''Check If Circular Linked List'''
def isCircular(head):
   temp=head
   while 1:
       if temp==None:
           return 0
       temp=temp.next
       if temp==head:
           return 1

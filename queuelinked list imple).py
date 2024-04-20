class node:
   def __init__(self,data):
    self.data=data
    self.next=None

def enQueue(head,val):
    newblock=node(val)
    if head==None:
        return newblock

    tail=head
    while tail.next!=None:
        tail=tail.next
    tail.next=newblock
    return head 

def deQueue(head):
    if head==None:
        print("queue is empty,nothing to delete")
        return None

    
    print("deleting",head.data)
    secondnode=head.next
    head.next=None
    return secondnode

def printQueue(head):
    if head==None:
        print("Queue is empty")
        return
    curr=head
    while curr!=None:
        print(curr.data,end=" -->")
        curr=curr.next
    print()


head=None
head=enQueue(head,1)
head=enQueue(head,2)
head=enQueue(head,3)
head=enQueue(head,4)
head=enQueue(head,5)

printQueue(head)
head=deQueue(head)
printQueue(head)
head=deQueue(head)
printQueue(head)


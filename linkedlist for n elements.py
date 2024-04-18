class node:
    def __init__(self,data):
        self.data=data
        self.next=None


def printlinkedlist(head):
    curr=head
    while curr !=None:
        print(curr.data, end = " -->")
        curr=curr.next
    print()

def insertAtEndOfTail(head,ele):
    newblock=node(ele)
    if head==None:
        return newblock

    curr=head
    while curr.next!=None:
        curr=curr.next
    curr.next=newblock
    return head
A=[11,22,33,44,55,66,77,88,99,110]
head=None
for ele in A:
    head=insertAtEndOfTail(head,ele)
printlinkedlist(head)

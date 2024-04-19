class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
def printLeftToRightManner(head):
    print("Left to Right")
    curr=head
    while curr!=None:
        print(curr.data,end="-->")
        curr=curr.next
    print()
    
def printRightToLeftManner(tail):
    print("right to left")
    curr=tail
    while curr!=None:
        print(curr.data,end="-->")
        curr=curr.prev
    print()

obj1=node(121)
obj2=node(122)
obj3=node(123)
obj4=node(124)
obj5=node(125)


obj1.next=obj2
obj2.prev=obj1
obj2.next=obj3
obj3.prev=obj2
obj3.next=obj4
obj4.prev=obj3
obj4.next=obj5
obj5.prev=obj4

printLeftToRightManner(obj1)
printRightToLeftManner(obj5)





class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

obj1 = Node(5)
obj2 = Node(10)
obj3 = Node(15)
obj4 = Node(20)
obj5 = Node(25)
obj6 = Node(30)
obj1.next = obj2
obj2.next = obj3
obj3.next = obj4
obj4.next = obj5
obj5.next = obj6

curr=obj1
while curr !=None:
    print(curr.data,end="-->")
    curr=curr.next

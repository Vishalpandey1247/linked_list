class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Linkedlist:
    def __init__(self):
        self.head=None

    def print(self):
        if self.head==None:
            print("List is Empty!")

        i=self.head
        ll=""
        while i:
            ll += str(i.data) + "-->"
            i=i.next
        print(ll)

    def begin_with(self,data):
        node=Node(data,self.head)
        self.head=node

    def insert(self,data_list):
        self.data=None
        for data_ls in data_list:
            self.end_with(data_ls)
    
    def end_with(self,data):
        if self.head==None:
            self.head=Node(data,None)
            return

        i=self.head
        while i.next:
            i=i.next
        i.next=Node(data,None)            

    def length(self):
        count=0

        i=self.head
        while i.next:
            count += 1
            i=i.next
        print(count)

    def last_node(self):
        if self.head==None:
            return

        i=self.head
        while i:
            i=i.next
        print(i.data)

    def remove_by_index(self,index):
        if index==0:
            self.head=self.head.next
            return
        if index<0:
            raise Exception("Value Error")
        
        i = self.head
        number = 0
        while i.next:
            if number == index-1:
                i.next = i.next.next
            i = i.next
            number += 1

    def insert_at(self,index,data):
        if index < 0:
            raise Exception("Bad Input!")
        
        if index == 0:
            self.begin_with(data)

        i=self.head
        count=0
        while i.next:
            if count == index-1:
                i.next = Node(data,i.next.next)
            i=i.next
            count += 1

    def insert_after(self,data_before,data_after):
        if self.head== None:
            raise Exception("Bad Input")

        if self.head == data_before:
            self.head.next = Node(data_after,self.head.next)
            return

        i=self.head
        while i:
            if i.data==data_before:
                i.next=Node(data_after,i.next)
                break
            i=i.next

    def remove_by_name(self,data_to_remove):
        if self.head==None:
            raise Exception("Bad Input")

        if self.head.data==data_to_remove:
            self.head=self.head.next
            return

        i=self.head
        while i.next:
            if i.next.data==data_to_remove:
                i.next=i.next.next
            i=i.next

    def search(self,val):
        if self.head==None:
            raise Exception("Bad Input")

        i=self.head
        while i.next:
            if i.data==val:
                return True
            i=i.next
        return False


                
a=Linkedlist()
a.insert(["Shin-chan","Doraemon","Perman","Pokemon","Ninja Hatori"])
a.insert_at(4,"kiteretsu")
a.print()
a.remove_by_name("Ninja Hatori")
a.remove_by_index(2)
a.insert_after("Perman","Power Rangers")
print(a.search("Perman"))
print(a.length())
a.end_with("oggy and cockroches")
a.begin_with("Tom and Jarry")
a.print()






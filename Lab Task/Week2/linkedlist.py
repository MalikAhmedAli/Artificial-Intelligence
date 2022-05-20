from hashlib import new


class Node:
    def __init__(self, data=None):
        self.val = data
        self.next_node = None
        
        
class LinkedList:
    #constructor
    def __init__(self):
        self.head = None
    
    #push
    def push(self,data):
        new_node=Node(data)
    
        new_node.next_node=self.head
        self.head=new_node
    
    #pop
    def pop(self):
        temp = self.head
        while(temp.next_node.next_node != None):
            temp = temp.next_node
        temp.next_node = None
              
    
    #check linkedlist is empty or not
    def isEmpty(self):
        return self.head == None
    
    def size(self):
        count=0
        current = self.head
        while(current):
            count += 1
            current=current.next_node
        return count
    
    
    #Insertion 
    def insert(self,data,index):
        if(index==0):
            self.push(data)
        else:
            new=Node(data)
            position=index
            current=self.head
            while position >2 and current:
                current = current.next_node
                position -= 1
            if(position == 2 and current.next_node == None):
                current.next_node=new
                new.next_node=None
            elif(position > 1 and current.next_node != None):  
                prev=current
                next_node=current.next_node
                prev.next_node=new
                new.next_node=next_node  
 
    #Deletion
    def remove(self,key):
        current = self.head
        found=False
        previous=None
        while current and not found:
            if(current.val == key and current is self.head):
                found=True
                self.head=current.next_node
            elif(current.val==key):
                found=True
                previous.next_node=current.next_node
            else:
                previous=current
                current=current.next_node
        return current

#main
l1 =  LinkedList()
l1.push(10)
l1.push(20)
l1.insert(30,20)
l1.remove(20)
l1.remove(10)
print(l1.size())

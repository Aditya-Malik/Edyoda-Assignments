"""
Detect loop in a linked list.

Implement Linked list first in python. To test the detectLoop() method simulate a loop in a linked list like this - 

# Driver program for testing
llist = LinkedList()
llist.append(20)
llist.append(4)
llist.append(15)
llist.append(10)
 
# Create a loop for testing
llist.head.next.next.next.next = llist.head
"""
class Node:
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self):  
    self.head = None
    self.last = None

  #insert at last
  def append(self, new_data):
    new_node = Node(new_data)

    if self.head is None:
        self.head = new_node
        self.last = new_node
        return
    
    prev_node=self.last
    self.last=new_node
    prev_node.next=self.last

  def insertAfter(self, prev_node, new_data):

    if prev_node is None:
      print("The given previous node must be in LinkedList.")
      return

    new_node = Node(new_data)

    new_node.next = prev_node.next
    prev_node.next = new_node

  def insertAtStart(self, new_data):

    new_node=Node(new_data)

    if self.head is None:
      self.head=new_node
      self.last=self.head
      return
    
    next=self.head
    self.head=new_node
    self.head.next=next

  def deleteNode(self, key):
    if self.head is None:
        print("Linked List is empty")
        return

    temp = self.head
    prev = None
    found = False
    while(temp is not None):
        if temp.data == key:
            found = True
            break       
        prev = temp
        temp = temp.next

    if found:
        if self.last == temp:
          self.last = prev
          self.last.next = None
        prev.next = temp.next
        temp.data = None
        temp.next = None

  def length(self):
    temp = self.head
    count = 0
    while(temp != self.last.next):
      temp = temp.next
      count +=1

    return count

  def printLL(self):
    current = self.head
    while(current):
      print(current.data, end='=>')
      current = current.next

  def reverse(self):
    self.last=self.head
    prev = None
    current = self.head
    while(current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
    self.head = prev

  def detectloop(self):

    #To test loop, lets reference next attribute of last object to head object.
    #self.last.next=self.head.next
    current = self.head
    list = []
    loop = False

    while(current.next != None):
      list.append(current)
      current = current.next
      if current in list:
        loop = True
        break

    if loop == True:
      return print("Loop detected.")

    else:
      return print("No loop.")

if __name__=='__main__':

    llist = LinkedList()
    llist.append(20)
    llist.append(4)
    llist.append(15)
    llist.append(10)
    llist.detectloop()
    llist.head.next.next.next.next = llist.head
    llist.detectloop()
#Rotate an Linked list by one. Ex - if array is [1, 4, 6, 8, 7] Output will be [7, 1, 4, 6, 8]
class Node:
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self):  
    self.head = None

  def append(self, new_data):
    new_node = Node(new_data)

    if self.head is None:
        self.head = new_node
        return

    last = self.head
    while (last.next is not None):
      last = last.next

    last.next = new_node
  
  def insertAfter(self, prev_node, new_data):

    if prev_node is None:
      print("The given previous node must be in LinkedList.")
      return

    new_node = Node(new_data)

    new_node.next = prev_node.next

    prev_node.next = new_node

  def length(self):
    temp = self.head
    count = 0 
    while(temp is not None):
      temp = temp.next
      count +=1

    return count

  def printLL(self):
    current = self.head
    while(current):
      print(current.data, end='=>')
      current = current.next

  def rotateBy1(self):

    tail = self.head
    while(tail.next is not None):
        tail=tail.next
    
    prev = self.head
    while(prev.next is not tail):
        prev = prev.next
    
    tail.next = self.head
    prev.next = None
    self.head = tail

if __name__=='__main__':
  
    llist = LinkedList()
  
    llist.append(1)
    llist.append(4)
    llist.append(6)
    llist.append(8)
    llist.append(7)
    print("Original linkedlist: ")
    llist.printLL()
    llist.rotateBy1()
    print("\n\nRotated linked list by 1: ")
    llist.printLL()
    
class Node:  
  
    # Function to initialise the current object  
    def __init__(self, data):  
        self.data = data   
        self.next = None   
  
# Linked List class 
class LinkedList:  
  
    # Function to initialize head  
    def __init__(self):  
        self.head = None  
  
def Circular(head):  
    if head==None:  
        return True  
          
    # Next of head  
    current_node = head.next  
    i = 0  
      
    # This loop would stop in both cases (1) If  
    # Circular (2) Not circular  
    while((current_node is not None) and (current_node is not head)):  
        i = i + 1  
        current_node = current_node.next  
      
    return(current_node==head)  
  
  
node = LinkedList()  
node.head = Node(1)  
second =  Node(2)  
third =  Node(3)  
fourth = Node(4)  
  
node.head.next = second;  
second.next = third;  
third.next = fourth  
  
if (Circular(node.head)):  
    print('The given linked list is a circular list')  
else:  
    print('The given linked list is not a circular list')  
  
fourth.next = node.head  
  
if (Circular(node.head)):  
    print('The given linked list is a circular list')  
else:  
    print('The given linked list is not a circular list')  
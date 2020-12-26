
def Similarity_Compare(Object_1, Object_2):
    Blue_Diff = abs((Object_1.Blue_Proportion - Object_2.Blue_Proportion)/(Object_1.Blue_Proportion))*((Object_1.Blue_Proportion+Object_2.Blue_Proportion)/2)
    print("Weighted difference in object Blue color proportions is: ", Blue_Diff)
    Green_Diff = abs((Object_1.Green_Proportion - Object_2.Green_Proportion)/(Object_1.Green_Proportion))*((Object_1.Green_Proportion+Object_2.Green_Proportion)/2)
    print("Weighted difference in object Green color proportions is: ", Green_Diff)
    Red_Diff = abs((Object_1.Red_Proportion - Object_2.Red_Proportion)/(Object_1.Red_Proportion))*((Object_1.Red_Proportion+Object_2.Red_Proportion)/2)
    print("Weighted difference in object Red color proportions is: ", Red_Diff)
    Match_Percent = 1 - (Blue_Diff + Green_Diff + Red_Diff)
    return Match_Percent

class object():
    def __init__(self, Blue_Count, Green_Count, Red_Count):
        self.Blue_Count = Blue_Count
        self.Green_Count = Green_Count
        self.Red_Count = Red_Count
        self.Blue_Proportion = (Blue_Count)/(Blue_Count + Green_Count + Red_Count)
        self.Green_Proportion = (Green_Count)/(Blue_Count + Green_Count + Red_Count)
        self.Red_Proportion = (Red_Count)/(Blue_Count + Green_Count + Red_Count)

    def show(self):
        print("Object Blue Count is: ", self.Blue_Count, ", Proportion is: ", 100*self.Blue_Proportion, "%")
        print("Object Green Count is: ", self.Green_Count, ", Proportion is: ", 100*self.Green_Proportion, "%")
        print("Object Red Count is: ", self.Red_Count, ", Proportion is: ", 100*self.Red_Proportion, "%")

# A single node of a singly linked list
class Node:
  # constructor
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

# A Linked List class with a single head node
class LinkedList:
  def __init__(self):  
    self.head = None
  
  # insertion method for the linked list
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
  
    # This function is in LinkedList class. It inserts 
    # a new node at the beginning of Linked List. 
  def push(self, new_data): 
  
        # 1 & 2: Allocate the Node & 
        #     Put in the data 
        new_node = Node(new_data) 
  
        # 3. Make next of new Node as head 
        new_node.next = self.head 
  
        # 4. Move the head to point to new Node 
        self.head = new_node
  # print method for the linked list
  def printLL(self):
    current = self.head
    while(current):
      print(current.data.Red_Count)
      current = current.next

# Singly Linked List with insertion and print methods



Person_1 = object(1, 20, 3240)
Person_1.show()
Person_2 = object(15, 21, 3200)
Person_2.show()

LL = LinkedList()
LL.insert(Person_1)
LL.insert(Person_2)
LL.insert(Person_1)
LL.printLL()

LL.insert(Person_2)
LL.printLL()

A = {}

B = Person_1
C = Person_2

A[0] = Person_1
A[0].show()
A[1] = Person_2
A[1].show()
A[2] = object(491, 7, 82)
A[2].show()

Objects = []
Objects[0] = (10, 10, 20, 20)
Objects[1] = (50, 50, 100, 100)
Objects[2] = (25, 25, 200, 200)

for Object in Objects:




P1_P2_Similarity = Similarity_Compare(A[0], A[1])
print("Person 1 and Person 2 are ", 100*P1_P2_Similarity, "% similar...")

print("Hello world")
#execfile(Hello.py)
#execfile(Hello.py)

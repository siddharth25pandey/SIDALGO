class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

# Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
    # Insertion at the Begining
    def AtBegining(self,newdata):
        NewNode = Node(newdata)
        self.head = NewNode

# Update the new nodes next val to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode
    # Insertion at the End
    # Function to add newnode
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode
    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node Cannot be Added")
            return

        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

    # Removal/Deletion of a Node
    def RemoveNode(self, Removekey):
        HeadVal = self.head
        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.head = HeadVal.next
                HeadVal = None
                return
        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if (HeadVal == None):
            return

        prev.next = HeadVal.next

        HeadVal = None
list = SLinkedList()
def create(a):
    list.headval = Node(a)

def b_insert(a):
    list.AtBegining(a)
def e_insert(a):
    list.AtEnd(a)
def i_insert(a):
    list.Inbetween(list.headval.nextval,a)
def remove(a):
    list.RemoveNode(a)

def print_sll():
    list.listprint()
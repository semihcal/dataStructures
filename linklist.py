class Node:

    def __init__(self,d,n=None,p=None):

        self.data =d
        self.next_node =n
        self.prev_node =p #for doubly linked list

    def __str__ (self):
        return ('('+str(self.data)+')')



class LinkedList:

    def __init__(self,r=None):
        self.root =r
        self.size =0

    def add(self,d):
        new_node = Node(d,self.root)
        self.root = new_node
        self.size += 1

    def find(self,d):

        this_node = self.root

        while this_node is not None:
            if this_node.data == d:
                return d
            else:
               this_node = this_node.next_node

        return None

    def remove(self,d):
        this_node = self.root
        prev_node = None

        while this_node is not None:
            if this_node.data ==d:

                if prev_node is not None:
                    prev_node.next_node = this_node.next_node

                else: #data is in the root
                    self.root = this_node.next_node

                self.size -= 1

                return True # data removed!

            else:
                prev_node = this_node
                this_node = this_node.next_node

        return False #data not found

    def printList(self):
        this_node = self.root
        while this_node is not None:
            print(this_node, end = '->')
            this_node = this_node.next_node

        print('None')



ll = LinkedList()
for i in range(5,10):
    ll.add(i)
ll.printList()
print("size=",str(ll.size))
ll.remove(9)
print("size=",str(ll.size))
print(ll.find(8))
print(ll.root)
        


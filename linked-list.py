""" 
Linked lists should be preferred over arrays when:
- You know the data will grow and shrink frequently
- You need constant-time insertions/deletions from the list (such as in real-time computing where time predictability is absolutely critical)
- You don’t know how many items will be in the list. With arrays, you may need to re-declare and copy memory if the array grows too big
- You don’t need random access to any elements
- You want to be able to insert items in the middle of the list (such as a priority queue)

Dynamic Size: Linked lists can grow or shrink dynamically without the need for preallocation or resizing.

Constant-time Insertions/Deletions: Insertions and deletions at any position in a linked list can be done in constant time (O(1)) if you have a reference to the specific node.

Memory Efficiency: Linked lists can be memory-efficient in scenarios where elements have varying sizes or when you want to avoid preallocating large memory blocks.

No Wasted Space: Linked lists don't require preallocation, so you only use the memory needed for the elements you're actually storing.

No Shifting Overhead: Inserting or deleting elements in a linked list doesn't require shifting other elements, making these operations efficient.

Memory Fragmentation: Linked lists can help avoid memory fragmentation since elements can be allocated in non-contiguous memory locations.

Flexibility: Linked lists are flexible for storing elements of different data types or for handling relationships between elements.

Node Overhead: Linked lists have some overhead per node (for the data and the reference to the next node), which can make them less memory-efficient for storing individual small elements.
"""

class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None

    def get_data(self):
        return self.__data

    def set_data(self,data):
        self.__data=data

    def get_next(self):
        return self.__next

    def set_next(self,next_node):
        self.__next=next_node


class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail


    def add(self,data):
        new_node=Node(data)
        if(self.__head is None):
            self.__head=self.__tail=new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail=new_node

    def insert(self,data,data_before):
        new_node=Node(data)
        if(data_before==None):
            new_node.set_next(self.__head)
            self.__head=new_node
            if(new_node.get_next()==None):
                self.__tail=new_node

        else:
            node_before=self.find_node(data_before)
            if(node_before is not None):
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if(new_node.get_next() is None):
                    self.__tail=new_node
            else:
                print(data_before,"is not present in the Linked list")

    def display(self):
        temp=self.__head
        while(temp is not None):
            print(temp.get_data())
            temp=temp.get_next()


    def find_node(self,data):
        temp=self.__head
        while(temp is not None):
            if(temp.get_data()==data):
                return temp
            temp=temp.get_next()
        return None

    def delete(self,data):
        node=self.find_node(data)
        if(node is not None):
            if(node==self.__head):
                if(self.__head==self.__tail):
                    self.__tail=None
                self.__head=node.get_next()
            else:
                temp=self.__head
                while(temp is not None):
                    if(temp.get_next()==node):
                        temp.set_next(node.get_next())
                        if(node==self.__tail):
                            self.__tail=temp
                        node.set_next(None)
                        break
                    temp=temp.get_next()
        else:
            print(data,"is not present in Linked list")

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp=self.__head
        msg=[]
        while(temp is not None):
            msg.append(str(temp.get_data()))
            temp=temp.get_next()
        msg=" ".join(msg)
        msg="Linkedlist data(Head to Tail): "+ msg
        return msg

marias_lst=LinkedList()
marias_lst.add("Sugar")
print("Maria's list after adding Sugar:")
print(marias_lst)


marias_lst.add("Tea Bags")
marias_lst.add("Milk")
marias_lst.add("Biscuit")
print("\nMaria's list after adding three more items:")
print(marias_lst)

marias_lst.insert("Salt","Sugar")
print("\nMaria's list after inserting Salt after Sugar:")
print(marias_lst)


marias_lst.delete("Milk")
print("\nMaria's list after deleting Milk:")
print(marias_lst)

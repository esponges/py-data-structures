class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        # when initializing the top element of the stack is -1 (0 would be the first element)
        self.__top=-1

    def is_full(self):
        if(self.__top==self.__max_size-1):
            return True
        return False

    def push(self,data):
        if(self.is_full()):
            print("The stack is full!!")
        else:
            self.__top+=1
            self.__elements[self.__top]=data

    def get_max_size(self):
        return self.__max_size

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__top
        while(index>=0):
            msg.append((str)(self.__elements[index]))
            index-=1
        msg=" ".join(msg)
        msg="Stack data(Top to Bottom): "+msg
        return msg


stack1=Stack(5)
stack1.push("Shirt1")

print("Stack after adding one shirt:")
print(stack1)


#Push all the remaining shirts
stack1.push("Shirt2")
stack1.push("Shirt3")
stack1.push("Shirt4")
stack1.push("Shirt5")
print("\nStack after adding all the 5 shirts:")
print(stack1)

#Pop all the shirts from the stack in reverse order and observe the output
stack1.__str__()

#Push one more shirt to the stack and observe what happens
stack1.push("Shirt6")



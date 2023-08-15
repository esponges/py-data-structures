""" 
A stack is a linear data structure that follows the Last In First Out (LIFO) principle. 
This means that the last element added to the stack is the first one to be removed. 
Imagine a stack of plates: you can only remove the top plate, and to add a new plate, you place it on top. 
Stacks have a variety of applications in computer science, programming, and real-world scenarios. 

Here are some key features and concepts related to stacks:

- Function Calls: Many programming languages use a stack to manage function calls. When a function is called, its local variables and execution context are pushed onto the stack. When the function completes, its context is popped, and the program returns to the caller.
- Expression Evaluation: Stacks are used to evaluate expressions, like arithmetic or postfix expressions. They can help manage operator precedence and parentheses.
- Undo/Redo Operations: Stacks can be used to implement undo and redo functionalities in applications.
- Backtracking: In algorithms like depth-first search, stacks can be used to backtrack when certain conditions are met.
- Memory Management: Stacks play a role in managing memory allocation for local variables in programs.
"""
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
    
    def is_empty(self):
        if(self.__top==-1):
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
    
    def pop(self):
      if(self.is_empty()):
          print("The stack is empty!!")
      else:
        data=self.__elements[self.__top]
        self.__top-=1
        print("The popped element is:",data, " with index:", self.__top)
        return data

    def display(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            index=self.__top
            while(index>=0):
                print(self.__elements[index])
                index-=1

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

# pop last element
stack1.pop()
stack1.__str__()



class Stack:
    data=[]
    top=len(data)-1
    size=10

    def push(self,element):
        if(self.top==self.size-1):
            print("Stack is full! OVERFLOW!")
        else:
            self.top+=1
            self.data.append(element)
            print(self.data[self.top],"has entered the stack\n")
    
    def pop(self):
        if(self.top==-1):
            print("Stack is Empty! UNDERFLOW!")
        else:
            print(self.data[self.top]," has been popped\n")
            del self.data[self.top]
            self.top-=1
    
    def peek(self):
        print("Location of Top is : ",self.top+1)
        for i in range(self.top+1):
            print(self.data[i])
    
s=Stack()
while(1):
    print("Enter:\n 1:Push\n 2:Pop\n 3:Display Stack\n 4:Exit")
    i=int(input("Enter your choice : "))
    if (i==1):
        element=int(input("Enter element to push : "))
        s.push(element)
    elif (i==2):
        s.pop() 
    elif (i==3):
        s.show() 
    else:
        break; 
class Stack():
    def __init__(self,stan = []):
        self.status = stan

    def add(self,element):
        self.status.append(element)

    def get(self):
        if len(self.status) > 1:
            return self.status.pop()
        else:
            return "Stack is empty"

    def __str__(self):
         return str(self.status)

my_stack = Stack()
my_stack.add("tomek")
my_stack.add(True)
my_stack.add("Parzych")
my_stack.add(12)
print("drawn from the stack:",my_stack.get())
print("status:",my_stack.status)
print("my stack:",my_stack)

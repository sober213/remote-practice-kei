N = int(input())
command = []
value = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        value.append(int(line[1]))
    else:
        value.append(0)

# Please write your code here.
class Stack:
    def __init__ (self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.empty():
            raise Exception("Stack is empty")
        return self.items.pop()
    def size(self):
        return len(self.items)
    def empty(self):
        if len(self.items) == 0:
            return 1
        else:
            return 0
    def top(self):
        return self.items[-1]

s_1 = Stack()
for i in range(N):
    if command[i] == "push":
        s_1.push(value[i])
    elif command[i] == "size":
        print(s_1.size())
    elif command[i] == "empty":
        if s_1.empty() == 1:
            print(1)
        else:
            print(0)
    elif command[i] == "pop":
        print(s_1.pop())
    elif command[i] == "top":
        print(s_1.top())
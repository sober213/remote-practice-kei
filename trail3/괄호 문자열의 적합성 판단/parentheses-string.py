str = input()

# Please write your code here.
stack_1 = []
is_True = True
for char in str:
    if char == "(":
        stack_1.append(char)
    elif char == ")":
        if len(stack_1) == 0:
            is_True = False
        else:
            open_stack = stack_1.pop()
            open_stack
if len(stack_1) == 0 and is_True == True:
    print("Yes")
else:
    print("No")

            


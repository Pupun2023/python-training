a, b = map(int, input().split())
op = input()
match op:
    case '+': print(a + b)
    case '-': print(a - b)
    case '*': print(a * b)
    case '/': print(a / b)
    case '//': print(a // b)
    case '%': print(a % b) 
    case _:print("Invalid Symbol") 
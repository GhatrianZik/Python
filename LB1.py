
def X(a, b):
    if a < b:
        print("X == ", (a/b - 1) )
    elif a == b:
        print("X == ", -295)
    elif a > b:
        print("X == ", (a - 235)/b)

for v in range(3):

    print("Введи значение а: ")
    user_input_a = input()

    print("Введи значение b: ")
    user_input_b = input()

    X(int(user_input_a), int(user_input_b))
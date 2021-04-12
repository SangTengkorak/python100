# Variable for while loop
first_run = 0
second_run = 0

# Calculator functions
def calc_function(a, b, symbol):
    "Calculator functions"
    if symbol == "+":
        result = a + b
        return result

    elif symbol == "-":
        result = a - b
        return result

    elif symbol == "*":
        result = a * b
        return result

    elif symbol == "/":
        result = a / b
        return result

# Initial operation
while first_run == 0 :
    second_run = 0
    calc_operation = input("What operation you want to do?\n+\n-\n*\n/\nYour input : ")
    f_val = float(input("Input your first number : "))
    s_val = float(input(f"{calc_operation} Input your second number : "))

    calc_result = calc_function(a=f_val, b=s_val, symbol=calc_operation)
    print(f"{f_val} {calc_operation} {s_val} is : {calc_result}")

    # Continue with result from initial operation
    while second_run == 0:
        is_run = int(input("Do you want to process the previous result or start new?\n1. continue\n2. new operation\nYour input : "))
        if is_run == 1:
            calc_operation = input("What operation you want to do?\n+\n-\n*\n/\nYour input : ")
            new_val = float(input(f"{calc_operation} Input your new number : "))
            new_result = calc_function(a=calc_result, b=new_val, symbol=calc_operation)
            print(f"{calc_result} {calc_operation} {new_val} is : {new_result}")
            calc_result = new_result
        else:
            # Return to initial operation
            second_run += 1
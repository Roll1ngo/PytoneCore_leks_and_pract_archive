result = None
operand = None
operator = None
wait_for_number = True

while True:
    user_input = input(">>>")

    if user_input == "=":
        print(float(result))
        break

    if wait_for_number == True:
        try:
            operand = float(user_input)
            wait_for_number = False
        except ValueError:
            print(f"Sorry'{user_input}' it's not number, try again:")
            continue
    else:
        if (
            user_input == "+"
            or user_input == "-"
            or user_input == "/"
            or user_input == "*"
        ):
            operator = user_input
            wait_for_number = True
        else:
            print(f"'{user_input}' is not operator, try again: ")
            continue

    if result is None:
        result = operand
        operand = None
        continue

    if operator and operand:
        if operator == "+":
            result += operand

        if operator == "-":
            result -= operand

        if operator == "*":
            result *= operand

        if operator == "/":
            result /= operand

        operator = None
        operand = None

print("End")

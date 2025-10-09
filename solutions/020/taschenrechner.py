#! /usr/bin/env python3

def calculate():
    # handle the operator
    operator = input("> ")
    if operator != "+":
        # print("ERROR: Unknown operator.")
        return None

    # read in the operands
    numbers = []
    while True:
        text = input(">> ")
        if "" == text:
            break
        numbers.append(int(text))

    # calculate result
    if operator == "+":
        result = 0
        for number in numbers:
            result += number

    return result

if __name__ == "__main__":
    while result := calculate():
        print(result)
from typing import Tuple, Union

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."


def parse_input(str_input: str) -> Tuple[Union[float, None], Union[str, None], Union[float,None], Union[str, None]]:
    """
    check input and return the operands or an error if there is one
    """

    x, oper, y = str_input.split(' ')

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        return None, None, None, msg_1

    if oper not in '+-*/':
        return None, None, None, msg_2

    return x, oper, y, None


def calculate(first_number: float, oper: str, second_number: float) -> Tuple[Union[float,None], Union[str,None]]:

    if oper == '/' and second_number == 0:
        return None, msg_3

    if oper == '+':
        return first_number + second_number, None

    if oper == '-':
        return first_number - second_number, None

    if oper == '/':
        return first_number / second_number, None

    if oper == '*':
        return first_number * second_number, None


if __name__ == '__main__':
    while True:
        print(msg_0)
        first_number, oper, secon_number, error = parse_input( input())
        if error:
            print(error)
            continue

        result, error = calculate(first_number, oper, secon_number)
        if error:
            print(error)
            continue

        print(result)

        break


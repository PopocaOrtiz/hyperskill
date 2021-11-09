from typing import Union

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"


def check_input(str_input: str) -> Union[str, None]:
    """
    returns true if str_input is a valid operation with the structure:
    number operation number
    """

    x, oper, y = str_input.split(' ')

    try:
        x = float(x)
    except ValueError:
        return msg_1

    try:
        y = float(y)
    except ValueError:
        return msg_1

    if oper not in ['+', '-', '*', '/']:
        return msg_2

    return None


if __name__ == '__main__':
    while True:
        print(msg_0)
        error = check_input( input())
        if error:
            print(error)
        else:
            break


from typing import Tuple, Union

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_= {
    10: "Are you sure? It is only one digit! (y / n)",
    11: "Don't be silly! It's just one number! Add to the memory? (y / n)",
    12: "Last chance! Do you really want to embarrass yourself? (y / n)",
}

memory = 0.0


def parse_input(str_input: str) -> Tuple[Union[float, None], Union[str, None], Union[float,None], Union[str, None]]:
    """
    check input and return the operands or an error if there is one
    """

    x, oper, y = str_input.split(' ')

    if x == 'M':
        x = memory

    if y == 'M':
        y = memory

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


def is_one_digig(number: float) -> bool:
    return number == int(number) and -10 < number < 10


def check(v1, v2, v3):
    msg = ''
    if is_one_digig(v1) and is_one_digig(v2):
        msg += msg_6

    if v1 == 1 or v2 == 1 and v3 == '*':
        msg += msg_7

    if (v1 == 0 or v2 == 0) and (v3 in '*+-'):
        msg += msg_8

    if msg:
        msg = msg_9 + msg
        print(msg)


if __name__ == '__main__':

    while True:

        print(msg_0)

        first_number, oper, secon_number, error = parse_input( input())
        if error:
            print(error)
            continue

        check(first_number, secon_number, oper)
        result, error = calculate(first_number, oper, secon_number)
        if error:
            print(error)
            continue

        print(result)

        while True:

            print(msg_4)

            answer = input()

            if answer == 'y':

                if is_one_digig(result):

                    msg_index = 10

                    while True:

                        print(msg_[msg_index])

                        answer = input()

                        if answer == 'y':
                            if msg_index < 12:
                                msg_index += 1
                                continue
                            else:
                                memory = result
                                break
                        elif answer == 'n':
                            break
                        else:
                            continue
                else:
                    memory = result

                break
            elif answer == 'n':
                break

        while True:

            print(msg_5)

            answer = input()

            if answer == 'y':
                break
            elif answer == 'n':
                quit()

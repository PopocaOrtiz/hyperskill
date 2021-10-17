
"""
input: recibe a string with 9 characters wich are the state of the field, e.g.
XOXOXOXXO
XXXOO__O_
XO_OOX_X_
XO_XO_XOX

output: prints the field and the state of the game e.g.
Game not finished
X wins
O wins
They both lose
Impossible game
"""
symbols = input()
matriz = [[symbols[(row * 3) + col] for col in range(3)] for row in range(3)]


def print_row(row):
    print('|', row[0],row[1],row[2],'|')


def print_matriz():
    print('---------')
    [print_row(row) for row in matriz]
    print('---------')


def get_col(index):
    return [row[index] for row in matriz]


def three_in_a_row(search, row):
    return row.count(search) == 3


def three_in_matriz(search):
    amount_of_threes = 0

    # threes in rows
    for row in matriz:
        if three_in_a_row(search,row):
            amount_of_threes += 1

    # threes in cols
    for col_number in range(3):
        if three_in_a_row(search, get_col(col_number)):
            amount_of_threes += 1

    # diagonals
    if matriz[0][0] == matriz[1][1] == matriz[2][2] == search:
        amount_of_threes += 1

    if matriz[0][2] == matriz[1][1] == matriz[2][0] == search:
        amount_of_threes += 1

    return amount_of_threes


def impossible_amount_of_symbols():
    if abs(symbols.count('X') - symbols.count('O')) > 1:
        return True


def check_result():

    x_threes_in_a_row = three_in_matriz('X')
    o_threes_in_a_row = three_in_matriz('O')

    if impossible_amount_of_symbols():
        print('Impossible')
    elif x_threes_in_a_row and o_threes_in_a_row:
        print('Impossible')
    elif x_threes_in_a_row:
        print('X wins')
    elif o_threes_in_a_row:
        print('O wins')
    elif symbols.count('_'):
        print('Game not finished')
    else:
        print('Draw')


print_matriz()
check_result()

"""
First receive the field form the input(string with the state of the 9 cells)
Then it receive two coordinates, analice, make the move and print the field with the new state of the field

Enter cells: _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
Enter the coordinates: 4 1
Coordinates should be from 1 to 3!
Enter the coordinates: 1 4
Coordinates should be from 1 to 3!
Enter the coordinates: 1 1
---------
| X X X |
| O O   |
| O X   |
---------
"""

print('Enter cells:', end='')
symbols = input()
matriz = [[symbols[(row * 3) + col] for col in range(3)] for row in range(3)]


def print_row(row):
    print('|', row[0],row[1],row[2],'|')


def print_matriz():
    print('---------')
    [print_row(row) for row in matriz]
    print('---------')


def str_is_valid_number(letter):
    return letter in "0123456789"


def is_valid_corrdinate(coordinate):
    return coordinate in ["1","2","3"]


def input_has_errors(input):

    x, y = input.split()

    if not (str_is_valid_number(x) and str_is_valid_number(y)):
        return 'You should enter numbers!'

    if not (is_valid_corrdinate(x) and is_valid_corrdinate(y)):
        return 'Coordinates should be from 1 to 3!'

    if not matriz[int(x)-1][int(y)-1] == '_':
        return 'This cell is occupied! Choose another one!'

    return None


print_matriz()

input_error = True

while input_error:

    print('Enter the coordinates:', end='')

    coordinates = input()

    input_error = input_has_errors(coordinates)

    if input_error:
        print(input_error)
    else:
        x, y = [int(coor) - 1 for coor in coordinates.split()]
        matriz[x][y] = 'X'
        print_matriz()

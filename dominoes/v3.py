import random


def create_pieces():
    pieces = [[i, j] for i in range(7) for j in range(i, 7)]
    random.shuffle(pieces)
    return pieces


def create_game(original_pieces):

    players = {
        'computer': [],
        'player': [],
    }

    begin_piece = None
    index_begin_piece = None
    player_begin_piece = None

    for name_player in players:

        for index_piece in range(7):

            piece = original_pieces.pop(0)

            players[name_player].append(piece)

            if piece[0] != piece[1]:  # arent twins
                continue

            if not begin_piece or (piece[0] > begin_piece[0]):
                begin_piece = piece
                index_begin_piece = index_piece
                player_begin_piece = name_player

    domino_snake = []
    if begin_piece:
        players[player_begin_piece].pop(index_begin_piece)
        domino_snake.append(begin_piece)

    player_start_game = 'computer' if player_begin_piece == 'player' else 'player'

    return players, domino_snake, player_start_game


class Game:
    def __init__(self, players, snake, next_player, stock_pieces):
        self.players = players
        self.snake = snake
        self.next_player = next_player
        self.stock_pieces = stock_pieces

    def print_game(self):
        print("=" * 70)

        print('Stock size:', len(self.stock_pieces))
        print('Computer pieces:', len(self.players['computer']))

        print_snake(self.snake)
        print('Your pieces:')
        for i, piece in enumerate(self.players['player']):
            print(f'{i + 1}:{piece}')

        if self.next_player == 'computer':
            msg_status = 'Computer is about to make a move. Press Enter to continue...'
        else:
            msg_status = "It's your turn to make a move. Enter your command."

        print()
        print('Status:', msg_status)

    def input_is_valid(self, in_player: str):

        if not in_player.isdigit():
            return False

        number = abs(int(in_player))

        if number > len(self.players['player']):
            return False

        return True

    def apply_move(self, player, piece):
        if piece > 0:
            self.snake.append(self.players[player].pop(abs(piece) - 1))
        elif piece < 0:
            new_snake = [self.players[player].pop(abs(piece) - 1)] + self.snake
            self.snake = new_snake
        else:
            self.players[player].append(self.stock_pieces.pop())

    def check_result(self):

        if not len(self.players['player']):
            return 'player'

        if not len(self.players['computer']):
            return 'computer'

        first = self.snake[0][0]
        last = self.snake[-1][1]

        if first == last:
            repetitions = 0
            for piece in self.snake:

                if piece[0] == first:
                    repetitions += 1

                if piece[1] == first:
                    repetitions += 1

            if repetitions == 8:
                return 'draw'

        return None

    def print_result(self, result):
        results = {
            'player': 'The game is over. You won!',
            'computer': 'The game is over. The computer won!',
            'draw': 'The game is over. It\'s a draw!',
        }
        print(results[result])


def print_snake(pieces):

    print()
    if len(pieces) < 7:
        print(*pieces, sep='')
    else:
        print(*pieces[:3], '...', *pieces[-3:], sep='')
    print()


def start_game():

    stock_pieces = create_pieces()
    players, domino_snake, player_start_game = create_game(stock_pieces)

    if not player_start_game:
        return None

    return Game(players, domino_snake, player_start_game, stock_pieces)


while True:
    game = start_game()
    if game:
        break

while True:
    game.print_game()

    if game.next_player == 'player':

        while True:
            player_input = input()
            if game.input_is_valid(player_input):
                break
            else:
                print('Invalid input. Please try again.')

        player_input = int(player_input)

        game.apply_move('player', player_input)

        game.next_player = 'computer'

    else:
        input()
        game.apply_move('computer', 1)

        game.next_player = 'player'

    result = game.check_result()

    if result:
        game.print_result(result)
        break

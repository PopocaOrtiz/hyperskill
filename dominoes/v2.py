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


def start_game():

    stock_pieces = create_pieces()
    players, domino_snake, player_start_game = create_game(stock_pieces)

    if not player_start_game:
        return False

    print_game(domino_snake, player_start_game, players, stock_pieces)

    return True


def print_game(domino_snake, player_start_game, players, stock_pieces):

    print("=" * 70)

    print('Stock size:', len(stock_pieces))
    print('Computer pieces:', len(players['computer']))

    print()
    for piece in domino_snake:
        print(piece)
    print()

    print('Your pieces:')
    for i, piece in enumerate(players['player']):
        print(f'{i+1}:{piece}')

    if player_start_game == 'computer':
        msg_status = 'Status: Computer is about to make a move. Press Enter to continue...'
    else:
        msg_status = "Status: It's your turn to make a move. Enter your command."

    print()
    print('Status:', msg_status)


while True:
    game_started = start_game()
    if game_started:
        break

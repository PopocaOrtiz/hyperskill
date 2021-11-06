import random


class Game:

    def __init__(self):

        try:
            pieces = self.create_pieces()
            begin_fields = self.create_game(pieces)

            self.players = begin_fields['players']
            self.snake = begin_fields['snake']
            self.next_player = begin_fields['player_next_move']
            self.stock_pieces = begin_fields['stock_pieces']
        except:
            self.__init__()

    @staticmethod
    def create_pieces():
        pieces = [[i, j] for i in range(7) for j in range(i, 7)]
        random.shuffle(pieces)
        return pieces

    @staticmethod
    def create_game(original_pieces):

        """
        assign the pieces and find the biggest twin
        :param original_pieces:
        :return:
        """

        players = {
            'computer': [],
            'player': [],
        }

        begin_piece = None
        index_begin_piece = None
        player_begin_piece = None

        for name_player in players:

            for index_piece in range(7):

                piece = original_pieces.pop()

                players[name_player].append(piece)

                if piece[0] != piece[1]:
                    continue  # arent twins

                if not begin_piece or (piece[0] > begin_piece[0]):
                    # there is not begin piece or this piece is bigger than the current twin
                    begin_piece = piece
                    index_begin_piece = index_piece
                    player_begin_piece = name_player

        players[player_begin_piece].pop(index_begin_piece)
        snake = [begin_piece]

        player_start_game = 'computer' if player_begin_piece == 'player' else 'player'

        return {
            'players': players,
            'snake': snake,
            'player_next_move': player_start_game,
            'stock_pieces': original_pieces
        }

    def print_snake(self):

        print()
        if len(self.snake) < 7:
            print(*self.snake, sep='')
        else:  # print the first 3 and the last 3
            print(*self.snake[:3], '...', *self.snake[-3:], sep='')
        print()

    def print_game(self):
        print("=" * 70)

        print('Stock size:', len(self.stock_pieces))
        print('Computer pieces:', len(self.players['computer']))

        self.print_snake()
        print('Your pieces:')
        for i, piece in enumerate(self.players['player']):
            print(f'{i + 1}:{piece}')

        if self.next_player == 'computer':
            msg_status = 'Computer is about to make a move. Press Enter to continue...'
        else:
            msg_status = "It's your turn to make a move. Enter your command."

        print()
        print('Status:', msg_status)

    def input_is_valid(self, input_player: str, name_player: str):

        if not input_player.lstrip("-").isdigit():
            return False

        number = abs(int(input_player))

        if number > len(self.players[name_player]):  # bigger than the current pieces
            return False

        return True

    def is_legal_move(self, input_number: int, player: str):
        """
        a move is legal if is 0 or
        the piece can be place in the left(<0) or the right(>0)
        :param input_number:
        :param player:
        :return:
        """

        if not input_number:  # 0 is always legal
            return True

        first = self.snake[0]
        last = self.snake[-1]

        piece = self.players[player][abs(input_number) - 1]

        if input_number < 1 and first[0] == piece[0] or first[0] == piece[1]:
            return True

        if input_number > 1 and last[1] == piece[0] or last[1] == piece[1]:
            return True

        return False

    def apply_move(self, input_number: int, player: str):
        """
        take a piece from the stock or
        take a piece from the player and put it in the snake
        swift the piece if necesary
        """

        if not input_number:
            if not len(self.stock_pieces):
                return False

            self.players[player].append(self.stock_pieces.pop())
            return True

        piece = self.players[player].pop(abs(input_number) - 1)

        if input_number > 0:
            if not self.snake[-1][1] == piece[0]:
                piece[0], piece[1] = piece[1], piece[0]
            self.snake.append(piece)
            return False

        if input_number < 0:
            if not self.snake[0][0] == piece[1]:
                piece[0], piece[1] = piece[1], piece[0]
            self.snake = [piece] + self.snake
            return False

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

    @staticmethod
    def print_result(result):
        results = {
            'player': 'The game is over. You won!',
            'computer': 'The game is over. The computer won!',
            'draw': 'The game is over. It\'s a draw!',
        }
        print(results[result])

    def calculate_repetitions(self):
        repetitions = {
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
        }

        for piece in self.players['computer']:
            repetitions[piece[0]] += 1
            repetitions[piece[1]] += 1

        return repetitions

    def get_index_pieces_orderer_by_min_core(self):

        repetitions = self.calculate_repetitions()

        index_pieces = []

        computer_pieces = self.players['computer']

        for i, piece in enumerate(computer_pieces):

            if not index_pieces:
                index_pieces.append(i)
                continue

            score = repetitions[piece[0]] + repetitions[piece[1]]

            piece_placed = False
            for index_order in index_pieces:

                piece_ordered = computer_pieces[index_order]

                score_from_ordered_piece = repetitions[piece_ordered[0]] + repetitions[piece_ordered[1]]

                if score < score_from_ordered_piece:
                    index_pieces.insert(index_order, i)
                    piece_placed = True
                    break

            if not piece_placed:  # is the biggest
                index_pieces.append(i)

        return index_pieces


game = Game()

while True:

    game.print_game()

    if game.next_player == 'player':

        fixed_input = None

        while True:

            player_input = input()

            if not game.input_is_valid(player_input, 'player'):
                print('Invalid input. Please try again.')
                continue

            player_input = int(player_input)

            if not game.is_legal_move(player_input, 'player'):
                print('Illegal move. Please try again.')
                continue

            break

        move_maked = game.apply_move(player_input, 'player')
        game.next_player = 'computer'

        if not move_maked:
            game_finished = 'draw'
            break

    else:

        input()

        computer_input = 0  # by default it takes a piece from the stock

        # for index_computer_piece in range(len(game.players['computer'])):
        for index_computer_piece in game.get_index_pieces_orderer_by_min_core():

            if game.is_legal_move(index_computer_piece + 1, 'computer'):
                computer_input = index_computer_piece
                break
            elif game.is_legal_move(-(index_computer_piece + 1), 'computer'):
                computer_input = -(index_computer_piece + 1)
                break

        move_maked = game.apply_move(computer_input, 'computer')
        game.next_player = 'player'

        if not move_maked:
            game_finished = 'draw'
            break

    game_finished = game.check_result()

    if game_finished:
        break

game.print_result(game_finished)

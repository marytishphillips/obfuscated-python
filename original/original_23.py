class ChessBoard:
    def __init__(self):
        self.board = self.create_board()
        self.turn = 'white'  # 'white' starts first

    def create_board(self):
        # Unicode symbols for the chess pieces
        board = [
            ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
            ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
            ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
        ]
        return board

    def print_board(self):
        # Print top label for Player 1 side
        print('      Player 1')
        print('  a b c d e f g h')

        # Print rows with side labels
        for i, row in enumerate(self.board):
            # Print row number and left side label
            print(f'{8 - i} ', end='')
            # Print row content
            for piece in row:
                print(piece, end=' ')
            # Print right side label
            print(f'{8 - i}')

        # Print bottom label for Player 2 side
        print('  a b c d e f g h')
        print('      Player 2\n')

    def move_piece(self, start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        piece = self.board[start_row][start_col]
        self.board[start_row][start_col] = '.'
        self.board[end_row][end_col] = piece

        # Toggle turn
        self.turn = 'black' if self.turn == 'white' else 'white'

def parse_position(pos):
    col, row = pos
    return 8 - int(row), ord(col) - ord('a')

def main():
    chess_board = ChessBoard()
    chess_board.print_board()

    while True:
        player = 'Player 1' if chess_board.turn == 'white' else 'Player 2'
        start_pos = input(f"{player}, enter the start position (e.g., 'e2'): ")
        end_pos = input(f"{player}, enter the end position (e.g., 'e4'): ")

        start_pos = parse_position(start_pos)
        end_pos = parse_position(end_pos)

        chess_board.move_piece(start_pos, end_pos)
        chess_board.print_board()

if __name__ == "__main__":
    main()

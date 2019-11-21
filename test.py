import chess
import chess.polyglot
board = chess.Board('rnbqkbnr/pppppppp/8/8/P7/8/1PPPPPPP/RNBQKBNR b KQkq -')
#
# board.push(chess.Move.from_uci("e2e4"))
book_moves = []
with chess.polyglot.open_reader("book.bin") as reader:
    print(len(reader))
    for entry in reader.find_all(board):
        print(entry.move, entry.weight, entry.learn)
        book_moves.append(str(entry.move))
        if len(book_moves) == 3:
            break

print(book_moves)
print(board)
print(board.fen())

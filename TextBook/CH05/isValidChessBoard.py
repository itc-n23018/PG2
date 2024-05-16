def is_valid_chess_board(board):
    piece_count = {
        'wking': 0, 'wqueen': 0, 'wrook': 0, 'wbishop': 0, 'wknight': 0, 'wpawn': 0,
        'bking': 0, 'bqueen': 0, 'brook': 0, 'bbishop': 0, 'bknight': 0, 'bpawn': 0
    }
    
    for position, piece in board.items():
        if position[0] not in '12345678' or position[1] not in 'abcdefgh':
            return False
        if piece not in piece_count:
            return False
        piece_count[piece] += 1
    
    if piece_count['wking'] != 1 or piece_count['bking'] != 1:
        return False
    
    if piece_count['wpawn'] > 8 or piece_count['bpawn'] > 8:
        return False
    
    if sum(piece_count.values()) > 32:
        return False
    
    return True

board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(is_valid_chess_board(board))  


import random
board = [" " for x in range(10)]


def insert_letter(letter, position):
    board[position] = letter


def is_free(pos):
    return board[pos] == " "


def print_board(board):
    print("   |   |   ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |   ")


def is_winner(board, letter):
    return((board[1] == letter and board[2] == letter and board[3] == letter) or
           (board[4] == letter and board[5] == letter and board[6] == letter) or
           (board[7] == letter and board[8] == letter and board[9] == letter) or
           (board[1] == letter and board[4] == letter and board[7] == letter) or
           (board[2] == letter and board[5] == letter and board[8] == letter) or
           (board[3] == letter and board[6] == letter and board[9] == letter))


def is_full(board):
    if board.count(" ") > 1:
        return False
    else:
        return True


def player_move():
    run = True
    while run:
        move = input("Please, Enter Your Move And It Should Be Between 1-9 Ok! >>")
        try:
            move = int(move)
            if 0 < move < 10:
                if is_free(move):
                    run = False
                    insert_letter("X", move)
                else:
                    print("This Place Is Already Full.")
            else:
                print("please, Choose Number between 1-9 ok.")
        except:
            print("You Should Give Number nothing else ok.")


def comp_move():
    possible_moves = [x for x, letter in enumerate(board) if letter == " " and x != 0]
    move = 0
    for let in ["O", "X"]:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = let
            if is_winner(board_copy, let):
                move = i
                return move
    open_corners = []
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            open_corners.append(i)
    if len(open_corners) > 0:
        move = select_random(open_corners)
    if 5 in possible_moves:
        move = 5
        return move
    open_edges = []
    for i in possible_moves:
        if i in [2, 4, 8, 6]:
            open_edges.append(i)
    if len(open_edges) > 0:
        move = select_random(open_edges)
    return move


def select_random(list):
    ln = len(list)
    ran = random.randrange(0, ln)
    return list[ran]


def main():
    print("Hi Dude Welcome To Tic Tac Toe Game Let's Get Started!👍")
    print_board(board)
    while not (is_full(board)):
        if not(is_winner(board, "O")):
            player_move()
            print_board(board)
        else:
            print("Sorry, The Comp(O) has Won The Game :(")
            break
        if not (is_winner(board, "X")):
            move = comp_move()
            if move == 0:
                print("End!")
            else:
                insert_letter("O", move)
                print("Comp(O) Placed His Move.")
                print_board(board)
        else:
            print("Hiiiii, You Have Won The Game :)")
            break
        if is_full(board):
            print("End.")


main()

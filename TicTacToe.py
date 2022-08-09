import random


def display_board(board):
    print(" " + board[1] + " " + "|" + " " +
          board[2] + " " + "|" + " " + board[3] + " ")
    print("-----------")
    print(" " + board[4] + " " + "|" + " " +
          board[5] + " " + "|" + " " + board[6] + " ")
    print("-----------")
    print(" " + board[7] + " " + "|" + " " +
          board[8] + " " + "|" + " " + board[9] + " ")


def player_input():

    player1 = ''
    player2 = ''
    checkValues = ['X', 'O']

    while player1 not in checkValues:

        if player1 not in checkValues:
            player1 = input("Player 1, please select your sign: (X or O): ")

        if player1 == 'X':
            player2 = 'O'

        if player1 == 'O':
            player2 = 'X'

        if player1 not in checkValues:
            print("Please select a proper sign.")

    return [player1, player2]


def place_marker(board, marker, position):

    board[position] = marker

    display_board(board)


def win_check(board, mark):

    win = False

    if (board[1] == mark) and (board[2] == mark) and (board[3] == mark):
        win = True
        return win
    if (board[4] == mark) and (board[5] == mark) and (board[6] == mark):
        win = True
        return win
    if (board[7] == mark) and (board[8] == mark) and (board[9] == mark):
        win = True
        return win
    if (board[1] == mark) and (board[4] == mark) and (board[7] == mark):
        win = True
        return win
    if (board[2] == mark) and (board[5] == mark) and (board[8] == mark):
        win = True
        return win
    if (board[3] == mark) and (board[6] == mark) and (board[9] == mark):
        win = True
        return win
    if (board[1] == mark) and (board[5] == mark) and (board[9] == mark):
        win = True
        return win
    if (board[3] == mark) and (board[5] == mark) and (board[7] == mark):
        win = True
        return win

    return win


def choose_first():

    if random.randint(0, 10) % 2 == 0:
        return True
    else:
        return False


def space_check(board, position):

    if board[position] == ' ':
        return True
    else:
        return False


def full_board_check(board):

    if ' ' not in board:
        return True
    else:
        return False


def player_choice(board):

    appValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    choiceValue = 11

    while choiceValue not in appValues:

        if choiceValue not in appValues:
            choiceValue = int(
                input("Please select your next position number: "))
            spotCheck = space_check(board, choiceValue)

        if spotCheck == False:
            print("Sorry, that spot is already taken.")
            choiceValue = 11

        else:
            return choiceValue


def replay():

    appValues = ['Y', 'N']
    playAgain = input("Would you like to play again? (Y or N): ")

    if playAgain == 'Y':
        return True
    if playAgain == 'N':
        return False
    if playAgain not in appValues:
        print("Sorry, I didn't understand. Please enter 'Y' or 'N'.")


print('Welcome to Tic Tac Toe!')

play = True
while play:
    # Set the game up here
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    display_board(board)

    playerSigns = player_input()
    player1Sign = playerSigns[0]
    player2Sign = playerSigns[1]

    firstMove = choose_first()

    while play:
        # Player 1 Moves First
        if firstMove:
            # Player 1 moves
            player1Choice = player_choice(board)
            board[player1Choice] = player1Sign
            display_board(board)

            if win_check(board, player1Sign):
                print("Player 1 has won the game!")
                play = replay()
                break

            if full_board_check(board):
                print("Board has been filled and there are no winners!")
                play = replay()
                break
            # Player 2 moves
            player2Choice = player_choice(board)
            board[player2Choice] = player2Sign
            display_board(board)

            if win_check(board, player2Sign):
                print("Player 2 has won the game!")
                play = replay()
                break

            if full_board_check(board):
                print("Board has been filled and there are no winners!")
                play = replay()
                break

        # Player 2 Moves First.
        else:
            # Player 2 moves
            player2Choice = player_choice(board)
            board[player2Choice] = player2Sign
            display_board(board)

            if win_check(board, player2Sign):
                print("Player 2 has won the game!")
                play = replay()
                break

            if full_board_check(board):
                print("Board has been filled and there are no winners!")
                play = replay()
                break
            # Player 1 moves
            player1Choice = player_choice(board)
            board[player1Choice] = player1Sign
            display_board(board)

            if win_check(board, player1Sign):
                print("Player 1 has won the game!")
                play = replay()
                break

            if full_board_check(board):
                print("Board has been filled and there are no winners!")
                play = replay()
                break

    if not play:
        break

print("Thanks for playing!")

def welcome():
    print("-------------------")
    print("       Игра        ")
    print(' "Крестики-нолики" ')
    print("-------------------")


def show_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-" * 13)

def wincon(board):
    win_line = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for symbol in win_line:
        if board[symbol[0]] == board[symbol[1]] == board[symbol[2]]:
            show_board(board)
            print(f"{board[symbol[0]]} победил! Поздравляю!")
            return True
    return False

def player_move(symbol):
    while True:
        cell = input(f"Выберите ячейку, {symbol}: ")
        if cell.isdigit():
            cell = int(cell)
            if cell >= 1 and cell <= 9:
                if (str(board[cell-1]) not in "XO"):
                    board[cell-1] = symbol
                    return
                else:
                    print("Клетка занята!")
            else:
                print ("Номера клеток от 1 до 9.")
        else:
            print("Неправильный ввод.Введите число от 1 до 9.")

welcome()
board = list(range(1,10))
count = 0
while True:
    show_board(board)
    if count % 2 == 0:
        player_move("X")
    else:
        player_move("O")
    count += 1
    if wincon(board):
        break
    if count == 9:
        print("Ничья!")
        break

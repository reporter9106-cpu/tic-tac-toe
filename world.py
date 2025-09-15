def print_board(board):
    """
    This function correctly displays the matrix that we are
    passing to it in the form of a 3x3 playing field.
    """
    print('Текущее состояние поля:')
    print(f'  0 1 2')
    for i in range(3):
        print(f'{i} {board[i][0]} {board[i][1]} {board[i][2]}')
    print()

def define_winner(board):
    """
    This function determines the current state of the playing field
    and determines whether there are three identical symbols standing in a row or diagonally.
    If this condition is met, the function returns the symbol (the winner), otherwise it returns None.
    :param board: Matrix
    :return: A symbol if the condition is met, and nothing else.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '-':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != '-':
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != '-':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '-':
        return board[0][2]

    return None

def define_draw(board):
    """
    This function determines whether there are any free zones on the playing field.
    :param board: Matrix
    :return: If there are no empty zones, returns True, otherwise False.
    """
    for row in board:
        if '-' in row:
            return False
    return True

def checking_the_values():
    """
    This function is used to check whether the coordinates are entered correctly.
    The function checks their number, whether the entered coordinates are numbers,
    and whether they satisfy the conditions 0 <= x <= 2 and 0 <= y <= 2.
    If any of the conditions do not match the entered variables,
    the user is prompted to enter the coordinates again.
    :return: coordinates: (row, col)
    """
    while True:
        coordinates = input('Введите координаты: ').split()
        if len(coordinates) != 2:
            print('Введите 2 координаты!')
            continue

        if (coordinates[0].isdigit() == False) or (coordinates[1].isdigit() == False):
            print('Вы ввели не числа! Попробуйте снова.')
            continue

        row, col = map(int, coordinates)
        if (row < 0 or row > 2) or (col < 0 or col > 2):
            print('Введите значения в диапазоне [0, 2]!')
            continue

        return row, col

print("Добро пожаловать в игру: <<Крестики Нолики>>")
print("Правила игры: Кто составит 3 символа в ряд первым - тот побеждает")
print("Важно: координаты вводить через пробел, значения должны быть в диапазоне [0, 2], например: 1 1\n")

board = [['-' for _ in range(3)] for _ in range(3)]
print_board(board)
player = 'x'
print(f'Игру начинает игрок: {player}')

while True:
    row, col = checking_the_values()
    board[row][col] = player
    print_board(board)

    if define_winner(board) is not None:
        print(f'Победитель {define_winner(board)}')
        break

    if define_draw(board):
        print('Ничья')
        break

    player = 'o' if player == 'x' else 'x'
    print(f'Ход переходит к игроку: {player}')
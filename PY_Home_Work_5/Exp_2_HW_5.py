# КРЕСТИКИ НОЛИКИ.

# Рабочее поле (пусть это будет список 3 на 3)

game_board=list(range(1, 10))    # Игровое поле.

# Выигрышные комбинации.

victory = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

# Функция которая будет выводить игровое поле на консоль.

def playing_field(game_board):      
    for i in range(3):
        print("|", game_board[0+i*3], "|", game_board[1+i*3], "|", game_board[2+i*3], "|")


# Функция: ХОД ИГРОКА (записать X или 0).
# position - место на игровом поле (1-9)
def player_move(position, symbol):            # Ход игрока
    ind = game_board.index(position)          # На вход подаётся значение списка и определяется индекс.
    game_board[ind] = symbol                  # В списке под индексом меняется значение с 1-9 на X или 0.


# Текущее состояние игры.
def current_result():
    win =""
    for i in victory:   # Проверка каждой строки на наличие элементов.
        if game_board[i[0]] =="X" and game_board[i[1]] =="X" and game_board[i[2]] =="X":
            win = "X"
        if game_board[i[0]] =="0" and game_board[i[1]] =="0" and game_board[i[2]] =="0":
            win = "0"
    return win

game_over = False
player1 = True
count = 0
while game_over == False:
    playing_field(game_board)         # Вызов функции кторая будет выводить игровое поле.

    if player1 == True:
        symbol = "X"
        position = int(input("Player 1:"))
    else:
        symbol = "0"
        position = int(input("Player 2:"))  
         
    player_move(position, symbol)   # Вызов функции ХОД ИГРОКА
    win = current_result()          # Состояние игры
    if win != "":
        game_over = True
    else:
        game_over = False
    player1 = not(player1)

    count += 1
    if count == 9:
        game_over = True
        win = 'Ничья'

playing_field(game_board)
print("Победитель: ", win)
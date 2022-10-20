import prompt


SIGN_X = 'X'
SIGN_O = 'O'


state = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
        ]


def check_index(index):
    min_value = 0
    max_value = 2
    return min_value <= index <= max_value


def print_win_state(state):

    print('Появился победитель') 

    for row in range(len(state)): 
        for col in range(len(state)): 

            if state[row][col] == None: 
                state[row][col] = '_'

            print(state[row][col], end = ' ')

        print()


def check_win(state):
   
    min_index = 0 
    max_index = 2

    for row in range(len(state)):  
        for col in range(len(state)):
            
            if row == min_index: 

                if (state[row][col] == state [row+1][col] == state[row+2][col]) and state[row][col] is not None:
                    return(f'Выиграл {str(state[row][col])} по {col+1}-oму столбцу') 

                if col == min_index:

                    if (state[row][col] == state [row][col+1] == state[row][col+2]) and state[row][col] is not None:
                        return(f'Выиграл {str(state[row][col])} по {row+1}-ой строке')
 
                if  row == col:

                    if (state[row][col] == state [row+1][col+1] == state[row+2][col+2]) and state[row][col] is not None:
                        return(f'Выиграл {str(state[row][col])} по главной диагонали')
                    
                if row + col == max_index:

                    if (state[row][col] == state [row+1][col-1] == state[row+2][col-2]) and state[row][col] is not None:
                        return(f'Выиграл {str(state[row][col])} по побочной диагонали') 
            
            elif col == min_index:

                if (state[row][col] == state [row][col+1] == state[row][col+2]) and state[row][col] is not None:
                    return(f'Выиграл {str(state[row][col])} по {row+1}-ой строке')

    return False


def start():
    steps = 9
    while steps != 0:
        current_sign = SIGN_O if steps % 2 == 0 else SIGN_X

        print(f'Ход: {current_sign}')

        row_index = prompt.integer('Введите строку от 1 до 3: ') - 1
        col_index = prompt.integer('Введите столбец от 1 до 3: ') - 1

        if check_index(row_index) and check_index(col_index):

            if state[row_index][col_index] is not None:
                print('Выберите другое место, так как это занято')
                continue

            state[row_index][col_index] = current_sign
            check_win(state)

            if check_win(state) != False:

                print_win_state(state)
                return print(check_win(state))

            else: 

                for line in state:
                    print(line)

            steps -= 1
        else:
            print('Неверное значение столбца или строки')

    print('Победа дружбы')


start()
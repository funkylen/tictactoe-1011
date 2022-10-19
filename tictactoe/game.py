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

def start():
    steps = 9
    while steps != 0:
        current_sign = SIGN_O if steps % 2 == 0 else SIGN_X

        print(f'Ходит {current_sign}')

        row_index = prompt.integer('Введите строку от 1 до 3: ') - 1
        col_index = prompt.integer('Введите столбец от 1 до 3: ') - 1

        if check_index(row_index) and check_index(col_index):

            if state[row_index][col_index] is not None:
                print('Выберите другое место. Занято.')
                continue

            state[row_index][col_index] = current_sign

            for line in state:
                print(line)

            steps -= 1
        else:
            print('Неправильное значение столбца или строки') 

def current_state(state): 
    for i in range(len(state)): 
        for j in range(len(state)):
            if state[i][j] == None: 
                state[i][j] = '_'
            print(state[i][j], end = ' ') 
        print()

def check_win(state):
    current_state(state)
    min_index = 0 
    max_index = 2
    for i in range(len(state)):  
        for j in range(len(state)):
            
            if i == min_index: 
                
                if (state[i][j] == state [i+1][j] == state[i+2][j]) and state[i][j] != '_':
                    return (f'Выиграл {str(state[i][j])} по {j+1}-oму столбцу')
                if j == min_index:
                    
                    if (state[i][j] == state [i][j+1] == state[i][j+2]) and state[i][j] != '_':
                        return (f'Выиграл {str(state[i][j])} по {i+1}-ой строке')
def check_win(state):
    current_state(state)
    min_index = 0 
    max_index = 2
    for i in range(len(state)):  
        for j in range(len(state)):
            
            if i == min_index: 
                
                if (state[i][j] == state [i+1][j] == state[i+2][j]) and state[i][j] != '_':
                    return (f'Выиграл {str(state[i][j])} по {j+1}-oму столбцу')
                if j == min_index:
                    
                    if (state[i][j] == state [i][j+1] == state[i][j+2]) and state[i][j] != '_':
                        return (f'Выиграл {str(state[i][j])} по {i+1}-ой строке')
                if  i == j:
                    
                    if (state[i][j] == state [i+1][j+1] == state[i+2][j+2]) and state[i][j] != '_':
                        return (f'Выиграл {str(state[i][j])} по главной диагонали')
                if i + j == max_index: 
                    
                    if (state[i][j] == state [i+1][j-1] == state[i+2][j-2]) and state[i][j] != '_':
                        return (f'Выиграл {str(state[i][j])} по побочной диагонали')
            elif j == min_index:
                
                if (state[i][j] == state [i][j+1] == state[i][j+2]) and state[i][j] != '_':
                    return (f'Выиграл {str(state[i][j])} по {i+1}-ой строке')
                
    return 'Ничья'
start()
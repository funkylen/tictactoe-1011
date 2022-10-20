import prompt

SIGN_X = 'X'
SIGN_O = 'O'

state = [
    [None, None, None],
    [None, None, None],
    [None, None, None],
]

def check_win(state):
    if (state[0][0] == state[0][1] == state[0][2]) and state[0][0] != None:
        print('Победил игрок ' + str(state[0][0]))
        return True
    elif (state[1][0] == state[1][1] == state[1][2]) and state[1][0] != None:
        print('Победил игрок ' + str(state[1][0]))
        return True
    elif (state[2][0] == state[2][1] == state[2][2]) and state[2][0] != None:
        print('Победил игрок ' + str(state[2][0]))
        return True
    elif (state[0][0] == state[1][0] == state[2][0]) and state[0][0] != None:
        print('Победил игрок ' + str(state[0][0]))
        return True
    elif (state[0][1] == state[1][1] == state[2][1]) and state[0][1] != None:
        print('Победил игрок ' + str(state[0][1]))
        return True
    elif (state[0][2] == state[1][2] == state[2][2]) and state[0][2] != None:
        print('Победил игрок ' + str(state[0][2]))
        return True
    elif (state[0][0] == state[1][1] == state[2][2]) and state[0][0] != None:
        print('Победил игрок ' + str(state[0][0]))
        return True
    elif (state[0][2] == state[1][1] == state[2][0]) and state[0][2] != None:
        print('Победил игрок ' + str(state[0][2]))
        return True

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

        if check_win(state) == True:
            return
        elif steps == 0:
            print('Ничья')

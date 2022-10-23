import prompt

SIGN_X = 'X'
SIGN_O = 'O'

state = [
    [None, None, None],
    [None, None, None],
    [None, None, None],
]


def check_index(index):
    min_value = 0
    max_value = 2
    return min_value <= index <= max_value


def winner_check():
    for position in range(len(state)):
        if state[0][position] == state[1][position] == state[2][position] and state[0][position] is not None:
            return True
        if state[position][0] == state[position][1] == state[position][2] and state[position][0] is not None:
            return True
    if state[0][0] == state[1][1] == state[2][2] and state[0][0] is not None:
        return True
    if state[2][0] == state[1][1] == state[0][2] and state[2][0] is not None:
        return True


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
        if winner_check():
            print(f'Победил {current_sign}')
            break
        if steps == 0:
            print('draw')

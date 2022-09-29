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

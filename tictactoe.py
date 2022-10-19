import pygame
import sys


def check_win(massive, sign):
    zeroes = 0
    for row in massive:
        zeroes += row.count(0)
        if row.count(sign) == 3:
            return sign.upper()
    for column in range(3):
        if massive[0][column] == sign and massive[1][column] == sign and massive[2][column] == sign:
            return sign.upper()
    if massive[0][0] == sign and massive[1][1] == sign and massive[2][2] == sign:
            return sign.upper()
    if massive[0][2] == sign and massive[1][1] == sign and massive[2][0] == sign:
            return sign.upper()
    if zeroes == 0:
        return 'Friendship'
    return False
    

pygame.init()
margin = 10   #размер отступа
size_block = 100 #размер ячейки
width = height = size_block * 3 + margin * 4 #ширина всей строки

size_window = (width, height)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption('TIC TAC TOE')

black = (0, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
red = (255, 0, 0)
massive = [[0] * 3 for i in range(3)] #массив из нулей для обозначения клеток, если клетка == 0 => клетка пустая
step = 0 
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            column = x_mouse // (size_block + margin)
            row = y_mouse // (size_block + margin)
            if massive[row][column] == 0:
                if step % 2 == 0:    #проверка на пустоту клетки
                    massive[row][column] = 'x'
                else: 
                    massive[row][column] = 'o'
                step += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            massive = [[0] * 3 for i in range(3)]
            step = 0 
            screen.fill(black)
    
    for row in range(3):
        for column in range(3):   #3 на 3 это размер поля, т.е. количество квадратов, да да магические числа
            if massive[row][column] == 'x':
                color = red
            elif massive[row][column] == 'o':
                color = green
            else:
                color = white
            x = column * size_block + (column + 1 ) * margin
            y = row * size_block + (row + 1 ) * margin
            pygame.draw.rect(screen, color, (x, y, size_block, size_block))
            if color == red:
                pygame.draw.line(screen, white, (x + 15, y + 15), (x + size_block - 15, y + size_block - 15), 6)
                pygame.draw.line(screen, white, (x + 15, y + size_block - 15), (x + size_block - 15, y + 15), 6)
            elif color == green:
                pygame.draw.circle(screen, white, (x + size_block / 2, y + size_block / 2), size_block / 2 - 7, 5)
    
    if (step - 1) % 2 == 0: 
        game_over = check_win(massive, 'x')
    else:
        game_over = check_win(massive, 'o')
    
    if game_over:
        
        screen.fill(black)
        
        font1 = pygame.font.SysFont('stxinqkai', 50)
        text1 = font1.render(game_over + ' won!!!', True, white)
        text1_rect = text1.get_rect()
        text1_x = screen.get_width() / 2 - text1_rect.width / 2
        text1_y = screen.get_height() / 2 - text1_rect.height / 2

        font2 = pygame.font.SysFont('stxinqkai', 25)
        text2 = font2.render('Press space to restart the game', True, white)
        text2_rect = text2.get_rect()
        text2_x = screen.get_width() / 2 - text2_rect.width / 2
        
        screen.blit(text1, [text1_x, text1_y])
        screen.blit(text2, [text2_x, 300])

    pygame.display.update()
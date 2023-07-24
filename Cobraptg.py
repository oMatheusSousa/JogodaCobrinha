##### 10 - Game over ####
import pygame
import random
from pygame.locals import *
#funções auxiliares
def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 *10, y//10 *10)
    
#colisões
def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

#dados de movimento
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init() #dados tela
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

snake = [(200, 200), (210, 200), (220, 200)] #dados cobra
snake_skin = pygame.Surface((10,10))
snake_skin.fill((75,0,130))

apple_pos = on_grid_random() #dados maçã
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

my_direction = LEFT #direção inicial

clock = pygame.time.Clock() #define tempo

font = pygame.font.Font('freesansbold.ttf', 18)
score = 0

game_over = False
while not game_over: #AVISO MECHER NO NOT game_over!!!!!!!!!!!! ver linha 109
    clock.tick(10) #VELOCIDADE (arrumar a velocidade para 20 depois)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
   
#locomoção (simbolo != significa diferente) e nesse caso impede a 
#cobra de ir na direção oposta passando por ela mesma 
        if event.type == KEYDOWN: 
            if event.key == K_UP and my_direction != DOWN:
                my_direction = UP
            if event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN
            if event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT
            if event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT 
    #add + pontos
    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))
        score = score +1
           
    #verifica se a cobra colide com a parede e se colidir game over
    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
        game_over = True
        break

    #checa se a cobra colidiu com ela mesma 
    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
            break

    if game_over:
        break

    for i in range(len(snake) - 1, 0, -1):# cobra corpo
        snake[i] = (snake[i-1][0], snake[i-1][1])

    #movimentação atual da cobra
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] -10)   
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] +10, snake[0][1])  
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] +10) 
    if my_direction == LEFT:
        snake[0] = (snake[0][0] -10, snake[0][1]) 
    
    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)

    for x in range(0, 600, 10): # desenha linhas verticais
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 600))
    for y in range(0, 600, 10): # desenha linhas horisontais
        pygame.draw.line(screen, (40, 40, 40), (0, y), (600, y))

    #dados pontuação
    score_font = font.render('Score: %s' % (score), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = ( 600 -120, 10)
    screen.blit(score_font, score_rect)

    for pos in snake: 
        screen.blit(snake_skin,pos)

    pygame.display.update()
    #encerramento do jogo após game over
while True: 
    game_over_font = pygame.font.Font('freesansbold.ttf', 75)
    game_over_screen = game_over_font.render('You Die', True, (255, 0, 0))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (600 / 2, 10)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
       for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit() 
import pygame
import random

pygame.init()

def aleatorio(x,y):
    numero = random.randint(x,y)
    return numero

tamanho = (1280,720)
preto = (0,0,0)
branco = (255,255,255)
verde = (0,255,0)
vermelho = (255,0,0)

clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Snake Game")

#variáveis
cima = False
baixo = False
esquerda = False
direita = False
locaisy_cobra = [360]
locaisx_cobra = [640]
cobra = []
x = aleatorio(1,1270)
y = aleatorio(1,710)
comida = [x,y,10,10]


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            direita = True
        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            direita = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            esquerda = True
        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            esquerda = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            baixo = True
        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            baixo = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            cima = True
        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
            cima = False

    tela.fill(preto)

    for x in locaisx_cobra:
        for y in locaisy_cobra:
            cobra = [x,y,10,10]
            pygame.draw.rect(tela,verde,(cobra))

    pygame.draw.rect(tela,vermelho,(comida))

    '''if (locaisx_cobra[0] < x + 10) and (locaisx_cobra[0] + 10 > x) and (locaisy_cobra[0] < y + 10) and (locaisy_cobra[0] + 10 > y):
        x = aleatorio(1,1270)
        y = aleatorio(1,710)
        comida = [x,y,10,10]'''

    if direita:
        locaisx_cobra[0] += 10
    if esquerda:
        locaisx_cobra[0] -= 10
    if cima:
        locaisy_cobra[0] -= 10
    if baixo:
        locaisy_cobra[0] += 10

    pygame.display.update()
    clock.tick(20)

pygame.quit()
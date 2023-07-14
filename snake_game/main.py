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
cobra = [640,360,10,10]
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

    pygame.draw.rect(tela,verde,(cobra))
    pygame.draw.rect(tela,vermelho,(comida))

    if direita:
        cobra[0] += 2
    if esquerda:
        cobra[0] -= 2
    if cima:
        cobra[1] -= 2
    if baixo:
        cobra[1] += 2



    pygame.display.update()
    clock.tick(144)

pygame.quit()
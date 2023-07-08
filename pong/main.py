import pygame

pygame.init()

tamanho = (1280,720)
verde = (0,128,0)
cinza = (192,192,192)
preto = (0,0,0)
branco = (255,255,255)
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Pong")

#variaveis
#jogador 1
x_jogador1 = 74
y_jogador1_cima = 265
y_jogador1_baixo = 454
velocidade = 1
movimentoY = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            movimentoY = y_jogador1_baixo - velocidade
            movimentoY = y_jogador1_cima - velocidade
        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
            movimentoY = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            movimentoY = y_jogador1_baixo + velocidade
            movimentoY = y_jogador1_cima + velocidade
        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            movimentoY = 0

    tela.fill(verde)
    
    #desenho do campo
    pygame.draw.circle(tela,branco,(642,360),84)
    pygame.draw.circle(tela,verde,(642,360),80)
    pygame.draw.line(tela,branco,(0,-2),(0,722),4)
    pygame.draw.line(tela,branco,(1279,-2),(1279,722),4)
    pygame.draw.line(tela,branco,(-2,719),(1282,719),4)
    pygame.draw.line(tela,branco,(-2,1),(1282,1),4)
    pygame.draw.line(tela,branco,(642,0),(642,720),4)

    #goleiros e bola
    pygame.draw.line(tela, preto,(x_jogador1,y_jogador1_cima) , (x_jogador1,y_jogador1_baixo),5)
    pygame.draw.line(tela,preto,(1205,454),(1205,265),5)
    pygame.draw.circle(tela,preto,(642,360),10)

    y_jogador1_cima = y_jogador1_cima - movimentoY
    y_jogador1_baixo = y_jogador1_baixo - movimentoY
    
    if y_jogador1_baixo and y_jogador1_cima <= 0:
        y_jogador1_cima = 0
        y_jogador1_baixo = 189

    if y_jogador1_baixo and y_jogador1_cima >= 720:
        y_jogador1_cima = 531
        y_jogador1_baixo = 720

    pygame.display.update()
    clock.tick(144)

pygame.quit()
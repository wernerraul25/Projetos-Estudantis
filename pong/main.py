import pygame

pygame.init()
pygame.mixer.init()

largura = 1280
altura = 720
tamanho = (largura,altura)

#cores
verde = (0,128,0)
cinza = (192,192,192)
preto = (0,0,0)
branco = (255,255,255)
vermelho = (255,0,0)

clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Pong")

#sons
tetra = pygame.mixer.Sound("tetra.mp3")
tetra.set_volume(0.1)
champions = pygame.mixer.Sound("champions.wav")
champions.set_volume(0.03)
estadio = pygame.mixer.Sound("estadio.mp3")
estadio.set_volume(0.05)

#variaveis

#fontes
fonte = pygame.font.Font(None,80)
fonte_inicial = pygame.font.Font(None,50)
fonte_pequena = pygame.font.Font(None,30)

#jogador 1
jogador1_altura = 189
jogador1_largura = 5
jogador1_y = 360 - ( jogador1_altura // 2)
jogador1_x = 74
subindo1 = False
descendo1 = False

#jogador 2
jogador2_altura = 189
jogador2_largura = 5
jogador2_y = 360 - (jogador2_altura // 2)
jogador2_x = 1205
subindo2 = False
descendo2 = False

#bola
pos_x = largura // 2
pos_y = altura // 2
vel_x = 0
vel_y = 0
raio = 10

#resultado
pontos1 = 0
pontos2 = 0
pontos_max = 10

#telas
tela1 = True
tela2 = False
tela3 = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if tela1:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                tela1 = False
                tela2 = True
                vel_x = 5
                vel_y = 5

        if tela2:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                subindo1 = True
            if event.type == pygame.KEYUP and event.key == pygame.K_w:
                subindo1 = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                descendo1 = True
            if event.type == pygame.KEYUP and event.key == pygame.K_s:
                descendo1 = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                subindo2 = True
            if event.type == pygame.KEYUP and event.key == pygame.K_UP:
                subindo2 = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                descendo2 = True
            if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                descendo2 = False

    if tela1:
        tela.fill(cinza)
        champions.play()
        texto_inicio = fonte_inicial.render("Aperte ESPAÇO para iniciar",True,branco)
        tela.blit(texto_inicio,(400,altura//2))
        creditos = fonte_pequena.render("By: Raul Werner",True,branco)
        tela.blit(creditos,(1100,700))
        pong = fonte.render("PONG",True,vermelho)
        tela.blit(pong,(530,altura//2 - 200))

    if tela2:        
        tela.fill(verde)
        champions.stop()
        estadio.play()
        #desenho do campo
        pygame.draw.circle(tela,branco,(largura // 2,altura // 2),84)
        pygame.draw.circle(tela,verde,(largura // 2,altura // 2),80)
        pygame.draw.line(tela,branco,(0,-2),(0,722),4)
        pygame.draw.line(tela,branco,(1279,-2),(1279,722),4)
        pygame.draw.line(tela,branco,(-2,719),(1282,719),4)
        pygame.draw.line(tela,branco,(-2,1),(1282,1),4)
        pygame.draw.line(tela,branco,(largura // 2,0),(largura // 2,720),4)

        #pontuação
        pontuacao1 = fonte.render(str(pontos1), True, branco)
        tela.blit(pontuacao1,(320,50))
        pontuacao2 = fonte.render(str(pontos2),True,branco)
        tela.blit(pontuacao2,(960,50))

        #goleiros e bola
        #jogador 1
        pygame.draw.rect(tela,preto,(jogador1_x,jogador1_y,jogador1_largura,jogador1_altura))
        #jogador 2
        pygame.draw.rect(tela,preto,(jogador2_x,jogador2_y,jogador2_largura,jogador2_altura))
        #bola
        pygame.draw.circle(tela,preto,(pos_x,pos_y),raio)
        pos_x += vel_x
        pos_y += vel_y
        if pos_x <= 0 or pos_x >= largura:
            vel_x = -vel_x
            if pos_x <=0:
                pontos2 += 1
            elif pos_x >= largura:
                pontos1 += 1
            pos_x = largura // 2
            pos_y = altura // 2

        if pos_y <= 0 or pos_y >= altura:
            vel_y = -vel_y

        if subindo1:
            jogador1_y -= 8
        if descendo1:
            jogador1_y += 8
        if jogador1_y <= 0:
            jogador1_y = 0
        if jogador1_y >= 531:
            jogador1_y = 531
        
        if subindo2:
            jogador2_y -= 8
        if descendo2:
            jogador2_y += 8
        if jogador2_y <= 0:
            jogador2_y = 0
        if jogador2_y >= 531:
            jogador2_y = 531

        #colisão bola jogador 1
        if pos_y + raio >= jogador1_y and pos_y + raio <= jogador1_y + jogador1_altura and pos_x >= jogador1_x and pos_x <= jogador1_x + jogador1_largura:
            vel_x = -vel_x
            vel_y = -vel_y
        
        #colisão bola jogador 2
        if pos_y + raio >= jogador2_y and pos_y + raio <= jogador2_y + jogador2_altura and pos_x >= jogador2_x and pos_x <= jogador2_x + jogador2_largura:
            vel_x = -vel_x
            vel_y = -vel_y

        #se pontuação máxima vai para tela 3
        if pontos1 == pontos_max:
            tela2 = False
            tela3 = True
        elif pontos2 == pontos_max:
            tela2 = False
            tela3 = True

    if tela3:
        tela.fill(cinza)
        estadio.stop()
        tetra.play()
        if pontos1 > pontos2:
            ganhador1 = fonte_inicial.render("O Jogador 1 foi o vencedor com "+str(pontos1)+" pontos!",True, verde)
            tela.blit(ganhador1,(300,altura//2))
        elif pontos2 > pontos1:
            ganhador2 = fonte_inicial.render("O Jogador 2 foi o vencedor com "+str(pontos2)+" pontos!",True, verde)
            tela.blit(ganhador2,(300,altura//2))

    pygame.display.update()
    clock.tick(144)

pygame.quit()
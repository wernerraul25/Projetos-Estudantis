import pygame

pygame.init()

tamanho = (1280,720)
preto = (0,0,0)
branco = (255,255,255)
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Snake Game")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    
    tela.fill(preto)
    
    pygame.display.update()
    clock.tick(144)

pygame.quit()
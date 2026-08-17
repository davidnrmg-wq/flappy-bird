import pygame 
from scripts.jogador import jogador
from scripts.cano import Cano

pygame.init()

tamnahoTela = [600, 400]
tela = pygame.display.set_mode(tamnahoTela)
pygame.display.set_caption("Paulo pau no cu ")
relogio = pygame.time.Clock()
corFundo = (86, 148, 214)
jog = jogador(tela, 100, 100)
cano = Cano(tela)

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
    tela.fill(corFundo) 

    jog.atualizar()
    jog.desenhar()
    cano.atualizar()
    cano.desenhar()

    relogio.tick(60)
    pygame.display.flip()
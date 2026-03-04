import pygame
import sys
from settings import ANCHO, ALTO, BLANCO
from jugador import Jugador
from plataforma import Plataforma

plataformas = pygame.sprite.Group()
suelo = Plataforma(0, 550, 800, 50)
plataformas.add(suelo)
plataformas.add(Plataforma(200, 350, 200, 20))

class Juego:
    def __init__(self):
        pygame.init()

        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Clase 10 - Felipe")
        self.clock = pygame.time.Clock()

        self.jugador = Jugador()

    def ejecutar(self):
        while True:
            self.clock.tick(60)
            self.pantalla.fill(BLANCO)
            
            # Movimiento del jugador
            teclas = pygame.key.get_pressed()
            self.jugador.update(teclas, plataformas)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            plataformas.draw(self.pantalla)
            self.pantalla.blits([(self.jugador.image, self.jugador.rect)])
            pygame.display.flip()

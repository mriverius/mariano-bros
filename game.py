import pygame
import sys
from settings import ANCHO, ALTO, BLANCO
from jugador import Jugador
from plataforma import Plataforma
from enemigo import Enemigo

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
        self.fuente = pygame.font.Font(None, 36)

        self.jugador = Jugador()
        self.puntaje = 0

        self.enemigos = pygame.sprite.Group()
        enemigo1 = Enemigo()
        self.enemigos.add(enemigo1)

    def ejecutar(self):
        while True:
            self.clock.tick(60)
            self.pantalla.fill(BLANCO)
            
            # Movimiento del jugador
            teclas = pygame.key.get_pressed()
            puntos_ganados = self.jugador.update(teclas, plataformas, self.enemigos)

            # Puntaje del jugador
            self.puntaje += puntos_ganados

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            plataformas.draw(self.pantalla)
            self.enemigos.draw(self.pantalla)
            self.enemigos.update(plataformas)

            self.pantalla.blits([(self.jugador.image, self.jugador.rect)])
            
            # Mostrar puntaje
            texto_puntaje = self.fuente.render(f"Puntaje: {self.puntaje}", True, (0, 0, 0))
            self.pantalla.blit(texto_puntaje, (10, 10))
            
            pygame.display.flip()

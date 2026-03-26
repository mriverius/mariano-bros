import pygame
import sys
from settings import ANCHO, ALTO, BLANCO
from jugador import Jugador
from plataforma import Plataforma
from enemigo import Enemigo

plataformas = pygame.sprite.Group()
suelo = Plataforma(0, 550, 800, 50)
plataformas.add(suelo)
plataformas.add(Plataforma(200, 350, 200, 20, (255, 255, 0)))

class Juego:
    def __init__(self):
        pygame.init()
    
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Clase 10 - Felipe")
        self.clock = pygame.time.Clock()
        self.fuente = pygame.font.Font(None, 36)
        self.fuente_grande = pygame.font.Font(None, 72)

        # Fondo de pantalla
        self.fondo = pygame.image.load("assets/fondo.jpg").convert()
        self.fondo = pygame.transform.scale(self.fondo, (ANCHO, ALTO))

        self.jugador = Jugador()
        self.puntaje = 0

        self.estado = "jugando"
        self.vidas = 3

        self.enemigos = pygame.sprite.Group()
        enemigo1 = Enemigo()
        self.enemigos.add(enemigo1)

    def ejecutar(self):
        while True:
            self.clock.tick(60)
            self.pantalla.blit(self.fondo, (0, 0))
            
            # Movimiento del jugador
            teclas = pygame.key.get_pressed()
            resultado = self.jugador.update(teclas, plataformas, self.enemigos)

            # Puntaje del jugador
            self.puntaje += resultado["puntos"]

            if resultado["danio"]:
                self.vidas -= 1
                print(f"¡Perdiste una vida! Te quedan {self.vidas}")
                # Reposicionar al jugador
                self.jugador.rect.x = 100
                self.jugador.rect.y = 200
                self.jugador.velocidad_y = 0

                if self.vidas <= 0:
                    self.estado = "game_over"
            
            if self.estado == "game_over":
                self.mostrar_game_over()

            # Verificar si no hay enemigos y crear uno nuevo
            if len(self.enemigos) == 0:
                nuevo_enemigo = Enemigo()
                self.enemigos.add(nuevo_enemigo)

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

            # Mostrar vidas
            texto_vidas = self.fuente.render(f"Vidas: {self.vidas}", True, (0, 0, 0))
            self.pantalla.blit(texto_vidas, (10, 40))
            
            pygame.display.flip()

    def mostrar_game_over(self):
        self.pantalla.fill((0, 0, 0))

        texto_game_over = self.fuente_grande.render("GAME OVER", True, (255, 0, 0))
        posicion_game_over = texto_game_over.get_rect(center=(ANCHO // 2, ALTO // 2 - 50))
        self.pantalla.blit(texto_game_over, posicion_game_over)

        # MOSTRAR PUNTAJE
        # MOSTRAR OPCION REINICIAR

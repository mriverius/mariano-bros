import pygame

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.frames = [
            pygame.transform.scale(pygame.image.load("assets/gokuss1.png").convert_alpha(), (150, 150)),
            pygame.transform.scale(pygame.image.load("assets/gokuss2.png").convert_alpha(), (150, 150)),
            pygame.transform.scale(pygame.image.load("assets/gokuss3.png").convert_alpha(), (150, 150))
        ]

        self.image = self.frames[2]
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 100

        self.velocidad_x = 6

        # Gravedad
        self.velocidad_y = 0
        self.gravedad = 0.5

    def update(self, teclas, plataformas):
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidad_x
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidad_x
        
        # Salto
        if teclas[pygame.K_SPACE]:
            # Verificar si está en una plataforma para poder saltar
            self.rect.y += 5  # Bajar un poco para verificar colisión
            colisiones = pygame.sprite.spritecollide(self, plataformas, False)
            self.rect.y -= 5  # Volver a la posición original
            
            if colisiones:  # Si hay colisión, puede saltar
                self.velocidad_y = -12  # Velocidad de salto (negativa porque va hacia arriba)

        # Aplicar gravedad
        self.velocidad_y += self.gravedad
        self.rect.y += self.velocidad_y

        # Colisiones
        colisiones = pygame.sprite.spritecollide(self, plataformas, False)
        for plataforma in colisiones:
            if self.velocidad_y > 0:  # Cayendo - aterrizar encima
                self.rect.bottom = plataforma.rect.top
                self.velocidad_y = 0  # Detener la caída
            elif self.velocidad_y < 0:  # Saltando - chocar con abajo
                self.rect.top = plataforma.rect.bottom
                self.velocidad_y = 0  # Detener el salto
            break  # Solo necesita una colisión
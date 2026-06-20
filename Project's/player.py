import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, posicion_inicial):
        # Llama al constructor de la clase base para inicializar el objeto correctamente
        super().__init__()
        
        # Creamos una superficie visual para el jugador (un cuadro de 50x50 pixeles)
        self.image = pygame.Surface((50, 50))
        # Pintamos al jugador de color azul
        self.image.fill((0, 102, 204))
        
        # Obtenemos el rectangulo que define los limites y la posicion del jugador
        self.rect = self.image.get_rect()
        # Colocamos al jugador en la posicion que recibimos al crearlo
        self.rect.topleft = posicion_inicial
        
        # Definimos la velocidad de movimiento en pixeles por cada actualizacion
        self.velocidad = 5

    def update(self):
        # Capturamos todas las teclas que estan siendo presionadas en este momento
        teclas = pygame.key.get_pressed()
        
        # Movimiento hacia la izquierda
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidad
        # Movimiento hacia la derecha
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidad
        # Movimiento hacia arriba
        if teclas[pygame.K_UP]:
            self.rect.y -= self.velocidad
        # Movimiento hacia abajo
        if teclas[pygame.K_DOWN]:
            self.rect.y += self.velocidad

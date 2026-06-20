import pygame
from player import Player

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mi juego")

# Creamos el contenedor de elementos
todos_los_elementos = pygame.sprite.Group()
player = Player((40, 40))

# ¡CUIDADO! Olvidaste meter al jugador dentro del contenedor para que pueda ser dibujado
todos_los_elementos.add(player)

running = True

# Para controlar la velocidad del juego de forma eficiente
reloj = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 1. Actualizamos la logica (movimiento del jugador)
    todos_los_elementos.update()

    # 2. Limpiamos la pantalla con el fondo gris oscuro
    screen.fill((30, 30, 30))

    # 3. Dibujamos los elementos encima del fondo limpio
    todos_los_elementos.add(player) # Nos aseguramos de que este agregado
    todos_los_elementos.draw(screen)

    # 4. Mostramos todo en el monitor al final del fotograma
    pygame.display.flip()
    
    # Controlamos que el juego corra maximo a 60 fotogramas por segundo
    reloj.tick(60)

pygame.quit()

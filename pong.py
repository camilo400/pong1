import pygame

ANCHO = 800
ALTO = 600

C_OBJETOS = (255, 255, 255)
ANCHO_PALA = 20
ALTO_PALA = 60
MARGEN = 10


class Pong:
    def __init__(self) -> None:
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))

    def jugar(self):
        salir = False
        while not salir:
            # bucle principal o (main loop)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    salir = True

            # Renderizar nuestros objetos
            # jugador 1(izquierda)
            jugador1 = pygame.Rect(
                MARGEN, ALTO/2 - ALTO_PALA/2, ANCHO_PALA, ALTO_PALA)
            pygame.draw.rect(self.pantalla, (C_OBJETOS), jugador1)
            # jugador 2(derecha)
            jugador2 = pygame.Rect(
                ANCHO - MARGEN - ANCHO_PALA, ALTO/2 - ALTO_PALA/2, ANCHO_PALA, ALTO_PALA)
            pygame.draw.rect(self.pantalla, (C_OBJETOS), jugador2)
            # mostrar los cambios en la pantalla
            pygame.display.flip()

        pygame.quit()


if __name__ == '__main__':
    print('Has llamado a pong.py directamente deasde la linea de comandos')
    juego = Pong()
    juego.jugar()
else:
    print('Has llamado a pong.py desde una sentencia import')

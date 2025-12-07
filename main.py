import pygame

class Sprite:
    def __init__(self,center,image):
        self.image = image
        self.rect = image.get_frect()
        self.rect.center = center


    def render(self,surface):
        surface.blit(self.image, self.rect)

        # на чем          что       где                                                                  привет



window = pygame.Window('Ping Pong',(800,600),pygame.WINDOWPOS_CENTERED)

surface = window.get_surface()
clock = pygame.Clock()

image = pygame.Surface( (40, 100) )
image.fill('orange')
left_player = Sprite((40,300), image)



running = True
while running:
    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # обновление объектов

    # Отрисовка
    # RGB - (0-255, 0-255, 0-255)
    surface.fill('white')
    left_player.render(surface)
    left_player.rect.x +=1
    window.flip()
    clock.tick(60)
    window.title = 'FPS:' + str(round(clock.get_fps()))

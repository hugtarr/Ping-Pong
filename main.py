import pygame

class Sprite:
    def __init__(self,center,image):
        self.image = image
        self.rect = image.get_frect()
        self.rect.center = center


    def render(self,surface):
        surface.blit(self.image, self.rect)

        # на чем          что       где                                                                  привет


class Player(Sprite):
    def __init__(self,center,image, speed):
        super().__init__(center,image)
        self.speed = speed
        self.move_up =  False
        self.move_down = False

    def update(self):
        if self.move_up != self.move_down:
            if self.move_up:
                self.rect.y-= self.speed
            else:
                self.rect.y+= self.speed

window = pygame.Window('Ping Pong',(800,600),pygame.WINDOWPOS_CENTERED)

surface = window.get_surface()
clock = pygame.Clock()

image = pygame.Surface( (40, 100) )
image.fill('orange')
left_player = Player((40,300), image,10)
right_player = Player((760,300),image, 10)


running = True
while running:
    # обработка событий
    for event in pygame.event.get():
       
        if event.type == pygame.QUIT:
            running = False 
        #левый чел
        elif event.type == pygame.KEYDOWN: # при нажатии клавиши 
            if event.key == pygame.K_w:
               left_player.move_up = True
            elif event.key == pygame.K_s:
                left_player.move_down = True
        #правый чел
            elif event.key == pygame.K_UP:
                right_player.move_up = True
            elif event.key == pygame.K_DOWN:
                right_player.move_down = True


        elif event.type == pygame.KEYUP: #при отпускании клавиши
            # левый игрок 
            if event.key == pygame.K_w:
                left_player.move_up = False
            elif event.key == pygame.K_s:
                left_player.move_down = False

            #правый игрок
            elif event.key == pygame.K_UP:
                right_player.move_up = False
            elif event.key == pygame.K_DOWN:
                right_player.move_down = False
    # обновление объектов
    left_player.update()
    right_player.update()
    

    # Отрисовка
    # RGB - (0-255, 0-255, 0-255)
    surface.fill('white')
    left_player.render(surface)
    right_player.render(surface)
    window.flip()
    clock.tick(60)
    window.title = 'FPS:' + str(round(clock.get_fps()))


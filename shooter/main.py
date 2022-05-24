import pygame
pygame.init()
import time
clock = pygame.time.Clock()
import random

run = True
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.surface.Surface((screen_width, screen_height))
background.fill((100, 100, 100))

class Zombie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.posx = random.randint(500,900)
        self.posy = random.randint(500, 900)
        self.image = pygame.image.load("zombie.png")
        self.rect = self.image.get_rect()
        self.health = 100
        self.rect.center = (self.posx, self.posy)



zombiea = Zombie()

zombie_single = pygame.sprite.GroupSingle()

zombie_single.add(zombiea)


class Player(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        super().__init__()
        self.posx = posx
        self.posy = posy
        self.image = pygame.image.load("Killer.jpg")
        self.rect = self.image.get_rect()
        self.rect.topleft = (posx, posy)
        self.health = 100

    def update(self):
        self.rect.topleft = (self.posx, self.posy)
        single_player.draw(screen)


#bullet() ---> moves bullet for i in range(20), and at each i it will draw both the bullet and the player and flip the screen

class bullet(pygame.sprite.Sprite):
    def __init__(self, p_x, p_y):
        super().__init__()
        self.image = pygame.surface.Surface((20,20))
        self.rect = self.image.get_rect()
        self.p_x = p_x
        self.p_y = p_y
        self.rect.topleft = (self.p_x, self.p_y)
    def check_collision(self):
        if self.rect.colliderect(zombiea.rect):
            zombiea.health = zombiea.health - 100
            print("You've shot the zombie")
            print("zombie's health is", zombiea.health)
            return True


    def update(self):

        self.p_x = player1.posx + 100
        self.p_y = player1.posy + 60
        for j in range(15):
            screen.blit(background, (0,0))
            self.p_x = self.p_x + 10
            self.rect.topleft = (self.p_x, self.p_y)
            checkEvents(player1)
            player1.update()
            zombie_single.draw(screen)
            bullet_single.draw(screen)
            pygame.display.flip()
            if self.check_collision():
                break
            clock.tick(500)

        screen.blit(background, (0,0))

          #  clock.tick(60)











#player object instantiation and adding to group

player1 = Player(0, 0)

single_player = pygame.sprite.GroupSingle()

single_player.add(player1)

#bullet object instantiation and adding to group

bullet1 = bullet(player1.posx, player1.posy)

bullet_single = pygame.sprite.GroupSingle()

bullet_single.add(bullet1)


x = 0
y = 0
removed_indexes = []
def checkEvents(obj):
    global eventList

    for i in eventList:

        if i.type == pygame.KEYDOWN:



            if i.key == pygame.K_UP:
                obj.posy = obj.posy - 30

            if i.key == pygame.K_DOWN:
                obj.posy = obj.posy + 30

            if i.key == pygame.K_RIGHT:
                obj.posx = obj.posx + 30

            if i.key == pygame.K_LEFT:
                obj.posx = obj.posx - 30

            eventList.remove(i)

counter = 0
while run:
    global eventList
    eventList = pygame.event.get()

    for i in eventList:
        if i.type == pygame.QUIT:
            run = False

        else:


            if i.type == pygame.MOUSEBUTTONDOWN:
                print("IF BEING RUN", counter)
                bullet_single.update()



            else:
                print("else being run", counter)
                checkEvents(player1)
                single_player.update()
                zombie_single.draw(screen)
                pygame.display.flip()
                screen.blit(background, (0,0))
                print(player1.posx, player1.posy)


            counter = counter + 1
            print("counter is", counter)

            eventList = pygame.event.get()





raise SystemExit
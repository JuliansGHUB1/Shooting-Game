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

font = pygame.font.SysFont("Comic Sans", 25)

class Zombie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.posx = random.randint(500,900)
        self.posy = random.randint(500, 900)
        self.image = pygame.image.load("zombie.png")
        self.rect = self.image.get_rect()
        self.health = 100
        self.rect.center = (self.posx, self.posy)
        self.text_surface = font.render(str(self.health), False, (180, 180, 180))
        self.textwidth = self.text_surface.get_width()
        self.textheight = self.text_surface.get_height()
        self.text_surf_holder = pygame.surface.Surface((self.textwidth, self.textheight))
        self.text_rect = self.text_surf_holder.get_rect()
        self.text_rect.center = (self.posx, self.posy + 150)

    def updatehealthbox(self):
        self.text_surface = font.render(str(self.health), False, (180, 180, 180))
        self.text_surf_holder.blit(self.text_surf_holder,(0,0))
        self.text_rect.center = (self.posx, self.posy + 150)
        self.text_surf_holder.blit(screen, (self.posx, self.posy + 150))



    def update(self):

        if player1.posx > self.posx:
            self.posx = self.posx + 1
        if player1.posx < self.posx:
            self.posx = self.posx - 1
        if player1.posy > self.posy:
            self.posy = self.posy + 1
        if player1.posy < self.posy:
            self.posy = self.posy - 1
        self.rect.center = (self.posx, self.posy)

        self.updatehealthbox()




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
            self.p_x = self.p_x + 10
            self.rect.topleft = (self.p_x, self.p_y)

            if self.check_collision():
                self.kill()
            if self.p_x > 1000:
                self.kill()


          #  clock.tick(60)











#player object instantiation and adding to group

player1 = Player(0, 0)

single_player = pygame.sprite.GroupSingle()

single_player.add(player1)


bullet_group = pygame.sprite.Group()



x = 0
y = 0

def checkEvents(current_item, obj):

            if i.key == pygame.K_UP:
                obj.posy = obj.posy - 30

            if i.key == pygame.K_DOWN:
                obj.posy = obj.posy + 30

            if i.key == pygame.K_RIGHT:
                obj.posx = obj.posx + 30

            if i.key == pygame.K_LEFT:
                obj.posx = obj.posx - 30



counter = 0

while run:

    eventList = pygame.event.get()

    for i in eventList:

        if i.type == pygame.QUIT:
            run = False

        else:


            if i.type == pygame.MOUSEBUTTONDOWN:
                newbullet = bullet(player1.posx + 160, player1.posy + 50)
                bullet_group.add(newbullet)




            if i.type == pygame.KEYDOWN:
                checkEvents(i, player1)


            counter = counter + 1
            print("counter is", counter)


            screen.blit(background, (0,0))
            single_player.update()
            bullet_group.update()
            zombie_single.update()
            single_player.draw(screen)
            zombie_single.draw(screen)
            bullet_group.draw(screen)
            pygame.display.flip()







raise SystemExit
import pygame
pygame.init()
import time
clock = pygame.time.Clock()
import random

global run
run = True
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.surface.Surface((screen_width, screen_height))
background.fill((100, 100, 100))

font = pygame.font.SysFont("Comic Sans", 85)

class Zombie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.posx = random.randint(500,900)
        self.posy = random.randint(500, 900)
        self.image = pygame.image.load("zombie.png")
        self.rect = self.image.get_rect()
        self.health = 100
        self.rect.center = (self.posx, self.posy)





    def update(self):
        if self.health <= 0:
            self.kill()
        if player1.posx > self.posx:
            self.posx = self.posx + 0.5
        if player1.posx < self.posx:
            self.posx = self.posx - 0.5
        if player1.posy > self.posy:
            self.posy = self.posy + 0.5
        if player1.posy < self.posy:
            self.posy = self.posy - 0.5

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
        self.score = 0

    def check_zombie_bite(self):
        if self.rect.colliderect(zombiea.rect):
            print("You've been bit")
            self.health = self.health - 10

    def update(self):
        global run
        self.rect.topleft = (self.posx, self.posy)
        self.check_zombie_bite()
        if self.health <= 0:
            self.kill()
            hitbox_player.kill()
            run = False



        single_player.draw(screen)

class HitBox(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.posx = zombiea.posx
        self.posy = zombiea.posy + 100
        self.text_surface = font.render(str(zombiea.health), False, (180, 180, 180))
        self.width = self.text_surface.get_width()
        self.height = self.text_surface.get_height()
        self.image = pygame.surface.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.center = (self.posx, self.posy)
    def update(self):
        if zombiea.health <= 0:
            self.kill()
        self.text_surface = font.render(str(zombiea.health), False, (0, 150, 255))
        self.width = self.text_surface.get_width()
        self.height = self.text_surface.get_height()
        self.image = pygame.surface.Surface((self.width, self.height))
        self.image.fill((100, 100, 100))
        self.image.blit(self.text_surface, (0,0))
        self.rect = self.image.get_rect()
       # self.rect.center = (zombiea.posx, zombiea.posy + 100)
        self.rect.center = (zombiea.posx, zombiea.posy + 100)



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
            zombiea.health = zombiea.health - 10
            print("You've shot the zombie")
            print("zombie's health is", zombiea.health)
            return True
    if zombiea.health <= 0:
        zombiea.kill()


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

Hitbox1 = HitBox()

HitBox_Group = pygame.sprite.GroupSingle()
HitBox_Group.add(Hitbox1)




class health_player1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.text_surface = font.render(str(player1.health), False, (0, 150, 255))
        self.surface_width = self.text_surface.get_width()
        self.surface_height = self.text_surface.get_height()
        self.image = pygame.surface.Surface((self.surface_width, self.surface_height))
        self.rect = self.image.get_rect()
        self.rect.center = (player1.posx, player1.posy - 100)

    def update(self):
        self.text_surface = font.render(str(player1.health), False, (0, 150, 255))
        self.surface_width = self.text_surface.get_width()
        self.surface_height = self.text_surface.get_height()
        self.image = pygame.surface.Surface((self.surface_width, self.surface_height))
        self.image.blit(self.text_surface, (0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (player1.posx, player1.posy - 100)

class Flag(pygame.sprite.Sprite):
    def __init__(self, posx, posy, filename):
        super().__init__()
        self.posx = random.randint(0, screen_width)
        self.posy = random.randint(0, screen_height)
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
    def check_Collision(self):
        if self.rect.colliderect(player1.rect):
            player1.score = player1.score + 100
            self.kill()
            print(player1.score)
    def update(self):
        self.rect = self.image.get_rect()
        self.check_Collision()


hitbox_player = health_player1()
player_hitboxgroup = pygame.sprite.GroupSingle()
player_hitboxgroup.add(hitbox_player)





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

    if len(eventList) == 0:
        screen.blit(background, (0, 0))
        single_player.update()
        bullet_group.update()
        zombie_single.update()
        HitBox_Group.update()
        player_hitboxgroup.update()
        single_player.draw(screen)
        zombie_single.draw(screen)
        HitBox_Group.draw(screen)
        bullet_group.draw(screen)
        player_hitboxgroup.draw(screen)
        pygame.display.flip()



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

            screen.blit(background, (0, 0))
            single_player.update()
            bullet_group.update()
            zombie_single.update()
            HitBox_Group.update()
            player_hitboxgroup.update()
            single_player.draw(screen)
            zombie_single.draw(screen)
            HitBox_Group.draw(screen)
            bullet_group.draw(screen)
            player_hitboxgroup.draw(screen)
            pygame.display.flip()
            print("here")







screen.blit(background, (0,0))
text_surface = font.render("YOU LOSE", False, (180, 50, 180))
text_surface_x = text_surface.get_width()
text_surface_y = text_surface.get_height()
new_surface = pygame.surface.Surface((text_surface_x, text_surface_y))
new_surface.blit(text_surface, (0,0))
screen.blit(new_surface, (0, 0))
pygame.display.flip()

current_time = time.time()

while time.time() - current_time <= 20:
    eventList = pygame.event.get()

    for i in eventList:
        if i.type == pygame.QUIT:
            raise SystemExit

    screen.blit(background, (0, 0))
    text_surface = font.render("YOU LOSE", False, (180, 50, 180))
    text_surface_x = text_surface.get_width()
    text_surface_y = text_surface.get_height()
    new_surface = pygame.surface.Surface((text_surface_x, text_surface_y))
    new_surface.blit(text_surface, (0, 0))
    screen.blit(new_surface, (0, 0))
    pygame.display.flip()




raise SystemExit
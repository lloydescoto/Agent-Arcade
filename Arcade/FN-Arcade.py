import pygame
import random
pygame.init()

screen = pygame.display.set_mode((800,450))
def makeTextObjects(text,font):
    textSurface = font.render(text,True,(0,0,0))
    return textSurface, textSurface.get_rect()
def instructionMessage(text):
    smallText = pygame.font.SysFont("Arial",30)
    textSurf, textRect = makeTextObjects(text,smallText)
    textRect.center = (screen.get_width()/2,screen.get_height()/2)
    screen.blit(textSurf,textRect)
def killMessage(text):
    smallText = pygame.font.SysFont("Arial",30)
    textSurf, textRect = makeTextObjects(text,smallText)
    textRect.center = (50,20)
    screen.blit(textSurf,textRect)
def missMessage(text):
    smallText = pygame.font.SysFont("Arial",30)
    textSurf, textRect = makeTextObjects(text,smallText)
    textRect.center = (740,20)
    screen.blit(textSurf,textRect)
class Player(pygame.sprite.Sprite):
    rightImages = []
    leftImages = []
    punchRightImages = []
    punchLeftImages = []
    rightCounter = 1
    leftCounter = 1
    punchRightCounter = 1
    punchLeftCounter = 1
    direction = "Right"
    punching = False
    kills = 0
    miss = 0
    def __init__(self):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.image = self.rightImages[0]
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 390
    def update(self):
        keypress = pygame.key.get_pressed()
        self.punching = False
        if keypress[pygame.K_RIGHT]:
            self.rect.x += 5
            self.image = self.rightImages[self.rightCounter]
            self.rightCounter = (self.rightCounter + 1) % len(self.rightImages)
            self.direction = "Right"
        if keypress[pygame.K_LEFT]:
            self.rect.x -= 5
            self.image = self.leftImages[self.leftCounter]
            self.leftCounter = (self.leftCounter + 1) % len(self.leftImages)
            self.direction = "Left"
        if keypress[pygame.K_SPACE] and self.direction == "Right":
            self.image = self.punchRightImages[self.punchRightCounter]
            self.punchRightCounter = (self.punchRightCounter + 1) % len(self.punchRightImages)
            self.punching = True
        if keypress[pygame.K_SPACE] and self.direction == "Left":
            self.image = self.punchLeftImages[self.punchLeftCounter]
            self.punchLeftCounter = (self.punchLeftCounter + 1) % len(self.punchLeftImages)
            self.punching = True
class Obstacle(pygame.sprite.Sprite):
    direction = "None"
    def __init__(self):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.image = pygame.Surface((50,50))
        self.image = self.image.convert()
        self.image.fill((0,0,0))
        pygame.draw.rect(self.image,(0,255,0),(50,50,50,50))
        self.rect = self.image.get_rect()
        if random.randrange(0,2) % 2:
            self.direction = "Right"
            self.rect.y = 400
            self.rect.x = screen.get_height()+300
        else:
            self.direction = "Left"
            self.rect.y = 400
            self.rect.x = 0
    def update(self):
        if self.direction == "Right":
            self.rect.x -= 5
            if self.rect.x < 0:
                self.kill()
        else:
            self.rect.x += 5
            if self.rect.x > screen.get_width():
                self.kill()

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
Player.rightImages.append((pygame.image.load("agent1.png")))
Player.leftImages.append(pygame.transform.flip(Player.rightImages[0],True,False))
Player.rightImages.append(pygame.image.load("agent2.png"))
Player.leftImages.append(pygame.transform.flip(Player.rightImages[1],True,False))
Player.rightImages.append(pygame.image.load("agent3.png"))
Player.leftImages.append(pygame.transform.flip(Player.rightImages[2],True,False))
Player.rightImages.append(pygame.image.load("agent4.png"))
Player.leftImages.append(pygame.transform.flip(Player.rightImages[3],True,False))
Player.rightImages.append(pygame.image.load("agent5.png"))
Player.leftImages.append(pygame.transform.flip(Player.rightImages[4],True,False))
Player.rightImages.append(pygame.image.load("agent6.png"))
Player.leftImages.append(pygame.transform.flip(Player.rightImages[5],True,False))
Player.rightImages.append(pygame.image.load("agent7.png"))
Player.leftImages.append(pygame.transform.flip(Player.rightImages[6],True,False))
Player.rightImages.append(pygame.image.load("agent8.png"))
Player.leftImages.append(pygame.transform.flip(Player.rightImages[7],True,False))
Player.punchRightImages.append(pygame.image.load("agentpunch1.png"))
Player.punchLeftImages.append(pygame.transform.flip(Player.punchRightImages[0],True,False))
Player.punchRightImages.append(pygame.image.load("agentpunch2.png"))
Player.punchLeftImages.append(pygame.transform.flip(Player.punchRightImages[1],True,False))
clock = pygame.time.Clock()
keepGoing = True
obstacles = pygame.sprite.Group()
allSprite = pygame.sprite.RenderUpdates()
Player.containers = allSprite
Obstacle.containers = allSprite, obstacles
player = Player()
background = Background("Summer.jpg",[0,0])
while keepGoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
    if random.randrange(0,100) < 2:
        obstacles.add(Obstacle())
    screen.fill((255,255,255))
    screen.blit(background.image,background.rect)
    instructionMessage("[Press Space to Punch][Left and Right Arrown Keys to Move]")
    killMessage("Kills : " + str(player.kills))
    missMessage("Miss : " + str(player.miss))
    allSprite.update()
    allSprite.draw(screen)
    for obs in pygame.sprite.spritecollide(player,obstacles,0):
        if obs.direction == player.direction and player.punching:
            obs.kill()
            player.kills += 1
        else:
            obs.kill()
            player.miss += 1
    pygame.display.flip()
    clock.tick(30)
pygame.quit()



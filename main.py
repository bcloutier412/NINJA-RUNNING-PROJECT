import pygame, sys

pygame.init()

# CREATING THE GAME WINDOW
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("NINJA RUNNER")
clock = pygame.time.Clock()
FPS = 120


class Background:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        background_image = pygame.image.load('DarkForest.jpg')
        self.background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    def draw(self):
        screen.blit(self.background_image, (self.x, self.y))


class Player:
    def __init__(self):
        self.jump = True
        self.animation_list = []
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        for i in range(10):
            player_image = pygame.image.load(f'img/Run__{i + 1}.png')
            player_image = pygame.transform.scale(player_image, [int(player_image.get_width() / 4),
                                                                  int(player_image.get_height() / 4)])
            self.animation_list.append(player_image)
        self.player_image = self.animation_list[self.frame_index]
        self.rect = self.player_image.get_rect()
        self.rect.center = (200, 600)
        self.isJump = False
        self.jumpCounter = 0
        self.jump = False
        self.gravity = 0.65
        self.vel_y = 0

    def movement(self):
        dy = 0
        #Jump
        if self.jump:
            self.vel_y = -17
            self.jump = False

        #apply gravity
        self.vel_y += self.gravity
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        #check collision with floor
        if self.rect.bottom + dy > 643:
            dy = 644 - self.rect.bottom
            self.jumpCounter = 0
        #updating the rectangle position
        self.rect.y += dy
    def update_animation(self):
        #update animation
        ANIMATION_COOLDOWN = 100
        #update image depending on the current frame
        self.player_image = self.animation_list[self.frame_index]
        #check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # if the animation has run out reset back to the start
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0

    def draw(self):
        screen.blit(self.player_image, self.rect)


def createSurfaces():
    # SCREEN MOVEMENT
    background_1.draw()
    background_2.draw()
    background_1.x -= 2
    background_2.x -= 2
    if background_1.x < -1280:
        background_1.x = 0
    if background_2.x < 0:
        background_2.x = 1280
    # PLAYER DRAW
    player.draw()


background_1 = Background(0, 0)
background_2 = Background(1280, 0)
player = Player()
while True:
    clock.tick(FPS)
    screen.fill((0, 0, 0))
    createSurfaces()
    player.movement()
    player.update_animation()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player.jumpCounter <= 1:
                player.jump = True
                player.jumpCounter += 1

    userInput = pygame.key.get_pressed()
    pygame.display.update()

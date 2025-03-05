from pygame import * #очень важно!!1
game = True
window = display.set_mode((700 , 500))
class Sprite(sprite.Sprite):
    def __init__(self, filename, x, y, speed, long, width):
        super().__init__()
        self.image = transform.scale(image.load(filename), (width, long))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.width = width
        self.long = long
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y ))
player = Sprite('images/player.png', 0,100,4,100,65)
treasure = Sprite('images/treasure.png', 615,450,0,50,60)
enemy = Sprite('images/enemy.png',600,20,0,100,60)
walls = sprite.Group(
Sprite('images/wall.png', 200, 100,0,280,10),
Sprite('images/wall.png', 200, 380,0,10,250),
Sprite('images/wall.png', 100, 100,0,500,10),
Sprite('images/wall.png', 550, 230,0,400,10),
Sprite('images/wall.png', 450, 100,0,290,10),
Sprite('images/wall.png', 450,100,0,10,250)
)
clock = time.Clock()
display.set_caption('лабиринт')
background = transform.scale(image.load('images/background.jpg'),(700, 500))
counter = 0
while game:
    window.blit(background, (0,0))
    player.reset()
    treasure.reset()
    enemy.reset()
    walls.draw(window)
    for e in event.get():
        if e.type == QUIT:
            game = False
    keys = key.get_pressed()
    keys[K_UP]
    if keys[K_UP] and player.rect.y > 0:
        player.rect.y = player.rect.y - 2
    if keys[K_DOWN] and player.rect.y <= 400:
        player.rect.y = player.rect.y + 2
    if keys[K_LEFT] and player.rect.x > 0:
        player.rect.x = player.rect.x - 2
    if keys[K_RIGHT] and player.rect.x <= 600:
        player.rect.x = player.rect.x + 2
    if sprite.spritecollide(player, walls, False):
        break
    if player.rect.colliderect(treasure.rect):
        background = transform.scale(image.load('images/win.jpg'), (700, 500))
        walls.empty()
        treasure.rect.x = player.rect.x + 40
        treasure.rect.y = player.rect.y + 40
    if counter == 1:
        counter = 0
        if enemy.rect.x > player.rect.x:
            enemy.rect.x -= 1
        if enemy.rect.x < player.rect.x:
            enemy.rect.x += 1
        if enemy.rect.y < player.rect.y:
            enemy.rect.y += 1
        if enemy.rect.y > player.rect.y:
            enemy.rect.y -= 1
        if player.rect.colliderect(enemy.rect):
            break
    else:
        counter += 1
    display.update()
    clock.tick(144)
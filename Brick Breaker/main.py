import pygame 
import sys
import random

pygame.init()

# Dimension 
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Brick Breaker")

clock = pygame.time.Clock()

# paddle
pw = 120
ph = 30
px = width//2 - pw
py = height - ph - 20
paddle = pygame.Rect(px,py,pw,ph)
ps = 7

# Ball
bx = width//2
by = height//2 + 30
size = 15
ball = pygame.Rect(bx,by,size*2,size*2)
bsx = 4
bsy = -4

# Bricks
br = 5
bc = 8
bw = width // bc
bh = 30
bco = (100,200,255)

score = 0


bricks = []
for row in range(br):
    for col in range(bc):
        if random.choice([True, False]):  # 50% chance to place a brick
            brick_x = col * bw
            brick_y = row * bh + 50
            brick = pygame.Rect(brick_x + 5, brick_y + 5, bw - 10, bh - 10)
            bricks.append(brick)



def go():
    font = pygame.font.Font(None, 36)
    text = font.render(f"Game over", True, (255, 255, 255))
    screen.blit(text, (width//2 - text.get_width()//2, height//2 - text.get_height()//2))
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

running = True 
while running:
    clock.tick(60)
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Keys Handling 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= ps
    if keys[pygame.K_RIGHT] and paddle.right < width:
        paddle.x += ps

    ball.x += bsx
    ball.y += bsy

    if ball.left < 0 or ball.right >= width:
        bsx *= -1
    if ball.top < 0:
        bsy *= -1

    if ball.colliderect(paddle):
        bsy *= -1
        ball.bottom = paddle.top
    

    if ball.bottom >= height:
        go()

    for brick in bricks[:]:
        if ball.colliderect(brick):
            bsy *= -1
            bricks.remove(brick)
            score += 1
            break
        
    for brick in bricks:
        pygame.draw.rect(screen, bco, brick)

    # Draw the score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))




    pygame.draw.ellipse(screen, (255, 100, 100), ball)
    pygame.draw.rect(screen, (200,200,200), paddle)
    
    pygame.display.flip()

pygame.quit()
sys.exit()
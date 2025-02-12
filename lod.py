import pygame

pygame.init()

WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ovládání trojúhelníku")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

x = WIDTH // 2
y = HEIGHT - 50
speed = 5  

bullets = []
bullet_speed = 7

running = True
while running:
    pygame.time.delay(20)
    screen.fill(WHITE)
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x - 15 > 0:
        x -= speed
    
    if keys[pygame.K_RIGHT] and x + 15 < WIDTH:
        x += speed

    points = [(x, y), (x + 15, y + 30), (x - 15, y + 30)]
    pygame.draw.polygon(screen, BLACK, points)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append([x, y - 10])
                
    for bullet in bullets:
        bullet[1] -= bullet_speed  

    bullets = [bullet for bullet in bullets if bullet[1] > 0]

    points = [(x, y), (x + 15, y + 30), (x - 15, y + 30)]
    pygame.draw.polygon(screen, BLACK, points)

    for bullet in bullets:
        pygame.draw.circle(screen, BLUE, (bullet[0], bullet[1]), 5)

    pygame.display.update()

pygame.quit()

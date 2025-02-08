import pygame

pygame.init()

WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ovládání trojúhelníku")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

x = WIDTH // 2
y = HEIGHT - 50
speed = 5  

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

pygame.quit()

import pygame
import random
import math
import time

pygame.init()
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ovládání trojúhelníku")

#Změna pozadí :3--------------------------------------------------
#background = pygame.image.load("pozadi_vesmir.png")              
#background = pygame.transform.scale(background, (WIDTH, HEIGHT)) 
                                                                  
#background = pygame.image.load("sakura_pozadí.png")               
#background = pygame.transform.scale(background, (WIDTH, HEIGHT))  
                                                                  
#background = pygame.image.load("mesto_pozadi.png")               
#background = pygame.transform.scale(background, (WIDTH, HEIGHT))

background = pygame.image.load("spagety.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
                                                                  
#Změna skinu  :D--------------------------------------------------
#rocket_img = pygame.image.load("raketa_new.png") 
#rocket_img = pygame.transform.scale(rocket_img, (60, 80))

rocket_img = pygame.image.load("raketa_new_01.png")
rocket_img = pygame.transform.scale(rocket_img, (60, 80))

#rocket_img = pygame.image.load("kebab_new.png")
#rocket_img = pygame.transform.scale(rocket_img, (60, 80))
#Změna meteoritu---------------------------------------------------
meteor_img = pygame.image.load("meteorit.png")  
meteor_img = pygame.transform.scale(meteor_img, (80, 80))

#meteor_img = pygame.image.load("meteorit_2.png")
#meteor_img = pygame.transform.scale(meteor_img, (80, 80))
#-----------------------------------------------------------------

WHITE = (255, 255, 255)
BLACK = (255, 255, 255)
BLUE = (0, 255, 0)
BROWN = (238, 203, 173)
RED = (255, 0, 0)

x = WIDTH // 2
y = HEIGHT - 50
speed = 5  

bullets = []
bullet_speed = 9
enemies = []
enemy_speed = 2
score = 0

shield_active = False
shield_start_time = 0
font = pygame.font.Font(None, 36)

font = pygame.font.Font(None, 36)

for _ in range(5):
    enemy_x = random.randint(20, WIDTH - 20)  
    enemy_y = random.randint(20, 100)         
    enemies.append([enemy_x, enemy_y])
    
def reset_enemy(enemy):
    enemy[0] = random.randint(20, WIDTH - 20)
    enemy[1] = random.randint(-50, -10)

def is_collision(obj1, obj2, radius=40):
    distance = math.hypot(obj1[0] - obj2[0], obj1[1] - obj2[1])
    return distance < radius

running = True
game_over = False
clock = pygame.time.Clock() 
while running:
    clock.tick(60)
    
    if game_over: 

        screen.fill(BLACK)
        game_over_text = font.render("GAME OVER", True, RED)
        score_text = font.render(f"Skóre: {score}", True, RED)
        screen.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2 - 40))
        screen.blit(score_text, (WIDTH // 2 - 50, HEIGHT // 2 + 10))
        restart_text = font.render("Stiskni 'R' pro restart", True, WHITE)
        screen.blit(restart_text, (WIDTH // 2 - 120, HEIGHT // 2 + 50))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:

                    game_over = False
                    score = 0
                    x = WIDTH // 2
                    y = HEIGHT - 50
                    enemies = []
                    bullets = []
                    for _ in range(5):
                        enemy_x = random.randint(20, WIDTH - 20)  
                        enemy_y = random.randint(20, 100)         
                        enemies.append([enemy_x, enemy_y])
                        
        continue
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x - 15 > 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x + 15 < WIDTH:
        x += speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append([x, y - 10])
                
    screen.blit(background, (0, 0))
    screen.blit(rocket_img, (x - 15, y))
    
    if shield_active and time.time() - shield_start_time > 5:  
        shield_active = False 
    
    for enemy in enemies:
        if not shield_active and is_collision((x, y), enemy, 40):
            game_over = True
            break 
    
    for bullet in bullets:
        bullet[1] -= bullet_speed
        
    for enemy in enemies:
        enemy[1] += enemy_speed  
        if enemy[1] > HEIGHT:  
            reset_enemy(enemy)

        if not shield_active and is_collision((x, y), enemy, 40):
            game_over = True

    bullets = [bullet for bullet in bullets if bullet[1] > 0]

    for bullet in bullets[:]:  
        for enemy in enemies[:]:
            if is_collision(bullet, enemy):
                bullets.remove(bullet)  
                enemies.remove(enemy)
                score += 1
                break 

    points = [(x, y), (x + 15, y + 30), (x - 15, y + 30)]
    
    if score % 10 == 0 and score > 0 and not shield_active:
        shield_active = True
        shield_start_time = time.time()
    
    if shield_active:
        pygame.draw.circle(screen, BLUE, (x, y + 30), 40, 3)
    
    for bullet in bullets:
        pygame.draw.circle(screen, BLUE, (bullet[0], bullet[1]), 5)

    for enemy in enemies:
        screen.blit(meteor_img, (enemy[0] - 40, enemy[1] - 40))

    if not enemies:
        for _ in range(10):
            enemy_x = random.randint(20, WIDTH - 20)
            enemy_y = random.randint(20, 100)
            enemies.append([enemy_x, enemy_y])
            
    score_text = font.render(f"Skóre: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    pygame.display.update()

pygame.quit()
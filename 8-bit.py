import pygame
import random

pygame.init()

res = (1080, 720)
screen = pygame.display.set_mode(res)
clock = pygame.time.Clock()

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
startl = (169, 169, 169)  
startd = (100, 100, 100)  


smallfont = pygame.font.SysFont('Corbel', 35)
largefont = pygame.font.SysFont('Corbel', 50)

player_c = random.choice([red, green, blue])
lead_x = 40
lead_y = res[1] // 2
player_size = 40


enemy_size = 50
e_p = [res[0], random.randint(50, res[1] - 50)]  # Enemy 1 position
e1_p = [random.randint(res[0], res[0] + 100), random.randint(50, res[1] - 50)]  # Enemy 2 position

# Game variables
count = 0 
speed = 15

# Function to display game over screen
def game_over():
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 100 < mouse_pos[0] < 140 and res[1] - 100 < mouse_pos[1] < res[1] - 80:
                    pygame.quit()
                if res[0] - 180 < mouse_pos[0] < res[0] - 100 and res[1] - 100 < mouse_pos[1] < res[1] - 80:
                    game(lead_x, lead_y, speed, count)

        screen.fill((65, 25, 64)) 
        game_over_text = smallfont.render('GAME OVER', True, white)
        restart_text = smallfont.render('Restart', True, white)
        exit_text = smallfont.render('Exit', True, white)
        screen.blit(game_over_text, (res[0] // 2 - 150, 295))

        # Draw exit button
        mouse_pos = pygame.mouse.get_pos()
        if 100 < mouse_pos[0] < 140 and res[1] - 100 < mouse_pos[1] < res[1] - 80:
            pygame.draw.rect(screen, startl, [100, res[1] - 100, 40, 20])
        else:
            pygame.draw.rect(screen, startd, [100, res[1] - 100, 40, 20])

        # Draw restart button
        if res[0] - 180 < mouse_pos[0] < res[0] - 100 and res[1] - 100 < mouse_pos[1] < res[1] - 80:
            pygame.draw.rect(screen, startl, [res[0] - 180, res[1] - 100, 80, 20])
        else:
            pygame.draw.rect(screen, startd, [res[0] - 180, res[1] - 100, 80, 20])

        screen.blit(restart_text, (res[0] - 180, res[1] - 100))
        screen.blit(exit_text, (100, res[1] - 100))

        pygame.display.update()


# Function for the main game loop
def game(lead_x, lead_y, speed, count):
    global e_p, e1_p

    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            lead_y -= 10
        if keys[pygame.K_DOWN]:
            lead_y += 10

        # Fill background color
        screen.fill((65, 25, 64))
        clock.tick(speed)

        # Draw player (a rectangle)
        pygame.draw.rect(screen, player_c, [lead_x, lead_y, player_size, player_size])

        # Draw the enemies
        pygame.draw.rect(screen, red, [e_p[0], e_p[1], enemy_size, enemy_size])
        pygame.draw.rect(screen, blue, [e1_p[0], e1_p[1], enemy_size, enemy_size])

        # Update enemy positions
        if e_p[0] > 0:
            e_p[0] -= 10
        else:
            e_p[0] = res[0]
            e_p[1] = random.randint(50, res[1] - 50)

        if e1_p[0] > 0:
            e1_p[0] -= 10
        else:
            e1_p[0] = res[0] + 100
            e1_p[1] = random.randint(50, res[1] - 50)

     
        if lead_x <= e_p[0] <= lead_x + player_size and lead_y <= e_p[1] <= lead_y + player_size:
            game_over()

        if lead_x <= e1_p[0] <= lead_x + player_size and lead_y <= e1_p[1] <= lead_y + player_size:
            e1_p[0] = res[0] + 100 
            count += 1  # Increase score
            speed += 1  # Increase speed

        # Display score
        score_text = smallfont.render(f'Score: {count}', True, white)
        screen.blit(score_text, (res[0] - 120, res[1] - 40))

        # Update the screen
        pygame.display.update()


# Intro screen with instructions and "Start" button
def intro():
    instructions_shown = False  
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.fill((65, 25, 64)) 
        mouse_pos = pygame.mouse.get_pos()

        if not instructions_shown:
            instructions_title = largefont.render("Speed Escape - Instructions", True, white)
            instructions_text1 = smallfont.render("1. Use UP and DOWN arrows to move.", True, white)
            instructions_text2 = smallfont.render("2. Avoid the red enemies.", True, white)
            instructions_text3 = smallfont.render("3. Score points by colliding blue friend.", True, white)
            instructions_text4 = smallfont.render("4. Speed increases with each score.", True, white)
            instructions_text5 = smallfont.render("5. Game ends if you collide with an enemy.", True, white)

            screen.blit(instructions_title, (res[0] // 2 - 180, 50))
            screen.blit(instructions_text1, (res[0] // 2 - 200, 150))
            screen.blit(instructions_text2, (res[0] // 2 - 200, 190))
            screen.blit(instructions_text3, (res[0] // 2 - 200, 230))
            screen.blit(instructions_text4, (res[0] // 2 - 200, 270))
            screen.blit(instructions_text5, (res[0] // 2 - 200, 310))

            if 300 < mouse_pos[0] < 420 and 400 < mouse_pos[1] < 440:
                pygame.draw.rect(screen, startl, [300, 400, 120, 40]) 
            else:
                pygame.draw.rect(screen, startd, [300, 400, 120, 40]) 

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 300 < mouse_pos[0] < 420 and 400 < mouse_pos[1] < 440:
                    instructions_shown = True 
                    continue  # Skip drawing instructions

        if instructions_shown:
            # Draw the "Start" button
            if 300 < mouse_pos[0] < 420 and 290 < mouse_pos[1] < 330:
                pygame.draw.rect(screen, startl, [300, 290, 120, 40])
            else:
                pygame.draw.rect(screen, startd, [300, 290, 120, 40])

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 300 < mouse_pos[0] < 420 and 290 < mouse_pos[1] < 330:
                    game(lead_x, lead_y, speed, count)

            # Draw the text "Start"
            text = smallfont.render('Start', True, white)

            screen.blit(text, (320, 295))

        pygame.display.update()


intro()

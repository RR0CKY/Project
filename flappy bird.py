import pygame
import sys
import random

# Pygame initialize karein
pygame.init()

# Game Constants (Hard Difficulty Configuration)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
GRAVITY = 0.20         # Tezi se neeche girne ke liye (Normal: 0.25)
FLAP_STRENGTH = -4.0     # Jump ki taqat
PIPE_SPEED = 4           # Pipes ki speed tezi se badhai hai (Normal: 3)
PIPE_GAP = 300          # Pipes ke beech ka gap chota kiya hai (Normal: 150+)
PIPE_FREQUENCY = 1200   # Naye pipes jaldi aayenge (milliseconds)

# Colors
WHITE = (255, 255, 255)
SKY_BLUE = (113, 197, 207)
BIRD_YELLOW = (247, 216, 54)
PIPE_GREEN = (115, 191, 46)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird - HARD MODE')
clock = pygame.time.Clock()

class Bird:
    def __init__(self):
        self.x = 80
        self.y = SCREEN_HEIGHT // 2
        self.velocity = 0
        self.radius = 15

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity
        
        # Screen se baahar jaane par lock lagana
        if self.y < self.radius:
            self.y = self.radius
            self.velocity = 0

    def draw(self):
        pygame.draw.circle(screen, BIRD_YELLOW, (self.x, int(self.y)), self.radius)
        # Bird ki aankh (visual look ke liye)
        pygame.draw.circle(screen, (0, 0, 0), (self.x + 6, int(self.y) - 4), 3)

class Pipe:
    def __init__(self):
        # Pipe ki height randomly select hogi
        self.top_height = random.randint(50, SCREEN_HEIGHT - PIPE_GAP - 100)
        self.bottom_height = SCREEN_HEIGHT - self.top_height - PIPE_GAP
        self.x = SCREEN_WIDTH
        self.width = 60
        self.passed = False

    def update(self):
        self.x -= PIPE_SPEED

    def draw(self):
        # Top Pipe
        pygame.draw.rect(screen, PIPE_GREEN, (self.x, 0, self.width, self.top_height))
        # Bottom Pipe
        pygame.draw.rect(screen, PIPE_GREEN, (self.x, SCREEN_HEIGHT - self.bottom_height, self.width, self.bottom_height))

def check_collision(bird, pipes):
    # Zameen ya aasmaan se takrana
    if bird.y + bird.radius >= SCREEN_HEIGHT:
        return True

    # Pipes se takrana
    for pipe in pipes:
        # Check if bird is within pipe's X boundaries
        if pipe.x < bird.x + bird.radius and pipe.x + pipe.width > bird.x - bird.radius:
            # Top pipe ya bottom pipe se collision check
            if bird.y - bird.radius < pipe.top_height or bird.y + bird.radius > SCREEN_HEIGHT - pipe.bottom_height:
                return True
    return False

def main():
    bird = Bird()
    pipes = []
    score = 0
    game_active = False
    font = pygame.font.SysFont('Arial', 32, bold=True)
    
    # Custom event for pipe generation
    spawn_pipe_event = pygame.USEREVENT
    pygame.time.set_timer(spawn_pipe_event, PIPE_FREQUENCY)

    while True:
        screen.fill(SKY_BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not game_active:
                        # Game reset loop
                        bird = Bird()
                        pipes = [Pipe()]
                        score = 0
                        game_active = True
                    else:
                        bird.flap()

            if event.type == spawn_pipe_event and game_active:
                pipes.append(Pipe())

        if game_active:
            bird.update()
            bird.draw()

            for pipe in pipes[:]:
                pipe.update()
                pipe.draw()

                # Score update jab pipe cross ho jaye
                if not pipe.passed and pipe.x + pipe.width < bird.x:
                    pipe.passed = True
                    score += 1

                # Purane pipes list se hatayein taaki computer slow na ho
                if pipe.x + pipe.width < 0:
                    pipes.remove(pipe)

            # Check Game Over
            if check_collision(bird, pipes):
                game_active = False

            # Display Current Score
            score_text = font.render(f'Score: {score}', True, WHITE)
            screen.blit(score_text, (10, 10))
        else:
            # Start / Game Over Screen UI
            if score == 0:
                start_text = font.render('Press SPACE to Start', True, WHITE)
                mode_text = font.render('MODE: HARD', True, (200, 0, 0))
                screen.blit(start_text, (60, SCREEN_HEIGHT // 2 - 20))
                screen.blit(mode_text, (120, SCREEN_HEIGHT // 2 + 30))
            else:
                game_over_text = font.render('GAME OVER', True, (200, 0, 0))
                final_score_text = font.render(f'Final Score: {score}', True, WHITE)
                restart_text = font.render('Press SPACE to Retry', True, WHITE)
                
                screen.blit(game_over_text, (110, SCREEN_HEIGHT // 2 - 60))
                screen.blit(final_score_text, (110, SCREEN_HEIGHT // 2 - 10))
                screen.blit(restart_text, (65, SCREEN_HEIGHT // 2 + 40))
            
            bird.draw()

        pygame.display.update()
        clock.tick(60) # 60 FPS

if __name__ == '__main__':
    main()
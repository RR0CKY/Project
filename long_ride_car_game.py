import pygame
import sys
import random

# Pygame initialize karein
pygame.init()

# Screen Dimensions
SCREEN_WIDTH = 200
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("The Long Highway - 10,000m Race")
clock = pygame.time.Clock()

# Colors
GRAY = (50, 50, 50)
WHITE = (255, 255, 255)
RED = (220, 20, 60)
BLUE = (30, 144, 255)
YELLOW = (255, 215, 0)
GREEN = (34, 139, 34)

# Game Configurations
PLAYER_SPEED = 7
ENEMY_SPEED = 6
TOTAL_DISTANCE = 1000  # Finish line ki doori (Bohut zyada door)

class PlayerCar:
    def __init__(self):
        self.width = 45
        self.height = 80
        self.x = SCREEN_WIDTH // 2 - self.width // 2
        self.y = SCREEN_HEIGHT - 120
        
    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 80: # Left boundary
            self.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and self.x < SCREEN_WIDTH - 80 - self.width: # Right boundary
            self.x += PLAYER_SPEED

    def draw(self):
        # Blue Car Body
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height), border_radius=5)
        # Windows & Wheels
        pygame.draw.rect(screen, WHITE, (self.x + 5, self.y + 15, self.width - 10, 20))
        pygame.draw.rect(screen, (0, 0, 0), (self.x - 5, self.y + 10, 5, 15))
        pygame.draw.rect(screen, (0, 0, 0), (self.x + self.width, self.y + 10, 5, 15))
        pygame.draw.rect(screen, (0, 0, 0), (self.x - 5, self.y + 55, 5, 15))
        pygame.draw.rect(screen, (0, 0, 0), (self.x + self.width, self.y + 55, 5, 15))

class EnemyCar:
    def __init__(self):
        self.width = 45
        self.height = 80
        # Road ke andar randomly spawn hoga
        self.x = random.randint(80, SCREEN_WIDTH - 80 - self.width)
        self.y = random.randint(-600, -100)
        
    def update(self):
        self.y += ENEMY_SPEED
        # Agar car screen se bahar nikal jaye toh dobara upar bhejein
        if self.y > SCREEN_HEIGHT:
            self.x = random.randint(80, SCREEN_WIDTH - 80 - self.width)
            self.y = random.randint(-300, -100)

    def draw(self):
        # Red Enemy Car
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height), border_radius=5)
        pygame.draw.rect(screen, (0, 0, 0), (self.x + 5, self.y + 25, self.width - 10, 15))

def main():
    player = PlayerCar()
    enemies = [EnemyCar(), EnemyCar(), EnemyCar()]
    
    distance_covered = 0
    road_stripe_y = 0
    game_state = "START" # START, PLAYING, GAMEOVER, WON
    font = pygame.font.SysFont("Arial", 24, bold=True)

    while True:
        keys = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if game_state in ["START", "GAMEOVER", "WON"]:
                    # Game Reset Logic
                    player = PlayerCar()
                    enemies = [EnemyCar(), EnemyCar(), EnemyCar()]
                    distance_covered = 0
                    game_state = "PLAYING"

        if game_state == "PLAYING":
            player.move(keys)
            
            # Distance tracker (Har frame car aage badhegi)
            distance_covered += 2 
            
            # Check Win Condition
            if distance_covered >= TOTAL_DISTANCE:
                game_state = "WON"

            # Road stripes animation effect
            road_stripe_y += ENEMY_SPEED
            if road_stripe_y > 40:
                road_stripe_y = 0

            # Background & Road Structure
            screen.fill(GREEN) # Side ki ghaas
            pygame.draw.rect(screen, GRAY, (70, 0, SCREEN_WIDTH - 140, SCREEN_HEIGHT)) # Main Road
            pygame.draw.rect(screen, WHITE, (70, 0, 5, SCREEN_HEIGHT)) # Left Line
            pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH - 75, 0, 5, SCREEN_HEIGHT)) # Right Line

            # Center Yellow Strips
            for y in range(-40, SCREEN_HEIGHT, 40):
                pygame.draw.rect(screen, YELLOW, (SCREEN_WIDTH // 2 - 2, y + road_stripe_y, 4, 20))

            # Enemies update aur collision check
            player_rect = pygame.Rect(player.x, player.y, player.width, player.height)
            for enemy in enemies:
                enemy.update()
                enemy.draw()
                
                enemy_rect = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)
                if player_rect.colliderect(enemy_rect):
                    game_state = "GAMEOVER"

            player.draw()

            # UI Text (Distance left)
            remaining_dist = max(0, TOTAL_DISTANCE - distance_covered)
            ui_text = font.render(f"Distance Left: {remaining_dist}m", True, WHITE)
            screen.blit(ui_text, (15, 15))

        else:
            # Menu Screens (Start / Over / Won)
            screen.fill((0, 0, 0))
            if game_state == "START":
                msg = font.render("THE LONG HIGHWAY (10,000m)", True, YELLOW)
                sub = font.render("Press SPACE to Start Driving", True, WHITE)
            elif game_state == "GAMEOVER":
                msg = font.render("CRASHED! Game Over", True, RED)
                sub = font.render("Press SPACE to Restart", True, WHITE)
            elif game_state == "WON":
                msg = font.render("VICTORY! You Finished the 10,000m Ride", True, GREEN)
                sub = font.render("Press SPACE to Play Again", True, WHITE)

            screen.blit(msg, (SCREEN_WIDTH // 2 - msg.get_width() // 2, SCREEN_HEIGHT // 2 - 30))
            screen.blit(sub, (SCREEN_WIDTH // 2 - sub.get_width() // 2, SCREEN_HEIGHT // 2 + 10))

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
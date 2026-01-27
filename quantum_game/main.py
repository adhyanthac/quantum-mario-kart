import pygame
import random

# --- CONFIGURATION ---
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 800
LANE_WIDTH = SCREEN_WIDTH // 4
LANE_X = [i * LANE_WIDTH + (LANE_WIDTH // 4) for i in range(4)]
FPS = 60

# Colors
COLOR_BG = (5, 5, 20)
COLOR_PLAYER = (0, 255, 200)
COLOR_OBSTACLE = (255, 50, 100)
COLOR_TEXT = (255, 255, 255)
COLOR_FINISH = (255, 215, 0)

class QuantumVehicle:
    def __init__(self):
        self.reset()

    def reset(self):
        self.amplitudes = [0.0, 1.0, 0.0, 0.0]
        self.q_score = 0
        self.start_ticks = pygame.time.get_ticks()

    def apply_hadamard(self):
        if max(self.amplitudes) > 0.9:
            self.amplitudes = [0.707, 0.0, 0.0, 0.707]
        else:
            self.measure(None) # Manual collapse

    def shift(self, direction):
        if direction == "right":
            self.amplitudes = [self.amplitudes[-1]] + self.amplitudes[:-1]
        else:
            self.amplitudes = self.amplitudes[1:] + [self.amplitudes[0]]

    def measure(self, obstacles):
        probs = [a**2 for a in self.amplitudes]
        is_superposition = max(self.amplitudes) < 0.9
        
        choice = random.choices([0, 1, 2, 3], weights=probs)[0]
        
        # Calculate Score Bonus if near obstacles
        if obstacles and is_superposition:
            for obs in obstacles:
                dist = abs(500 - obs[1])
                if dist < 200: # If collapse happened near a threat
                    multiplier = 2.0 if is_superposition else 0.5
                    self.q_score += int((1000 / (dist + 1)) * multiplier)

        self.amplitudes = [0.0, 0.0, 0.0, 0.0]
        self.amplitudes[choice] = 1.0

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Consolas", 18)
    
    car = QuantumVehicle()
    obstacles = [] 
    frame = 0
    # Finish line set to ~45 seconds of gameplay (60fps * 45 = 2700 frames)
    # At speed 4, distance 10000 works well.
    distance_to_finish = 10000 
    game_state = "PLAYING" # PLAYING, WON, CRASHED

    while True:
        screen.fill(COLOR_BG)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); return
            if event.type == pygame.KEYDOWN:
                if game_state == "PLAYING":
                    if event.key == pygame.K_h: car.apply_hadamard()
                    elif event.key == pygame.K_d: car.shift("right")
                    elif event.key == pygame.K_a: car.shift("left")
                    elif event.key == pygame.K_SPACE: car.measure(obstacles)
                elif event.key == pygame.K_r:
                    car.reset()
                    obstacles, distance_to_finish, frame, game_state = [], 10000, 0, "PLAYING"

        if game_state == "PLAYING":
            frame += 1
            distance_to_finish -= 4 # Finish line approaches
            
            if frame % 60 == 0:
                blocked = random.sample([0, 1, 2, 3], random.randint(1, 2))
                obstacles.append([blocked, -50])
            
            if distance_to_finish <= 0:
                game_state = "WON"

            for obs in obstacles[:]:
                obs[1] += 8
                if 500 < obs[1] < 560:
                    for lane in obs[0]:
                        if car.amplitudes[lane]**2 > 0.1:
                            game_state = "CRASHED"
                if obs[1] > 800: obstacles.remove(obs)

        # Draw Finish Line
        if distance_to_finish < SCREEN_HEIGHT:
            pygame.draw.rect(screen, COLOR_FINISH, (0, SCREEN_HEIGHT - distance_to_finish, SCREEN_WIDTH, 50))

        # Draw Lanes, Obstacles, and Car
        for x in range(0, SCREEN_WIDTH + 1, LANE_WIDTH):
            pygame.draw.line(screen, (40, 40, 70), (x, 0), (x, SCREEN_HEIGHT))
        for obs in obstacles:
            for lane in obs[0]:
                pygame.draw.rect(screen, COLOR_OBSTACLE, (LANE_X[lane]-10, obs[1], 60, 40))

        for i, amp in enumerate(car.amplitudes):
            p = amp**2
            if p > 0.01:
                s = pygame.Surface((40, 60), pygame.SRCALPHA)
                pygame.draw.rect(s, (*COLOR_PLAYER, int(p*255)), (0, 0, 40, 60), border_radius=8)
                screen.blit(s, (LANE_X[i], 500))
            pygame.draw.rect(screen, (60, 60, 90), (LANE_X[i], 720, 40, 40), 1)
            pygame.draw.rect(screen, COLOR_PLAYER, (LANE_X[i], 760-(p*40), 40, p*40))

        # UI
        if game_state == "PLAYING":
            screen.blit(font.render(f"Goal: {max(0, distance_to_finish//100)}m | Score: {car.q_score}", True, COLOR_TEXT), (20, 20))
        else:
            txt = "YOU WON" if game_state == "WON" else "GAME OVER"
            col = COLOR_FINISH if game_state == "WON" else COLOR_OBSTACLE
            screen.blit(font.render(txt, True, col), (210, 300))
            screen.blit(font.render(f"FINAL QUANTUM SCORE: {car.q_score}", True, COLOR_TEXT), (180, 350))
            screen.blit(font.render("Press R to Restart", True, (150, 150, 150)), (210, 400))
        
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
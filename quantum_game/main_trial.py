import pygame
import random
import asyncio

# --- CONFIGURATION ---
WIDTH, HEIGHT = 1200, 800  # Wider for 4 players + UI
FPS = 60

# Player Theme Colors
PLAYER_THEMES = [
    {"bg": (30, 10, 10), "car": (255, 50, 50), "btn": (150, 0, 0), "name": "Player 1"},
    {"bg": (10, 10, 30), "car": (50, 50, 255), "btn": (0, 0, 150), "name": "Player 2"},
    {"bg": (10, 30, 10), "car": (50, 255, 50), "btn": (0, 150, 0), "name": "Player 3"},
    {"bg": (30, 10, 30), "car": (200, 50, 255), "btn": (100, 0, 100), "name": "Player 4"}
]

class QuantumVehicle:
    def __init__(self, player_idx):
        self.idx = player_idx
        self.reset()
        
    def reset(self):
        self.amplitudes = [0.0, 1.0, 0.0, 0.0]
        self.alive = True
        self.score = 0
        self.frames_alive = 0
        self.successful_measures = 0

    def apply_hadamard(self):
        if not self.alive: return
        if max(self.amplitudes) > 0.9:
            idx = self.amplitudes.index(max(self.amplitudes))
            self.amplitudes[idx] = 0.707
            self.amplitudes[(idx + 1) % 4] = 0.707
        else:
            self.measure()

    def shift(self, direction):
        if not self.alive: return
        if direction == "right":
            self.amplitudes = [self.amplitudes[-1]] + self.amplitudes[:-1]
        else:
            self.amplitudes = self.amplitudes[1:] + [self.amplitudes[0]]

    def measure(self):
        if not self.alive: return
        probs = [a**2 for a in self.amplitudes]
        if max(self.amplitudes) < 0.9: self.successful_measures += 1
        choice = random.choices([0, 1, 2, 3], weights=probs)[0]
        self.amplitudes = [0.0] * 4
        self.amplitudes[choice] = 1.0

    def update_score(self):
        if self.alive:
            self.frames_alive += 1
            # Math: (Survival Time * 1) + (Successful Measure Multiplier)
            self.score = (self.frames_alive // 10) + (self.successful_measures * 50)

class Button:
    def __init__(self, x, y, w, h, text, color, action_val=None):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.color = color
        self.action_val = action_val

    def draw(self, surf, font):
        pygame.draw.rect(surf, self.color, self.rect, border_radius=8)
        pygame.draw.rect(surf, (255, 255, 255), self.rect, 2, border_radius=8) # Border
        txt = font.render(self.text, True, (255, 255, 255))
        surf.blit(txt, (self.rect.centerx - txt.get_width()//2, self.rect.centery - txt.get_height()//2))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

async def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Quantum Arena - Xu Research Group")
    font = pygame.font.SysFont("Consolas", 16)
    title_font = pygame.font.SysFont("Consolas", 50)
    clock = pygame.time.Clock()
    
    state = "MENU" # MENU, PLAYING, LEADERBOARD
    players = []
    num_players = 1
    obstacles = []
    frame = 0

    # MENU BUTTONS
    menu_btns = [
        Button(WIDTH//2 - 100, 300, 200, 50, "1 PLAYER", (50, 50, 50), 1),
        Button(WIDTH//2 - 100, 370, 200, 50, "2 PLAYERS", (50, 50, 50), 2),
        Button(WIDTH//2 - 100, 440, 200, 50, "4 PLAYERS", (50, 50, 50), 4)
    ]

    while True:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if state == "MENU":
                    for btn in menu_btns:
                        if btn.is_clicked(mouse_pos):
                            num_players = btn.action_val
                            players = [QuantumVehicle(i) for i in range(num_players)]
                            p_width = WIDTH // num_players
                            # RE-GENERATE GAME BUTTONS
                            game_btns = []
                            for i in range(num_players):
                                bx = i * p_width
                                col = PLAYER_THEMES[i]["btn"]
                                game_btns.append({
                                    "H": Button(bx + 10, 740, 50, 40, "H", col),
                                    "L": Button(bx + 70, 740, 50, 40, "<", col),
                                    "R": Button(bx + 130, 740, 50, 40, ">", col),
                                    "M": Button(bx + 190, 740, 90, 40, "MEASURE", col)
                                })
                            obstacles, frame, state = [], 0, "PLAYING"
                
                elif state == "PLAYING":
                    for i, p_btns in enumerate(game_btns):
                        if p_btns["H"].is_clicked(mouse_pos): players[i].apply_hadamard()
                        if p_btns["L"].is_clicked(mouse_pos): players[i].shift("left")
                        if p_btns["R"].is_clicked(mouse_pos): players[i].shift("right")
                        if p_btns["M"].is_clicked(mouse_pos): players[i].measure()

                elif state == "LEADERBOARD":
                    if pygame.Rect(WIDTH//2-100, 600, 200, 50).collidepoint(mouse_pos):
                        state = "MENU"

        # --- LOGIC ---
        if state == "MENU":
            screen.fill((10, 10, 20))
            title = title_font.render("QUANTUM ARENA", True, (0, 255, 200))
            screen.blit(title, (WIDTH//2 - title.get_width()//2, 150))
            for btn in menu_btns: btn.draw(screen, font)

        elif state == "PLAYING":
            frame += 1
            if frame % 60 == 0:
                blocked = random.sample([0, 1, 2, 3], random.randint(1, 2))
                obstacles.append([blocked, -50])

            for obs in obstacles[:]:
                obs[1] += 6
                for p in players:
                    if p.alive:
                        if 500 < obs[1] < 560:
                            for lane in obs[0]:
                                if p.amplitudes[lane]**2 > 0.1: p.alive = False
                    p.update_score()
                if obs[1] > 800: obstacles.remove(obs)

            # Draw Zones
            p_width = WIDTH // num_players
            for i, p in enumerate(players):
                bx = i * p_width
                theme = PLAYER_THEMES[i]
                pygame.draw.rect(screen, theme["bg"], (bx, 0, p_width, HEIGHT))
                pygame.draw.line(screen, (100, 100, 100), (bx, 0), (bx, HEIGHT), 1)
                
                for obs in obstacles:
                    for lane in obs[0]:
                        ox = bx + (lane * (p_width // 4)) + 15
                        pygame.draw.rect(screen, (255, 50, 100), (ox, obs[1], 40, 40), border_radius=4)

                if p.alive:
                    for l_idx, amp in enumerate(p.amplitudes):
                        prob = amp**2
                        if prob > 0:
                            cx = bx + (l_idx * (p_width // 4)) + 15
                            s = pygame.Surface((40, 50), pygame.SRCALPHA)
                            pygame.draw.rect(s, (*theme["car"], int(prob*255)), (0, 0, 40, 50), border_radius=5)
                            screen.blit(s, (cx, 500))
                    # Probability Bars
                    for l_idx, amp in enumerate(p.amplitudes):
                        px = bx + (l_idx * (p_width // 4)) + 15
                        pygame.draw.rect(screen, (50, 50, 50), (px, 680, 40, 40), 1)
                        pygame.draw.rect(screen, theme["car"], (px, 720-(amp**2*40), 40, amp**2*40))
                else:
                    msg = font.render("DECOHERENCE CRASH", True, (255, 50, 50))
                    screen.blit(msg, (bx + p_width//2 - msg.get_width()//2, 400))

                score_txt = font.render(f"SCORE: {p.score}", True, (255, 255, 255))
                screen.blit(score_txt, (bx + 10, 10))
                for btn in game_btns[i].values(): btn.draw(screen, font)

            # Check if all players dead
            if all(not p.alive for p in players):
                state = "LEADERBOARD"

        elif state == "LEADERBOARD":
            screen.fill((5, 5, 10))
            lbl = title_font.render("FINAL RANKINGS", True, (255, 215, 0))
            screen.blit(lbl, (WIDTH//2 - lbl.get_width()//2, 100))
            
            # Sort players by score
            sorted_players = sorted(players, key=lambda x: x.score, reverse=True)
            for i, p in enumerate(sorted_players):
                col = PLAYER_THEMES[p.idx]["car"]
                p_name = PLAYER_THEMES[p.idx]["name"]
                row = font.render(f"{i+1}. {p_name} --- {p.score} QUANTUM PTS", True, col)
                screen.blit(row, (WIDTH//2 - 150, 250 + i*50))
            
            # Back to menu button
            Button(WIDTH//2-100, 600, 200, 50, "MAIN MENU", (100, 100, 100)).draw(screen, font)

        pygame.display.flip()
        await asyncio.sleep(0)
        clock.tick(FPS)

if __name__ == "__main__":
    asyncio.run(main())
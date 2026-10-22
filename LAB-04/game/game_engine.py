import random
from collections import Counter, deque
import pygame
from .button import Button

BG = (18, 24, 40)
PANEL = (29, 38, 59)
TEXT = (241, 245, 255)
MUTED = (169, 181, 204)
GREEN = (70, 190, 135)
RED = (232, 91, 105)
GOLD = (255, 199, 84)
MOVES = ("ROCK", "PAPER", "SCISSORS")
BEATS = {"ROCK": "SCISSORS", "SCISSORS": "PAPER", "PAPER": "ROCK"}
COUNTER = {"ROCK": "PAPER", "PAPER": "SCISSORS", "SCISSORS": "ROCK"}
ICONS = {"ROCK": "rock", "PAPER": "paper", "SCISSORS": "scissors"}


class GameEngine:
    def __init__(self, width, height, target_score=5):
        self.width, self.height = width, height
        self.target_score = target_score
        self.player_score = 0
        self.cpu_score = 0
        self.player_pick = None
        self.cpu_pick = None
        self.result = "Choose your move"
        self.result_color = TEXT
        self.round_timer = 0.0
        self.reveal_timer = 0.0
        self.phase = "ready"  # ready, reveal, result, game_over
        self.history = deque(maxlen=8)
        self.message = "First to 5 points wins • CPU learns your recent patterns"
        self.font = pygame.font.SysFont("arial", 24, bold=True)
        self.small = pygame.font.SysFont("arial", 17)
        self.title_font = pygame.font.SysFont("arial", 36, bold=True)
        self.icon_font = pygame.font.SysFont("segoeuisymbol", 66)
        self.buttons = [
            Button((100, 430, 180, 64), "ROCK", (67, 112, 210), "ROCK"),
            Button((310, 430, 180, 64), "PAPER", (128, 91, 199), "PAPER"),
            Button((520, 430, 180, 64), "SCISSORS", (202, 91, 120), "SCISSORS"),
        ]

    def determine_winner(self, player, cpu):
        """Return PLAYER, CPU, or DRAW using standard RPS rules."""
        if player == cpu:
            return "DRAW"
        return "PLAYER" if BEATS[player] == cpu else "CPU"

    def choose_cpu_move(self):
        """Use random play until there is enough history, then bias against the most common move."""
        if len(self.history) < 3:
            return random.choice(MOVES)
        counts = Counter(self.history)
        most_common, frequency = counts.most_common(1)[0]
        # Adapt only when a pattern is reasonably clear; otherwise stay unpredictable.
        if frequency >= 3 and frequency / len(self.history) >= 0.45 and random.random() < 0.72:
            return COUNTER[most_common]
        return random.choice(MOVES)

    def play(self, move):
        if self.phase == "game_over":
            return
        self.player_pick = move
        self.cpu_pick = self.choose_cpu_move()
        self.history.append(move)
        self.phase = "reveal"
        self.reveal_timer = 0.65
        self.round_timer = 0
        self.result = "Ready..."
        self.result_color = GOLD

    def finish_round(self):
        outcome = self.determine_winner(self.player_pick, self.cpu_pick)
        if outcome == "PLAYER":
            self.player_score += 1
            self.result, self.result_color = "You win this round!", GREEN
        elif outcome == "CPU":
            self.cpu_score += 1
            self.result, self.result_color = "CPU wins this round", RED
        else:
            self.result, self.result_color = "It's a draw!", GOLD
        self.phase = "result"
        self.round_timer = 1.8
        if self.player_score >= self.target_score or self.cpu_score >= self.target_score:
            self.phase = "game_over"
            self.result = "YOU WIN THE MATCH!" if self.player_score >= self.target_score else "CPU WINS THE MATCH"
            self.result_color = GREEN if self.player_score >= self.target_score else RED

    def reset(self):
        self.player_score = self.cpu_score = 0
        self.player_pick = self.cpu_pick = None
        self.result = "Choose your move"
        self.result_color = TEXT
        self.round_timer = self.reveal_timer = 0
        self.phase = "ready"
        self.history.clear()
        self.message = "Match reset • First to 5 points wins"

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r and self.phase == "game_over":
            self.reset()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.phase == "game_over":
                return
            for button in self.buttons:
                if button.clicked(event.pos) and self.phase == "ready":
                    self.play(button.value)
                    break

    def update(self, dt):
        if self.phase == "reveal":
            self.reveal_timer -= dt
            if self.reveal_timer <= 0:
                self.finish_round()
        elif self.phase == "result":
            self.round_timer -= dt
            if self.round_timer <= 0:
                self.player_pick = self.cpu_pick = None
                self.phase = "ready"
                self.result = "Choose your move"
                self.result_color = TEXT

    def draw_icon(self, surface, move, center, shake=0):
        x, y = center
        x += shake
        if move is None:
            pygame.draw.circle(surface, (68, 80, 105), (x, y), 39, 3)
            return
        if move == "ROCK":
            points = [(x-29,y-9),(x-18,y-30),(x+10,y-34),(x+31,y-12),(x+24,y+22),(x+2,y+32),(x-25,y+19)]
            pygame.draw.polygon(surface, (139, 155, 180), points)
            pygame.draw.polygon(surface, (225, 233, 247), points, 3)
            pygame.draw.line(surface, (91, 108, 137), (x-12,y-7),(x+12,y+9),3)
        elif move == "PAPER":
            rect = pygame.Rect(x-25,y-34,50,68)
            pygame.draw.rect(surface, (246, 248, 255), rect, border_radius=4)
            pygame.draw.rect(surface, (124, 148, 190), rect, 3, border_radius=4)
            for yy in (y-14,y,y+14):
                pygame.draw.line(surface, (124, 148, 190), (x-14,yy),(x+14,yy),2)
        else:
            pygame.draw.line(surface, (225, 233, 247), (x-22,y-29),(x+20,y+25),9)
            pygame.draw.line(surface, (225, 233, 247), (x+22,y-29),(x-20,y+25),9)
            pygame.draw.line(surface, (150, 170, 205), (x-22,y-29),(x+20,y+25),3)
            pygame.draw.line(surface, (150, 170, 205), (x+22,y-29),(x-20,y+25),3)
            pygame.draw.circle(surface, GOLD, (x,y+7), 7)

    def render(self, surface):
        surface.fill(BG)
        title = self.title_font.render("ROCK  •  PAPER  •  SCISSORS", True, TEXT)
        surface.blit(title, title.get_rect(center=(self.width//2, 45)))
        subtitle = self.small.render("ADAPTIVE DUEL", True, MUTED)
        surface.blit(subtitle, subtitle.get_rect(center=(self.width//2, 78)))
        pygame.draw.rect(surface, PANEL, (70, 105, self.width-140, 70), border_radius=16)
        score = self.font.render(f"YOU   {self.player_score}     —     {self.cpu_score}   CPU", True, TEXT)
        surface.blit(score, score.get_rect(center=(self.width//2, 140)))
        surface.blit(self.small.render(f"First to {self.target_score}", True, GOLD), (self.width-150, 124))
        # Choice panels
        for x, label in ((220,"YOUR MOVE"),(580,"CPU MOVE")):
            pygame.draw.rect(surface, PANEL, (x-125, 195, 250, 160), border_radius=18)
            t = self.small.render(label, True, MUTED)
            surface.blit(t, t.get_rect(center=(x, 216)))
        shake = int(random.uniform(-5,5)) if self.phase == "reveal" and int(self.reveal_timer*20)%2 else 0
        self.draw_icon(surface, self.player_pick, (220, 275), shake)
        self.draw_icon(surface, self.cpu_pick, (580, 275), -shake)
        if self.phase == "reveal":
            msg = "3  •  2  •  1  •  REVEAL!"
            color = GOLD
        else:
            msg, color = self.result, self.result_color
        res = self.font.render(msg, True, color)
        surface.blit(res, res.get_rect(center=(self.width//2, 382)))
        for button in self.buttons:
            button.draw(surface, self.font, pygame.mouse.get_pos(), enabled=self.phase == "ready")
        footer = self.small.render(self.message, True, MUTED)
        surface.blit(footer, footer.get_rect(center=(self.width//2, 520)))
        if self.phase == "game_over":
            overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            overlay.fill((5, 8, 18, 175))
            surface.blit(overlay, (0,0))
            banner = self.title_font.render(self.result, True, self.result_color)
            surface.blit(banner, banner.get_rect(center=(self.width//2, 240)))
            restart = self.font.render("Press R to play again", True, TEXT)
            surface.blit(restart, restart.get_rect(center=(self.width//2, 295)))
            final = self.small.render(f"Final score: You {self.player_score} — {self.cpu_score} CPU", True, MUTED)
            surface.blit(final, final.get_rect(center=(self.width//2, 330)))

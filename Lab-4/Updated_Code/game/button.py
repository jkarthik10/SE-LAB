import pygame


class Button:
    def __init__(self, rect, label, color, value):
        self.rect = pygame.Rect(rect)
        self.label = label
        self.color = color
        self.value = value

    def draw(self, surface, font, mouse_pos, enabled=True):
        hovered = self.rect.collidepoint(mouse_pos) and enabled
        color = tuple(min(255, int(c * 1.14)) for c in self.color) if hovered else self.color
        if not enabled:
            color = (95, 99, 110)
        pygame.draw.rect(surface, color, self.rect, border_radius=14)
        pygame.draw.rect(surface, (235, 240, 250), self.rect, 2, border_radius=14)
        text = font.render(self.label, True, (255, 255, 255))
        surface.blit(text, text.get_rect(center=self.rect.center))

    def clicked(self, pos):
        return self.rect.collidepoint(pos)

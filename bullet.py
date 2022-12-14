import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets shot from the ship."""

    def __init__(self, ai_game):
        """Create bullet object at current ship's position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0, 0) and then set the correct position.
        self.rect = pygame.Rect(0,0, self.settings.bullet_height, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store bullet's position at decimal value
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up to the screen."""
        # Update the decimal positions of the bullet
        self.y -= self.settings.bullet_speed
        # Update the rectangle position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet on the screen."""
        pygame.draw.circle(self.screen, self.color, (self.rect.x, self.rect.y), self.settings.bullet_height)


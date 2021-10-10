import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""A class to represent a single alien in the fleet."""

	def __init__(self, ai_settings, screen):
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		#load gambar alien
		self.image = pygame.image.load('images/musuh.png')
		self.rect = self.image.get_rect()

		#bikin alien
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#Lokasi alien
		self.x = float(self.rect.x)


	def blitme(self):
		"""Draw the alien at its current location."""
		self.screen.blit(self.image, self.rect)


	def check_edges(self):
		"""Return True if alien is at edge of screen."""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right - 10:
			return True
		elif self.rect.left <= 10:
			return True

	def update(self):
		"""Move the alien right or left."""
		self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
		self.rect.x = self.x


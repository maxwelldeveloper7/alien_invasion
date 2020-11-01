import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
	# Inicializa o pygame, as configurações e objeto screen
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_heght))
	pygame.display.set_caption("Alien Invasion")
	# Cria uma espaçonave, um grupo de projéteis e um grupo de alienígenas
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()
	# Cria uma frota de alienígenas
	gf.create_fleet(ai_settings, screen, aliens)
	#Inicia o laço principal do jogo
	while True:
		gf.check_events(ai_settings, screen, ship, alien, bullets)
		ship.update()
		bullets.update()
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings, screen, ship, alien, bullets)

run_game()

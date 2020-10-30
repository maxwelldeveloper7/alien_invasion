import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	# Inicializa o pygame, as configurações e objeto screen
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_heght))
	pygame.display.set_caption("Alien Invasion")
	# Cria uma espaçonave
	ship = Ship(ai_settings, screen)
	#Inicia o laço principal do jogo
	while True:
		ship.update()
		gf.check_events(ship)
		gf.update_screen(ai_settings, screen, ship)

run_game()

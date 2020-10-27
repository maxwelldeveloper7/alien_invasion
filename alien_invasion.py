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
	ship = Ship(screen)
	# Define a cor de fundo
	bg_color = (230, 230, 230)
	#Inicia o laço principal do jogo
	while True:
		gf.check_events()
		gf.update_screen(ai_settings, screen, ship)
run_game()

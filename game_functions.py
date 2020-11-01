from bullet import Bullet
import sys
import pygame
from alien import Alien

def check_events(ai_settings, screen, ship, alien, bullets):
	"""Responde a eventos de pressionamento de teclas e de mouse"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		check_keydown_events(event, ai_settings, screen, ship, bullets)
		check_keyup_events(event, ship)
		
def check_keydown_events(event, ai_settings, screen, ship, bullets):
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_RIGHT:
			ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			ship.moving_left = True
		elif event.key == pygame.K_SPACE:
			fire_bullet(ai_settings, screen, ship, bullets)
		elif event.key == pygame.K_q:
			sys.exit()

def check_keyup_events(event, ship):
	if event.type == pygame.KEYUP:
		if event.key == pygame.K_RIGHT:
			ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			ship.moving_left = False

def update_screen(ai_settings, screen, ship, alien, bullets):
	"""Atualiza as imagens na tela e alterna para nova tela."""
	# Redesenha a tela a cada passagem pelo laço
	screen.fill(ai_settings.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	alien.blitme()
	# Deixa a tela mais recente visível
	pygame.display.flip()

def update_bullets(bullets):
	"""Atualiza a posição dos projéteis e se livra dos projéteis 
	antigos"""
	# Livrar-se dos projéties que desapareceram
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
	"""Dispara um projétil se o limite ainda não foi alcançado"""
	# Cria um novo projétil e o adiciona ao grupo de projéteis
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

def create_fleet(ai_settings, screen, aliens):
	"""Cria uma fota completa de alienígenas."""
	# Cria um alienígena e calcula o número de alienígenas em uma linha
	# O espaçamento entre os alienígenas é igual à largura de um alieníg
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	avalilable_space_x = ai_settings.screen_width - 2 * alien_width
	numbers_aliens_x = int(avalilable_space_x / (2 * alien_width))
	# Cria a primeira linha de alienígenas
	for alien_number in range(numbers_aliens_x):
		# Cria um alienígena e o posiciona na linha
		alien = Alien(ai_settings, screen)
		alien.x = alien_width + 2
		aliens.add(alien)

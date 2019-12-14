import pygame
import time
import json
import random
import pickle
from save_game_func import *

save_game = cont_game()

#iniate pygame
pygame.init()
 
#set game display
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Tamagochi")

#color value
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

#nyantaro size
witdh_nyan = int(display_width * 0.35)
height_nyan = int(display_height * 0.37)

#load image
nyantaro_img = pygame.image.load('asset/KYET/Kyet (1).png')
nyantaro_img = pygame.transform.smoothscale(nyantaro_img, (witdh_nyan, height_nyan))
nyantaro_img2 = pygame.image.load('asset/KYET/Kyet Phase 2 (1).png')
nyantaro_img2 = pygame.transform.smoothscale(nyantaro_img2, (witdh_nyan, height_nyan))
car_width = 73

def button(x_t,y_t,w,h,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x_t+w > mouse[0] > x_t and y_t+h > mouse[1] > y_t:
        pygame.draw.rect(gameDisplay, red,(x_t,y_t,w,h))
        if click[0] == 1 and action != None:
            action()

def gui(type):
	x_gu = display_width
	y_gu = display_height
	if type == 'home':
		#Shop Icon	
		shop_con = pygame.image.load('asset/Shop_Icon.png')
		shop_con = pygame.transform.smoothscale(shop_con, (int(witdh_nyan * 0.55), int(height_nyan * 0.50)))
		gameDisplay.blit(shop_con, (int(display_width * 0.80),int(display_height * 0.001)))
		button(int(display_width * 0.85),int(display_height * 0.04),int(height_nyan * 0.45),int(witdh_nyan * 0.18),shop_loop)

		mg_con = pygame.image.load('asset/Minigames_Icon.png')
		mg_con = pygame.transform.smoothscale(mg_con, (int(witdh_nyan * 0.55), int(height_nyan * 0.50)))
		gameDisplay.blit(mg_con, (int(display_width * 0.80),int(display_height * 0.10)))
		button(int(display_width * 0.85),int(display_height * 0.14),int(height_nyan * 0.45),int(witdh_nyan * 0.18),mg_loop)


		Food_con = pygame.image.load('asset/Food Bar/Food Bar Content (1).png')
		Food_con = pygame.transform.smoothscale(Food_con, (int(int(witdh_nyan * 2)*save_game['food_level']/100), int(height_nyan * 0.35)))
		Food_bar = pygame.image.load('asset/Food Bar/Food Bar Border (1).png')
		Food_bar = pygame.transform.smoothscale(Food_bar, (int(witdh_nyan * 2), int(height_nyan * 0.35)))
		gameDisplay.blit(Food_con, (int(display_width * 0.009),int(display_height * 0.026)))
		gameDisplay.blit(Food_bar, (int(display_width * 0.003),int(display_height * 0.001)))
		br_bar = pygame.image.load('asset/Brain Bar/Brain Bar Content (1).png')
		br_bar = pygame.transform.smoothscale(br_bar, (int(int(witdh_nyan * 2)*save_game['brain_power']/100), int(height_nyan * 0.35)))
		start_con = pygame.image.load('asset/Brain Bar/Brain Bar Border (1).png')
		start_con = pygame.transform.smoothscale(start_con, (int(witdh_nyan * 2), int(height_nyan * 0.35)))
		gameDisplay.blit(br_bar, (int(display_width * 0.009),int(display_height * 0.141)))
		gameDisplay.blit(start_con, (int(display_width * 0.003),int(display_height * 0.115)))

		feed_con = pygame.image.load('asset/ICONS/Feed Icon.png')
		feed_con = pygame.transform.smoothscale(feed_con, (int(witdh_nyan * 0.20), int(height_nyan * 0.27)))
		gameDisplay.blit(feed_con, (int(display_width * 0.55),int(display_height * 0.45)))
		button(int(display_width * 0.55),int(display_height * 0.45),int(height_nyan * 0.27),int(witdh_nyan * 0.20))

		sett_con = pygame.image.load('asset/ICONS/Settings Icon.png')
		sett_con = pygame.transform.smoothscale(sett_con, (int(witdh_nyan * 0.45), int(height_nyan * 0.25)))
		gameDisplay.blit(sett_con, (int(display_width * 0.01),int(display_height * 0.90)))
		button(int(display_width * 0.02),int(display_height * 0.90),int(height_nyan * 0.50),int(witdh_nyan * 0.18),sett_loop)

	elif type == "shop":
		Home_con = pygame.image.load('asset/ICONS/Home Icon.png')
		Home_con = pygame.transform.smoothscale(Home_con, (int(witdh_nyan * 0.35), int(height_nyan * 0.25)))
		gameDisplay.blit(Home_con, (int(display_width * 0.03),int(display_height * 0.01)))
		button(int(display_width * 0.03),int(display_height * 0.009),int(height_nyan * 0.50),int(witdh_nyan * 0.20),game_loop)

	elif type == "MG":
		Home_con = pygame.image.load('asset/ICONS/Home Icon.png')
		Home_con = pygame.transform.smoothscale(Home_con, (int(witdh_nyan * 0.35), int(height_nyan * 0.25)))
		gameDisplay.blit(Home_con, (int(display_width * 0.03),int(display_height * 0.01)))
		button(int(display_width * 0.03),int(display_height * 0.009),int(height_nyan * 0.50),int(witdh_nyan * 0.20),game_loop)

		HGN_con = pygame.image.load('asset/Minigame/Lobby Icons/Hangman.png')
		HGN_con = pygame.transform.smoothscale(HGN_con, (int(witdh_nyan * 1.1), int(height_nyan * 1.1)))
		gameDisplay.blit(HGN_con, (int(display_width * 0.01),int(display_height * 0.2)))
		button(int(display_width * 0.12),int(display_height * 0.25),int(height_nyan * 0.7),int(witdh_nyan * 0.8),game_loop)

#draw BG
def bg(bg,floor=None):
	BG = pygame.image.load('asset/%s.png' % bg)
	BG = pygame.transform.smoothscale(BG, (display_width, display_height))
	if floor != None :
		floor = pygame.image.load('asset/%s.png' % floor)
		floor = pygame.transform.smoothscale(floor, (display_width, display_height))

		gameDisplay.blit(floor, (0,0))
	
	gameDisplay.blit(BG, (0,0))

#draw card function
def nyantaro(x,y,frame):
	if frame % 2 != 0:
		gameDisplay.blit(nyantaro_img, (x,y))
	else:
		gameDisplay.blit(nyantaro_img2, (x,y))

clock = pygame.time.Clock()

car_speed = 0

def food_stuff():
	if save_game['food_level'] > 0:
		save_game['food_level'] = int(save_game['food_level']) - 1

def br_stuff():
	if save_game['brain_power'] > 0:
		save_game['brain_power'] = int(save_game['brain_power']) - 1

def general_room_stuff():
	for event in pygame.event.get():
		if event.type == pygame.USEREVENT:
			food_stuff()
		if event.type == pygame.USEREVENT+1:
			br_stuff()
		if event.type == pygame.USEREVENT+2:
			print(save_game['food_level'])
			save1 = json.dumps(save_game)
			pickle.dump(save1, open("save_game.pickle", "wb"))
		if event.type == pygame.QUIT:
			print(save_game['food_level'])
			save1 = json.dumps(save_game)
			pickle.dump(save1, open("save_game.pickle", "wb"))
			gameExit = True
			return gameExit
		print(event)

pygame.time.set_timer(pygame.USEREVENT+1, 600000)
pygame.time.set_timer(pygame.USEREVENT+2, 60000)
pygame.time.set_timer(pygame.USEREVENT, 60000)
def game_loop():

	x =  (display_width * 0.30)
	y = (display_height * 0.50)

	x_change = 0
	
	frame_v = 1

	gameExit = False

	while not gameExit:
		
		frame_v += 1

		gameExit = general_room_stuff()
	
		#event for moving object
		'''if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_change = -5
			elif event.key == pygame.K_RIGHT:
				x_change = 5
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				x_change = 0'''
	
		x += x_change
	
		#fill background with white	
		bg('bg','floor')
		#gui('home')
		#Draw Obstacle
		#things(thing_startx, thing_starty, thing_width, thing_height, black)
		#thing_starty += thing_speed
		#draw a car in x y coordinate
		nyantaro(x,y,frame_v)
		gui('home')
	
		pygame.display.update()
		clock.tick(60)

def shop_loop():
	#Car info
	x =  (display_width * 0.30)
	y = (display_height * 0.50)

	x_change = 0
	
	frame_v = 1

	gameExit = False

	while not gameExit:
		
		frame_v += 1

		general_room_stuff()
	
		#event for moving object
		'''if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_change = -5
			elif event.key == pygame.K_RIGHT:
				x_change = 5
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				x_change = 0'''
	
		x += x_change
	
		#fill background with white	
		bg('ShopBGType2')
		#gui('home')
		#Draw Obstacle
		#things(thing_startx, thing_starty, thing_width, thing_height, black)
		#thing_starty += thing_speed
		#draw a car in x y coordinate
		gui('shop')
	
		pygame.display.update()
		clock.tick(60)

def sett_loop():
	#Car info
	x =  (display_width * 0.30)
	y = (display_height * 0.50)

	x_change = 0
	
	frame_v = 1

	gameExit = False

	while not gameExit:
		
		frame_v += 1

		general_room_stuff()
	
		#event for moving object
		'''if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_change = -5
			elif event.key == pygame.K_RIGHT:
				x_change = 5
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				x_change = 0'''
	
		x += x_change
	
		#fill background with white	
		bg('BG_Settings_2')
		#gui('home')
		#Draw Obstacle
		#things(thing_startx, thing_starty, thing_width, thing_height, black)
		#thing_starty += thing_speed
		#draw a car in x y coordinate
		gui('shop')
	
		pygame.display.update()
		clock.tick(60)

def mg_loop():
	x =  (display_width * 0.30)
	y = (display_height * 0.50)

	x_change = 0
	
	frame_v = 1

	gameExit = False

	while not gameExit:
		
		frame_v += 1

		gameExit = general_room_stuff()
	
		#event for moving object
		'''if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_change = -5
			elif event.key == pygame.K_RIGHT:
				x_change = 5
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				x_change = 0'''
	
		x += x_change
	
		#fill background with white	
		bg('Nimp_Background')
		#gui('home')
		#Draw Obstacle
		#things(thing_startx, thing_starty, thing_width, thing_height, black)
		#thing_starty += thing_speed
		#draw a car in x y coordinate
		gui('MG')
	
		pygame.display.update()
		clock.tick(60)
mg_loop()
pygame.quit()
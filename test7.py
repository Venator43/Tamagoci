import pygame
import pygame_functions
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

surface = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Tamagochi")

#color value
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

#nyantaro size
witdh_nyan = int(display_width * 0.35)
height_nyan = int(display_height * 0.37)

#load image
nyantaro_img = pygame.image.load('asset/KYET/Kyet_Jump.png')
nyantaro_img = pygame.transform.smoothscale(nyantaro_img, (witdh_nyan, height_nyan))
nyantaro_img2 = pygame.image.load('asset/KYET/Kyet Phase 2 (1).png')
nyantaro_img2 = pygame.transform.smoothscale(nyantaro_img2, (witdh_nyan, height_nyan))
car_width = 73

def button(x_t,y_t,w,h,action,param=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x_t+w > mouse[0] > x_t and y_t+h > mouse[1] > y_t:
        if click[0] == 1 and action != None:
            action(param)

    #pygame.draw.rect(surface, red,(x_t,y_t,w,h))

def gui(type):
	x_gu = display_width
	y_gu = display_height
	if type == 'home':
		#Shop Icon	
		shop_con = pygame.image.load('asset/Shop_Icon.png')
		shop_con = pygame.transform.smoothscale(shop_con, (int(witdh_nyan * 0.55), int(height_nyan * 0.50)))
		surface.blit(shop_con, (int(display_width * 0.80),int(display_height * 0.001)))
		button(int(display_width * 0.85),int(display_height * 0.04),int(height_nyan * 0.45),int(witdh_nyan * 0.18),shop_loop)

		mg_con = pygame.image.load('asset/Minigames_Icon.png')
		mg_con = pygame.transform.smoothscale(mg_con, (int(witdh_nyan * 0.55), int(height_nyan * 0.50)))
		surface.blit(mg_con, (int(display_width * 0.80),int(display_height * 0.10)))
		button(int(display_width * 0.85),int(display_height * 0.14),int(height_nyan * 0.45),int(witdh_nyan * 0.18),mg_loop)


		Food_con = pygame.image.load('asset/Food Bar/Food Bar Content (1).png')
		Food_con = pygame.transform.smoothscale(Food_con, (int(int(witdh_nyan * 2)*save_game['food_level']/100), int(height_nyan * 0.35)))
		Food_bar = pygame.image.load('asset/Food Bar/Food Bar Border (1).png')
		Food_bar = pygame.transform.smoothscale(Food_bar, (int(witdh_nyan * 2), int(height_nyan * 0.35)))
		surface.blit(Food_con, (int(display_width * 0.009),int(display_height * 0.026)))
		surface.blit(Food_bar, (int(display_width * 0.003),int(display_height * 0.001)))
		br_bar = pygame.image.load('asset/Brain Bar/Brain Bar Content (1).png')
		br_bar = pygame.transform.smoothscale(br_bar, (int(int(witdh_nyan * 2)*save_game['brain_power']/100), int(height_nyan * 0.35)))
		start_con = pygame.image.load('asset/Brain Bar/Brain Bar Border (1).png')
		start_con = pygame.transform.smoothscale(start_con, (int(witdh_nyan * 2), int(height_nyan * 0.35)))
		surface.blit(br_bar, (int(display_width * 0.009),int(display_height * 0.141)))
		surface.blit(start_con, (int(display_width * 0.003),int(display_height * 0.115)))

		feed_con = pygame.image.load('asset/ICONS/Feed Icon.png')
		feed_con = pygame.transform.smoothscale(feed_con, (int(witdh_nyan * 0.20), int(height_nyan * 0.27)))
		surface.blit(feed_con, (int(display_width * 0.55),int(display_height * 0.45)))
		button(int(display_width * 0.55),int(display_height * 0.45),int(height_nyan * 0.27),int(witdh_nyan * 0.20))

		sett_con = pygame.image.load('asset/ICONS/Settings Icon.png')
		sett_con = pygame.transform.smoothscale(sett_con, (int(witdh_nyan * 0.45), int(height_nyan * 0.25)))
		surface.blit(sett_con, (int(display_width * 0.01),int(display_height * 0.90)))
		button(int(display_width * 0.02),int(display_height * 0.90),int(height_nyan * 0.50),int(witdh_nyan * 0.18),sett_loop)

		pygame.display.update()
	elif type == "shop":
		Home_con = pygame.image.load('asset/ICONS/Home Icon.png')
		Home_con = pygame.transform.smoothscale(Home_con, (int(witdh_nyan * 0.35), int(height_nyan * 0.25)))
		surface.blit(Home_con, (int(display_width * 0.03),int(display_height * 0.01)))
		button(int(display_width * 0.03),int(display_height * 0.009),int(height_nyan * 0.50),int(witdh_nyan * 0.20),game_loop)

		pygame.display.update()
	elif type == "MG":
		largeText = pygame.font.Font('freesansbold.ttf',20) 

		Home_con = pygame.image.load('asset/ICONS/Home Icon.png')
		Home_con = pygame.transform.smoothscale(Home_con, (int(witdh_nyan * 0.35), int(height_nyan * 0.25)))
		surface.blit(Home_con, (int(display_width * 0.03),int(display_height * 0.01)))
		button(int(display_width * 0.03),int(display_height * 0.009),int(height_nyan * 0.50),int(witdh_nyan * 0.20),game_loop)

		hangnyan_text = largeText.render('HangNyan', True, black)
		HGN_con = pygame.image.load('asset/Minigame/Lobby Icons/Hangman.png')
		HGN_con = pygame.transform.smoothscale(HGN_con, (int(witdh_nyan * 1.1), int(height_nyan * 1.1)))
		surface.blit(HGN_con, (int(display_width * 0.01),int(display_height * 0.2)))
		surface.blit(hangnyan_text, (int(display_width * 0.16),int(display_height * 0.56)))
		button(int(display_width * 0.12),int(display_height * 0.25),int(height_nyan * 0.7),int(witdh_nyan * 0.8),game_loop)

		ttc_text = largeText.render('Tic-Tac-Toe', True, black)
		ttc_con = pygame.image.load('asset/Minigame/Lobby Icons/TicTacToe.png')
		ttc_con = pygame.transform.smoothscale(ttc_con, (int(witdh_nyan * 0.8), int(height_nyan * 0.8)))
		surface.blit(ttc_con, (int(display_width * 0.39),int(display_height * 0.29)))
		surface.blit(ttc_text, (int(display_width * 0.46),int(display_height * 0.56)))
		button(int(display_width * 0.43),int(display_height * 0.25),int(height_nyan * 0.7),int(witdh_nyan * 0.8),game_loop)

		NIMP_text = largeText.render('NIMP', True, black)
		NIMP_con = pygame.image.load('asset/Minigame/Lobby Icons/NIMP_Icon.png')
		NIMP_con = pygame.transform.smoothscale(NIMP_con, (int(witdh_nyan * 1.1), int(height_nyan * 1.1)))
		surface.blit(NIMP_con, (int(display_width * 0.63),int(display_height * 0.26)))
		surface.blit(NIMP_text, (int(display_width * 0.80),int(display_height * 0.56)))
		button(int(display_width * 0.72),int(display_height * 0.25),int(height_nyan * 0.7),int(witdh_nyan * 0.8),nmp_loop)

		pygame.display.update()
#draw BG
def bg(bg,floor=None):
	BG = pygame.image.load('asset/%s.png' % bg)
	BG = pygame.transform.smoothscale(BG, (display_width, display_height))
	if floor != None :
		floor = pygame.image.load('asset/%s.png' % floor)
		floor = pygame.transform.smoothscale(floor, (display_width, display_height))

		surface.blit(floor, (0,0))
	
	surface.blit(BG, (0,0))

#draw card function
def nyantaro(x,y,frame):
	if frame % 2 != 0:
		surface.blit(nyantaro_img, (x,y))
	else:
		surface.blit(nyantaro_img2, (x,y))

clock = pygame.time.Clock()

car_speed = 0

def food_stuff():
	if save_game['food_level'] > 0:
		save_game['food_level'] = int(save_game['food_level']) - 1

def br_stuff():
	if save_game['brain_power'] > 0:
		save_game['brain_power'] = int(save_game['brain_power']) - 1

def general_room_stuff(mg = False):
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.USEREVENT:
			food_stuff()
		if event.type == pygame.USEREVENT+1 and mg == False:
			br_stuff()
		if event.type == pygame.USEREVENT+2:
			save1 = json.dumps(save_game)
			pickle.dump(save1, open("save_game.pickle", "wb"))
		if event.type == pygame.QUIT:
			save1 = json.dumps(save_game)
			pickle.dump(save1, open("save_game.pickle", "wb"))
			gameExit = True
			return gameExit
		print(event)

def nmp_button(num):
	n1 = num[1] - num[0]

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

def nmp_loop():
	x =  (display_width * 0.30)
	y = (display_height * 0.50)

	x_change = 0
	
	frame_v = 1

	n1 = 12
	n3=0
	if 85 >= save_game['brain_power']:
		n1 += 1
	gameExit = False
	user_turn = True
	while not gameExit:
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		frame_v += 1

		events = pygame.event.get()
		for event in events:
			if event.type == pygame.USEREVENT:
				food_stuff()
			if event.type == pygame.USEREVENT+2:
				save1 = json.dumps(save_game)
				pickle.dump(save1, open("save_game.pickle", "wb"))
			if event.type == pygame.QUIT:
				save1 = json.dumps(save_game)
				pickle.dump(save1, open("save_game.pickle", "wb"))
				gameExit = True
				return gameExit
			print(event)
	
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
		gameF = False
		#fill background with white	
		bg('Nimp_Background')
		
		n2 = 0
		for n in range(n1):
			NIMP_asset_cn = pygame.image.load('asset/Minigame/Nimp [Completed]/Coin.png')
			NIMP_asset_cn = pygame.transform.smoothscale(NIMP_asset_cn, (int(witdh_nyan * 0.9), int(height_nyan * 0.9)))
			if n2 >= 9:
				surface.blit(NIMP_asset_cn, (int(display_width * 0.005)*((n-n2)*19),int(display_height * 0.26)))
			else:
				n2 += 1
				surface.blit(NIMP_asset_cn, (int(display_width * 0.005)*(n*19),int(display_height * 0.06)))
		for num in range(1,4):
			NIMP_butto1_cn = pygame.image.load(f'asset/Minigame/Nimp [Completed]/button_{num}.png')
			NIMP_butto1_cn = pygame.transform.smoothscale(NIMP_butto1_cn, (int(witdh_nyan * 0.5), int(height_nyan * 0.5)))
			surface.blit(NIMP_butto1_cn, (int(display_width * 0.05)*(num*5),int(display_height * 0.6)))
		if user_turn == True and (int(display_width * 0.05)*(1*5)+int(height_nyan * 0.6)) > mouse[0] > (int(display_width * 0.05)*(1*5)) and int(display_height * 0.6)+int(witdh_nyan * 0.5) > mouse[1] > int(display_height * 0.6):
			if click[0] == 1:
				user_turn = False
				n1 -= 1
				n3 = 1
				print("test")
		if user_turn == True and (int(display_width * 0.05)*(2*5)+int(height_nyan * 0.6)) > mouse[0] > (int(display_width * 0.05)*(2*5)) and int(display_height * 0.6)+int(witdh_nyan * 0.5) > mouse[1] > int(display_height * 0.6):
			if click[0] == 1:
				user_turn = False
				n1 -= 2
				n3 = 2
		if user_turn == True and (int(display_width * 0.05)*(3*5)+int(height_nyan * 0.6)) > mouse[0] > (int(display_width * 0.05)*(3*5)) and int(display_height * 0.6)+int(witdh_nyan * 0.5) > mouse[1] > int(display_height * 0.6):
			if click[0] == 1:
				user_turn = False
				n1 -= 3
				n3 = 3

		pygame.display.update()

		if user_turn == False and n1 > 0:
			n1 -= (4-n3)
			user_turn = True
		if n1 == 0:
			if user_turn == True :
				print("ai won")
			elif user_turn == False:
				print("User won")

		pygame.display.update()
		clock.tick(60)
nmp_loop()
pygame.quit()
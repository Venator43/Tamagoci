import pygame
import pygame_textinput
import time
import json
import random
import numpy as np
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

date = date.today()
date = str(date)

#color value
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

if save_game['last_played'] == "10-15-1998" :
    save_game['last_played'] = date

date_old = save_game['last_played'].split('-')
date_new = date.split('-')

print(date_new)
print(date_old)
print(int(date_new[2])-int(date_old[2]))

if abs(int(date_new[2]) - int(date_old[2])) >= 7:
	save_game['food_level'] = 0
	save_game['brain_power'] = 0
	save_game['lost'] = 1

#nyantaro size
witdh_nyan = int(display_width * 0.35)
height_nyan = int(display_height * 0.37)

#load image
nyantaro_img = pygame.image.load('asset/KYET/Kyet_Jump.png')
nyantaro_img = pygame.transform.smoothscale(nyantaro_img, (witdh_nyan, height_nyan))
nyantaro_img2 = pygame.image.load('asset/KYET/Kyet Phase 2 (1).png')
nyantaro_img2 = pygame.transform.smoothscale(nyantaro_img2, (witdh_nyan, height_nyan))
if 25 > save_game['food_level'] and save_game['lost'] != 1:
	nyantaro_img = pygame.image.load('asset/KYET/Kyet_Angry.png')
	nyantaro_img = pygame.transform.smoothscale(nyantaro_img, (witdh_nyan, height_nyan))
	nyantaro_img2 = pygame.image.load('asset/KYET/Kyet_Angry.png')
	nyantaro_img2 = pygame.transform.smoothscale(nyantaro_img2, (witdh_nyan, height_nyan))
elif 10 > save_game['brain_power'] and save_game['lost'] != 1:
	nyantaro_img = pygame.image.load('asset/KYET/Kyet_Stupid.png')
	nyantaro_img = pygame.transform.smoothscale(nyantaro_img, (witdh_nyan, height_nyan))
	nyantaro_img2 = pygame.image.load('asset/KYET/Kyet_Stupid.png')
	nyantaro_img2 = pygame.transform.smoothscale(nyantaro_img2, (witdh_nyan, height_nyan))
elif save_game['lost'] == 1:
	nyantaro_img = pygame.image.load('asset/KYET/Kyet_Drown.png')
	nyantaro_img = pygame.transform.smoothscale(nyantaro_img, (witdh_nyan, height_nyan))
	nyantaro_img2 = pygame.image.load('asset/KYET/Kyet_Drown.png')
	nyantaro_img2 = pygame.transform.smoothscale(nyantaro_img2, (witdh_nyan, height_nyan))
car_width = 73

def button(x_t,y_t,w,h,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x_t+w > mouse[0] > x_t and y_t+h > mouse[1] > y_t and save_game['lost'] != 1:
        if click[0] == 1 and action != None:
            action()

def button_param(x_t,y_t,w,h,action,param):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x_t+w > mouse[0] > x_t and y_t+h > mouse[1] > y_t:
        if click[0] == 1 and action != None:
            action(param)


    #pygame.draw.rect(surface, red,(x_t,y_t,w,h))

def gui(type):
	x_gu = display_width
	y_gu = display_height
	smallText = pygame.font.Font('freesansbold.ttf',20)
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


		coin = pygame.image.load('asset/Minigame/Nimp [Completed]/Coin.png')
		coin = pygame.transform.smoothscale(coin, (int(witdh_nyan * 0.5), int(height_nyan * 0.5)))
		coin_text = smallText.render(str(save_game['money']), True, black)
		surface.blit(coin_text, (int(display_width * 0.12),int(display_height * 0.24)))
		surface.blit(coin, (int(display_width * 0.005),int(display_height * 0.125)))
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
		button(int(display_width * 0.55),int(display_height * 0.45),int(height_nyan * 0.27),int(witdh_nyan * 0.20),eat_func)

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

		coin = pygame.image.load('asset/Minigame/Nimp [Completed]/Coin.png')
		coin = pygame.transform.smoothscale(coin, (int(witdh_nyan * 0.5), int(height_nyan * 0.5)))
		coin_text = smallText.render(str(save_game['money']), True, black)
		surface.blit(coin_text, (int(display_width * 0.12),int(display_height * 0.12)))
		surface.blit(coin, (int(display_width * 0.005),int(display_height * 0.01)))

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
		button(int(display_width * 0.12),int(display_height * 0.25),int(height_nyan * 0.7),int(witdh_nyan * 0.8),hangnyan_loop)

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
	if save_game['brain_power'] > 100:
		save_game['brain_power'] = 100
	if save_game['food_level'] > 100:
		save_game['food_level'] = 100
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

def shop_func(num):
	print(num)
	print(save_game['money'])
	if num == 0 and save_game['money'] >= 200:
		save_game['money'] -= 200
		save_game['invt'].append(50)
	elif num == 1 and save_game['money'] >= 100:
		save_game['money'] -= 100
		save_game['invt'].append(25)
	elif num == 2 and save_game['money'] >= 100 and 100 >= save_game['brain_power']:
		save_game['money'] -= 100
		save_game['brain_power'] += 25
	elif num == 3 and save_game['money'] >= 200 and 100 >= save_game['brain_power']:
		save_game['money'] -= 200
		save_game['brain_power'] += 50
	elif num == 4 and save_game['money'] >= 300 and 100 >= save_game['brain_power']:
		save_game['money'] -= 300
		save_game['brain_power'] += 75
	print(save_game['invt'])

def eat_func():
	print(save_game['invt'])
	if len(save_game['invt']) != 0:
		save_game['invt'].sort()
		save_game['food_level']+=save_game['invt'][0]
		del save_game['invt'][0]

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
		clock.tick(24)

def shop_loop():
	#Car info
	x =  (display_width * 0.30)
	y = (display_height * 0.50)

	x_change = 0
	
	frame_v = 1

	gameExit = False
	smallText = pygame.font.Font('freesansbold.ttf',20)
	while not gameExit:
		
		frame_v += 1

		gameExit = general_room_stuff()
	
		bg('ShopBGType2')
		square_con = pygame.image.load('asset/Shop Assets/Square.png')
		square_con = pygame.transform.smoothscale(square_con, (int(witdh_nyan * 0.7), int(height_nyan * 0.7)))
		buy_con = pygame.image.load('asset/Shop Assets/buy_button.png')
		buy_con = pygame.transform.smoothscale(buy_con, (int(witdh_nyan * 0.2), int(height_nyan * 0.2)))
		coin = pygame.image.load('asset/Minigame/Nimp [Completed]/Coin.png')
		coin = pygame.transform.smoothscale(coin, (int(witdh_nyan * 0.5), int(height_nyan * 0.5)))
		for h in range(3):
			surface.blit(square_con, (int(display_width * 0.15)*(h*2),int(display_height * 0.2)))
			surface.blit(buy_con, (int(display_width * 0.15)*(h*2),int(display_height * 0.2)))
			button_param(int(display_width * 0.15)*(h*2),int(display_height * 0.2),int(witdh_nyan * 0.2),int(height_nyan * 0.2),shop_func,h)

		food1_con = pygame.image.load('asset/Shop Assets/Food50.png')
		food1_con = pygame.transform.smoothscale(food1_con, (int(witdh_nyan * 0.7), int(height_nyan * 0.7)))
		price = smallText.render('200', True, black)
		surface.blit(food1_con, (int(display_width * 0.15)*(0*2),int(display_height * 0.2)))
		surface.blit(coin, (int(display_width * 0.02),int(display_height * 0.11)))
		surface.blit(price, (int(display_width * 0.15),int(display_height * 0.22)))

		food2_con = pygame.image.load('asset/Shop Assets/Food25.png')
		food2_con = pygame.transform.smoothscale(food2_con, (int(witdh_nyan * 0.7), int(height_nyan * 0.7)))
		price = smallText.render('100', True, black)
		surface.blit(food2_con, (int(display_width * 0.15)*(1*2),int(display_height * 0.2)))
		surface.blit(coin, (int(display_width * 0.02)*16,int(display_height * 0.11)))
		surface.blit(price, (int(display_width * 0.23)*(1*2),int(display_height * 0.22)))

		book1_con = pygame.image.load('asset/Shop Assets/Books Remastered/Kyet_Book_Basic.png')
		book1_con = pygame.transform.smoothscale(book1_con, (int(witdh_nyan * 0.7), int(height_nyan * 0.7)))
		price = smallText.render('100', True, black)
		surface.blit(book1_con, (int(display_width * 0.15)*(2*2),int(display_height * 0.2)))
		surface.blit(coin, (int(display_width * 0.02)*31,int(display_height * 0.11)))
		surface.blit(price, (int(display_width * 0.19)*(2*2),int(display_height * 0.22)))

		for h in range(2):
			square_con = pygame.image.load('asset/Shop Assets/Square.png')
			square_con = pygame.transform.smoothscale(square_con, (int(witdh_nyan * 0.7), int(height_nyan * 0.7)))
			buy_con = pygame.image.load('asset/Shop Assets/buy_button.png')
			buy_con = pygame.transform.smoothscale(buy_con, (int(witdh_nyan * 0.2), int(height_nyan * 0.2)))
			surface.blit(square_con, (int(display_width * 0.15)*(h*2),int(display_height * 0.6)))
			surface.blit(buy_con, (int(display_width * 0.15)*(h*2),int(display_height * 0.6)))
		button_param(int(display_width * 0.15)*(0*2),int(display_height * 0.6),int(witdh_nyan * 0.2),int(height_nyan * 0.2),shop_func,3)
		button_param(int(display_width * 0.15)*(1*2),int(display_height * 0.6),int(witdh_nyan * 0.2),int(height_nyan * 0.2),shop_func,4)

		book2_con = pygame.image.load('asset/Shop Assets/Books Remastered/Kyet_Book_Advanced.png')
		book2_con = pygame.transform.smoothscale(book2_con, (int(witdh_nyan * 0.7), int(height_nyan * 0.7)))
		price = smallText.render('200', True, black)
		surface.blit(book2_con, (int(display_width * 0.15)*(0*2),int(display_height * 0.6)))
		surface.blit(coin, (int(display_width * 0.02),int(display_height * 0.51)))
		surface.blit(price, (int(display_width * 0.15),int(display_height * 0.62)))

		book3_con = pygame.image.load('asset/Shop Assets/Books Remastered/Kyet_Book_Expert.png')
		book3_con = pygame.transform.smoothscale(book3_con, (int(witdh_nyan * 0.7), int(height_nyan * 0.7)))
		price = smallText.render('300', True, black)
		surface.blit(book3_con, (int(display_width * 0.15)*(1*2),int(display_height * 0.6)))
		surface.blit(coin, (int(display_width * 0.02)*16,int(display_height * 0.51)))
		surface.blit(price, (int(display_width * 0.23)*(1*2),int(display_height * 0.62)))

		gui('shop')
	
		pygame.display.update()
		clock.tick(24)

def sett_loop():
	#Car info
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
		bg('BG_Settings_2')
		#gui('home')
		#Draw Obstacle
		#things(thing_startx, thing_starty, thing_width, thing_height, black)
		#thing_starty += thing_speed
		#draw a car in x y coordinate
		gui('shop')
	
		pygame.display.update()
		clock.tick(24)

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
		clock.tick(24)

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
	largeText = pygame.font.Font('freesansbold.ttf',100) 
	smallText = pygame.font.Font('freesansbold.ttf',40) 
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
		if 0 >= n1:
			if user_turn == True :
				won_text = largeText.render('AI WON', True, black)
				#reward_text = smallText.render('Gold: +100', True, black)
				surface.blit(won_text, (int(display_width * 0.25),int(display_height * 0.2)))
				pygame.display.update()
				pygame.time.delay(5000)
				mg_loop()
				#surface.blit(reward_text, (int(display_width * 0.25),int(display_height * 0.4)))
			elif user_turn == False:
				won_text = largeText.render('USER WON', True, black)
				reward_text = smallText.render('Gold: +100', True, black)
				save_game['money'] += 100
				if 80 >= save_game['brain_power']:
					save_game['brain_power'] += 10 
				surface.blit(won_text, (int(display_width * 0.25),int(display_height * 0.2)))
				surface.blit(reward_text, (int(display_width * 0.25),int(display_height * 0.4)))
				pygame.display.update()
				pygame.time.delay(5000)
				mg_loop()
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

		pygame.display.update()
		clock.tick(24)

def ttc_loop():
	SIZE = 3

	HM_EPISODES = 1
	LOSE_PENALTY = 350
	WON_REWARD = 350
	DRAW_REWARD = 175
	epsilon = 0
	EPS_DECAY = 0.9998  # Every episode will be epsilon*EPS_DECAY
	SHOW_EVERY = 1  # how often to play through env visually.
	
	start_q_table ='qtable/qtable-1576318922-ttc-500000-gen2.1.pickle' # None or Filename
	
	LEARNING_RATE = 0.1
	DISCOUNT = 0.99
	
	PLAYER_N = 1  # player key in dict
	FOOD_N = 2  # food key in dict
	ENEMY_N = 3  # enemy key in dict
	
	d = {1: (255, 175, 0),
		2: (0, 255, 0),
		3: (0, 0, 255)}
	
	with open(start_q_table, "rb") as f:
	    q_table = pickle.load(f)
	
	episode_rewards = []
	x =  (display_width * 0.30)
	y = (display_height * 0.50)

	x_change = 0
	
	frame_v = 1

	gameExit = False
	board = [0,0,0,0,0,0,0,0,0]
	won_o = False
	lose_o = False
	episode_reward = 0
	turn = 0
	textinput = pygame_textinput.TextInput()
	test2 = 10
	turn_a = 0
	largeText = pygame.font.Font('freesansbold.ttf',100) 
	smallText = pygame.font.Font('freesansbold.ttf',40) 
	while not gameExit:
		turn += 1
		frame_v += 1

		bg('TTT_Background')
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
			print(event)

		#tic tac toe AI
		obs = tuple(board)
		if turn == 1:
			action = np.random.randint(0, 9)
			board[action] = 1
			turn = 2
		elif turn_a == 1 and turn >= 1:
			if np.random.random() > epsilon and save_game['brain_power'] >= 95:
			# GET THE ACTION
				action = np.argmax(q_table[obs])
			else:
				action = np.random.randint(0, 9)
			turn_a = 0
			b = 0
			for c in board:
				if c == 0:
					b += 1
	
			if  b !=0:
				while board[action] != 0:
					action = np.random.randint(0, 9)
				board[action] = 1

			if board[0] == 1 and board[1] == 1 and board[2] == 1:
				won_o = True
			elif board[3] == 1 and board[4] == 1 and board[5] == 1:
				won_o = True
			elif board[6] == 1 and board[7] == 1 and board[8] == 1:
				won_o = True
			#horz
			elif board[1] == 1 and board[4] == 1 and board[7] == 1:
				won_o = True
			elif board[0] == 1 and board[3] == 1 and board[6] == 1:
				won_o = True
			elif board[2] == 1 and board[5] == 1 and board[8] == 1:
				won_o = True
			#dgonal
			elif board[0] == 1 and board[4] == 1 and board[8] == 1:
				won_o = True
			elif board[2] == 1 and board[4] == 1 and board[6] == 1:
				won_o = True
			
		n = 0
		hh = 1
		X_con = pygame.image.load('asset/Minigame/TTT/TTT_Cross.png')
		O_con = pygame.image.load('asset/Minigame/TTT/TTT_Circle.png')
		X_con = pygame.transform.smoothscale(X_con, (int(witdh_nyan * 0.5), int(height_nyan * 0.5)))
		O_con = pygame.transform.smoothscale(O_con, (int(witdh_nyan * 0.5), int(height_nyan * 0.5)))
		for h in range(len(board)):
			n+=1
			if board[h] == 1:
				surface.blit(O_con, (int((display_width * (0.1*(n*2))))+(n*10),int(display_height * 0.19)*hh+((hh-1)*15)))
				pygame.display.update()
			elif board[h] == -1:
				surface.blit(X_con, (int((display_width * (0.1*(n*2))))+(n*10),int(display_height * 0.19)*hh+((hh-1)*15)))
				pygame.display.update()
			elif board[h] == 0:
				print("| |",end="")
			if n == 3:
				n=0
				hh+=1
		x += x_change
	
		#fill background with white	
		
		b = 0
		for c in board:
			if c == 0:
				b += 1

		test2 = 10
		surface.blit(textinput.get_surface(), (int(display_width * 0.5),int(display_height * 0.85)))
		if textinput.update(events):
			test2 = int(textinput.get_text()) - 1
		pygame.display.update()
		if turn_a == 0 and test2 != 10 and won_o != True:
			board[test2] = -1
			turn_a = 1
		#vert
		if board[0] == -1 and board[1] == -1 and board[2] == -1:
			lose_o = True
		elif board[3] == -1 and board[4] == -1 and board[5] == -1:
			lose_o = True
		elif board[6] == -1 and board[7] == -1 and board[8] == -1:
			lose_o = True
		#horz
		elif board[1] == -1 and board[4] == -1 and board[7] == -1:
			lose_o = True
		elif board[0] == -1 and board[3] == -1 and board[6] == -1:
			lose_o = True
		elif board[2] == -1 and board[5] == -1 and board[8] == -1:
			lose_o = True
		#dgonal
		elif board[0] == -1 and board[4] == -1 and board[8] == -1:
			lose_o = True
		elif board[2] == -1 and board[4] == -1 and board[6] == -1:
			lose_o = True

		b = 0
		for c in board:
			if c == 0:
				b += 1
		if test2 != 10:
			reward = 0
			if lose_o == True:
				won_text = largeText.render('USER WON', True, black)
				reward_text = smallText.render('Gold: +100', True, black)
				save_game['money'] += 100
				if 80 >= save_game['brain_power']:
					save_game['brain_power'] += 10 
				surface.blit(won_text, (int(display_width * 0.25),int(display_height * 0.2)))
				surface.blit(reward_text, (int(display_width * 0.25),int(display_height * 0.4)))
				pygame.display.update()
				pygame.time.delay(5000)
				mg_loop()
				reward = -LOSE_PENALTY
			elif won_o:
				won_text = largeText.render('AI WON', True, black)
				#reward_text = smallText.render('Gold: +100', True, black)
				surface.blit(won_text, (int(display_width * 0.25),int(display_height * 0.2)))
				pygame.display.update()
				pygame.time.delay(5000)
				mg_loop()
				reward = WON_REWARD
			elif b == 0:
				won_text = largeText.render('DRAW', True, black)
				reward_text = smallText.render('Gold: +50', True, black)
				save_game['money'] += 50
				if 95 >= save_game['brain_power'] and 100 > save_game['brain_power']:
					save_game['brain_power'] += 5
				surface.blit(won_text, (int(display_width * 0.25),int(display_height * 0.2)))
				surface.blit(reward_text, (int(display_width * 0.25),int(display_height * 0.4)))
				pygame.display.update()
				pygame.time.delay(5000)
				mg_loop()
				reward = DRAW_REWARD
			## NOW WE KNOW THE REWARD, LET'S CALC YO
			# first we need to obs immediately after the move.
			new_obs = tuple(board)
			max_future_q = np.max(q_table[new_obs])
			current_q = q_table[obs][action]
	
			if reward == WON_REWARD:
				new_q = WON_REWARD
			else:
				new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)
			q_table[obs][action] = new_q
	
			episode_reward += reward

		pygame.display.update()
		clock.tick(24)

def hangnyan_loop():
	x =  (display_width * 0.30)
	y = (display_height * 0.50)

	x_change = 0
	
	frame_v = 1

	if save_game['brain_power'] > 50:
		text = "hangeman_hd"
	else:
		text = "hangeman_ez"
	with open(f"asset/Minigame/HangNyan/hangeman_ez.txt", "r") as f:
		fl =f.read().splitlines()
	text = fl[np.random.randint(len(fl))].lower()
	print(text)
	gameExit = False
	wrong = 0
	failure = 0
	won_c = len(text)
	won = 0
	textinput = pygame_textinput.TextInput()
	text_user = [' ']*len(text)
	largeText = pygame.font.Font('freesansbold.ttf',100) 
	smallText = pygame.font.Font('freesansbold.ttf',40) 
	print(text)
	while not gameExit:
		i_wrong = 0
		wrong = failure
		frame_v += 1

		bg('Nimp_Background')
		events2 = pygame.event.get()
		for event2 in events2:
			if event2.type == pygame.USEREVENT:
				food_stuff()
			if event2.type == pygame.USEREVENT+2:
				save1 = json.dumps(save_game)
				pickle.dump(save1, open("save_game.pickle", "wb"))
			if event2.type == pygame.QUIT:
				save1 = json.dumps(save_game)
				pickle.dump(save1, open("save_game.pickle", "wb"))
				gameExit = True
			print(event2)
		
		aquarium = pygame.image.load('asset/Minigame/HangNyan/AquariumV2.png')
		surface.blit(aquarium, (int(display_width * 0.15),int(display_height * 0.10)))

		board = pygame.image.load('asset/Minigame/HangNyan/Closed_Platform.png')
		board = pygame.transform.smoothscale(board, (int(witdh_nyan * 0.4), int(height_nyan * 0.1)))

		for n in range(5):
			if wrong > 0:
				board = pygame.image.load('asset/Minigame/HangNyan/Open_Platform.png')
				board = pygame.transform.smoothscale(board, (int(witdh_nyan * 0.4), int(height_nyan * 0.2)))
				wrong -= 1
			else:
				board = pygame.image.load('asset/Minigame/HangNyan/Closed_Platform.png')
				board = pygame.transform.smoothscale(board, (int(witdh_nyan * 0.4), int(height_nyan * 0.1)))
			surface.blit(board, (int(display_width * 0.45),int(display_height * 0.13)*(n+1)))

		kyet = pygame.image.load('asset/KYET/Kyet_Bling.png')
		kyet = pygame.transform.smoothscale(kyet, (int(witdh_nyan * 0.5), int(height_nyan * 0.5)))
		if failure == 0:
			surface.blit(kyet, (int(display_width * 0.45),int(display_height * 0.01)))
		if failure == 1:
			surface.blit(kyet, (int(display_width * 0.45),int(display_height * 0.15)))
		if failure == 2:
			surface.blit(kyet, (int(display_width * 0.45),int(display_height * 0.28)))
		if failure == 3:
			kyet = pygame.image.load('asset/KYET/Kyet_Angry.png')
			kyet = pygame.transform.smoothscale(kyet, (int(witdh_nyan * 0.5), int(height_nyan * 0.5)))
			surface.blit(kyet, (int(display_width * 0.45),int(display_height * 0.41)))
		if failure == 4:
			kyet = pygame.image.load('asset/KYET/Kyet_Angry.png')
			kyet = pygame.transform.smoothscale(kyet, (int(witdh_nyan * 0.5), int(height_nyan * 0.5)))
			surface.blit(kyet, (int(display_width * 0.45),int(display_height * 0.54)))
		if failure == 5:
			kyet = pygame.image.load('asset/KYET/Kyet_Drown.png')
			kyet = pygame.transform.smoothscale(kyet, (int(witdh_nyan * 0.3), int(height_nyan * 0.3)))
			surface.blit(kyet, (int(display_width * 0.45),int(display_height * 0.64)))
			pygame.display.update()
			won_text = largeText.render('YOU LOSE', True, black)
			#reward_text = smallText.render('Gold: +100', True, black)
			surface.blit(won_text, (int(display_width * 0.25),int(display_height * 0.2)))
			pygame.display.update()
			pygame.time.delay(5000)
			mg_loop()
		for n in range(len(text)):
			text_board = pygame.image.load('asset/Minigame/HangNyan/word_Platform.png')
			text_board = pygame.transform.smoothscale(text_board, (int(witdh_nyan * 0.1), int(height_nyan * 0.05)))
			surface.blit(text_board, (int(display_width * 0.05)*(n+1),int(display_height * 0.4)))
			if text[n] == text_user[n]:
				won_text = smallText.render(text_user[n], True, black)
				surface.blit(won_text, (int(display_width * 0.05)*(n+1),int(display_height * 0.35)))
		
		surface.blit(textinput.get_surface(), (int(display_width * 0.05),int(display_height * 0.45)))
		if textinput.update(events2):
			test2 = textinput.get_text()
			for n in range(len(text)):
				if text[n] == test2.lower():
					text_user[n] = test2.lower()
					won += 1
				else:
					i_wrong += 1
					print(len(text))
			if i_wrong == len(text):
				failure+=1
			print(failure)

		if won == won_c:
			won_text = largeText.render('USER WON', True, black)
			reward_text = smallText.render('Gold: +100', True, black)
			save_game['money'] += 100
			if 100 > save_game['brain_power']:
				save_game['brain_power'] += 5 
			surface.blit(won_text, (int(display_width * 0.25),int(display_height * 0.2)))
			surface.blit(reward_text, (int(display_width * 0.25),int(display_height * 0.4)))
			pygame.display.update()
			pygame.time.delay(5000)
			mg_loop()

		x += x_change
		pygame.display.update()
		clock.tick(24)
game_loop()
pygame.quit()
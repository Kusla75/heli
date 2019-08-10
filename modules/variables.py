import pygame as pg
import os
import ctypes as ct
import random as rand

#################################################################
user32 = ct.windll.user32
user32.SetProcessDPIAware()

monitor_w = user32.GetSystemMetrics(0)
monitor_h = user32.GetSystemMetrics(1)

x = monitor_w * 0.1318
y = monitor_h * 0.1302
#################################################################
wind_width = 1000
wind_height = 600

pl_speed = 15
bul_speed = 60

game_end = False
wait = True
restart = True

check_bul1 = False
check_bul2 = False
box1_check = False
box2_check = False

background = (153, 217, 234)
txt_color1 = (0, 0, 240)
txt_color2 = (240, 0, 0)
color_box1 = (60, 60, 255)
color_box2 = (255, 60, 60)
BLACK = (0, 0, 0)

start_time1 = 0
start_time2 = 0

col_count1 = 0    #color_counter - used for changing box transparency
col_count2 = 0    #during active period

start_count1 = False
start_count2 = False

sp_duck = pg.image.load("resources/duck.png")
sp_bullet = pg.image.load("resources/bullet.png")
sp_robot = pg.image.load("resources/robot.png")
controls_screen = pg.image.load("resources/controls.png")
icon = pg.image.load("resources/window_icon.png")

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (x, y)

gameDisplay = pg.display.set_mode((wind_width, wind_height))
pg.display.set_icon(icon)
pg.display.set_caption("Heli")
clock = pg.time.Clock()

#################################################################
pg.mixer.init()

soundtrack = "soundtrack/What is love 8 bit.mp3"
pg.mixer.music.load(soundtrack)

#################################################################
def text_object(text, font, txt_color):
    TextSurf = font.render(text, True, txt_color)
    return TextSurf, TextSurf.get_rect()

def write_text(text, txt_color, x, y, scale, pom = True, time = False):
    text_look = pg.font.Font("resources/Audiowide-Regular.ttf", scale)
    TextSurf, TextRect = text_object(text, text_look, txt_color)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)
    if pom:
        pg.display.update()
    if time:
        pg.time.wait(800)

def write_life(player1, player2):
        write_text(str(player1.life), BLACK, 470, 25, 40, False)
        write_text(str(player2.life), BLACK, 530, 25, 40, False)

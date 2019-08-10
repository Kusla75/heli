from modules.variables import *

class Object:
    def __init__(self, x, y, life = 0, num = 0):
        self.x = x
        self.y = y
        self.life = life
        self.num = num

    def move_down(self, speed):
        if self.y < 500:
            self.y += speed

    def move_up(self, speed):
        if self.y >= 15:
            self.y -= speed

    def move_left(self, speed):
        self.x -= speed

    def move_right(self, speed):
        self.x += speed

#################################################################
def draw_object(sp_object, object):
    gameDisplay.blit(sp_object, (object.x, object.y))

def activate_bullet(bullet, player):
        bullet.y = player.y + 50
        return bullet.y

def restart_bullet(bullet, check_bul, set):
    if bullet.x  > wind_width + 30 or bullet.x < -30 or check_bul == False:
        bullet.x = set
        check_bul = False
        return [bullet.x, check_bul]
    else:
        return [bullet.x, check_bul]

def check_corY(bullet, object):
    if (bullet.y + 15 >= object.y and bullet.y + 15 <= object.y + 100):
        return True
    else: return False

def check_colision_player(bullet, player):
    if bullet.num == 1:
        if check_corY(bullet, player) and bullet.x >= player.x:
                return True
        else: return False
    if bullet.num == 2:
        if check_corY(bullet, player) and bullet.x <= player.x + 100:
            return True
        else: return False

#################################################################
def activate_box(box, player):
    box.y = player.y
    return box.y

def draw_box(color_box, box):
    pg.draw.rect(gameDisplay, color_box, [box.x, box.y, 100, 100])
    start_time = pg.time.get_ticks()
    return start_time

def check_passed_time(time, box_check, start_count):
    if box_check and start_count:
        end_time = pg.time.get_ticks()
        if ((end_time - time) / 1000) >= 8:
            return True
        else: return False

def check_colision_box(bullet, box):
    if bullet.num == 1:
        if check_corY(bullet, box) and bullet.x >= box.x:
            return True
        else: return False
    if bullet.num == 2:
        if check_corY(bullet, box) and bullet.x <= box.x:
            return True
        else: return False

def change_color(i, color_box):
    if color_box[2] == 255:
        return (color_box[0] + i, color_box[1] + i, 255)
    if color_box[0] == 255:
        return (255, color_box[1] + i, color_box[2] + i)

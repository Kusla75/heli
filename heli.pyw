from sys import exit
from modules.logic import *
#from modules.variables import *

pg.init()

pl_duck = Object(5, 200, 7)
pl_robot = Object(895, 200, 7)

bullet1 = Object(105, 0, num = 1)
bullet2 = Object(895, 0, num = 2)

box1 = Object(115, 0, num = 1)
box2 = Object(775, 0, num = 2)

#################################################################
pg.mixer.music.play(-1)

gameDisplay.fill(background)
write_text("Heli", BLACK, wind_width/2, wind_height/2 - 40, 70)
write_text("-- game for 2 players --", BLACK, wind_width/2, wind_height/2 + 20, 25)
write_text("Made by: Nikola Kuslakovic", BLACK, 840, 20, 20)
write_text("Press any key to continue", BLACK, 870, 575, 15)
pg.display.update()
while wait:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            wait = False
wait = True

gameDisplay.blit(controls_screen, (0, 0))
pg.display.update()

while wait:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
                wait = False
wait = True

#################################################################
while game_end != True:
    if wait:
        gameDisplay.fill(background)
        write_text("3", BLACK, wind_width/2, wind_height/2 - 40, 70, time = True)
        gameDisplay.fill(background)
        write_text("2", BLACK, wind_width/2, wind_height/2 - 40, 70, time = True)
        gameDisplay.fill(background)
        write_text("1", BLACK, wind_width/2, wind_height/2 - 40, 70, time = True)
        gameDisplay.fill(background)
        write_text("START!", BLACK, wind_width/2, wind_height/2 - 40, 70, time = True)
        wait = False

    gameDisplay.fill(background)
    pg.draw.rect(gameDisplay, (67, 186, 216), [500, 0, 5, 600])
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                exit()

    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        pl_duck.move_up(pl_speed)
    if keys[pg.K_s]:
        pl_duck.move_down(pl_speed)
    if keys[pg.K_d]:
        if check_bul1 != True:
            bullet1.y = activate_bullet(bullet1, pl_duck)
            check_bul1 = True
    if keys[pg.K_a]:
        if box1_check != True:
            box1.y = activate_box(box1, pl_duck)
            box1_check = True

    if keys[pg.K_UP]:
        pl_robot.move_up(pl_speed)
    if keys[pg.K_DOWN]:
        pl_robot.move_down(pl_speed)
    if keys[pg.K_LEFT]:
        if check_bul2 != True:
            bullet2.y = activate_bullet(bullet2, pl_robot)
            check_bul2 = True
    if keys[pg.K_RIGHT]:
        if box2_check != True:
            box2.y = activate_box(box2, pl_robot)
            box2_check = True

#################################################################
    if pl_duck.life == 0 or pl_robot.life == 0:
        if pl_duck.life == 0:
            write_text("Robot won!", txt_color2, wind_width/2, 100, 60)
            pg.time.wait(2000)
        if pl_robot.life == 0:
            write_text("Duck won!", txt_color1, wind_width/2, 100, 60)
            pg.time.wait(2000)
        game_end = True
        restart = True

    if box1_check and check_bul1:
        if check_colision_box(bullet1, box1):
            check_bul1 = False
    if box2_check and check_bul1:
        if check_colision_box(bullet1, box2):
            check_bul1 = False

    if box1_check and check_bul2:
        if check_colision_box(bullet2, box1):
            check_bul2 = False
    if box2_check and check_bul2:
        if check_colision_box(bullet2, box2):
            check_bul2 = False

    if check_bul1:
        if check_colision_player(bullet1, pl_robot):
            check_bul1 = False
            pl_robot.life -= 1

    if check_bul2:
        if check_colision_player(bullet2, pl_duck):
            check_bul2 = False
            pl_duck.life -= 1

    if check_bul1:
        bullet1.move_right(bul_speed)
    if check_bul2:
        bullet2.move_left(bul_speed)

    bullet1.x, check_bul1 = restart_bullet(bullet1, check_bul1, 105)
    bullet2.x, check_bul2 = restart_bullet(bullet2, check_bul2, 895)

#################################################################
    if game_end != True:
        write_life(pl_duck, pl_robot)

        if check_bul1:
            draw_object(sp_bullet, bullet1)
        if check_bul2:
            draw_object(sp_bullet, bullet2)

        if box1_check:
            if start_count1 != True:
                start_time1 = draw_box(color_box1, box1)
                start_count1 = True
                col_count1 = 0
            else:
                draw_box(change_color(col_count1, color_box1), box1)
                col_count1 += 0.2

        if box2_check:
            if start_count2 != True:
                start_time2 = draw_box(color_box2, box2)
                start_count2 = True
                col_count2 = 0
            else:
                draw_box(change_color(col_count2, color_box2), box2)
                col_count2 += 0.2

        if check_passed_time(start_time1, box1_check, start_count1):
            box1_check = False
            start_count1 = False
        if check_passed_time(start_time2, box2_check, start_count2):
            box2_check = False
            start_count2 = False

        draw_object(sp_duck, pl_duck)
        draw_object(sp_robot, pl_robot)
        pg.display.update()

    if game_end:
        write_text("'R' to restart", BLACK, wind_width/2, wind_height/2 - 40, 20)
        write_text("'Q' to quit", BLACK, wind_width/2, wind_height/2, 20)
        while restart:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_r:
                        game_end = False
                        pl_duck.life = 7
                        pl_robot.life = 7
                        pl_duck.y = 200
                        pl_robot.y = 200
                        check_bul1 = False
                        check_bul2 = False
                        box1_check = False
                        box2_check = False
                        restart = False
                        wait = True
                    if event.key == pg.K_q:
                        exit()
    clock.tick(60)

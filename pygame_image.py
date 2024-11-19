import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_flip_img = pg.transform.flip(bg_img,True,False)
    koka_img = pg.image.load("fig/3.png")
    koka_img = pg.transform.flip(koka_img,True,False)
    tmr = 0
    kk_rct = koka_img.get_rect()
    kk_rct.center = 300, 200


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        key_lst = pg.key.get_pressed()

        if key_lst[pg.K_UP]:
            kk_rct.move_ip((0, -1))

        if key_lst[pg.K_DOWN]:
            kk_rct.move_ip((0, 1))
        
        if key_lst[pg.K_LEFT]:
            kk_rct.move_ip((-1, 0))

        if key_lst[pg.K_RIGHT]:
            kk_rct.move_ip((1,0))


        x = -(tmr%3200)
        screen.blit(bg_img, [x, 0])
        screen.blit(bg_flip_img,[x + 1600,0])
        screen.blit(bg_img, [x+3200, 0])
        screen.blit(bg_flip_img,[x+4800,0])

        #screen.blit(koka_img,[300,200])

        screen.blit(koka_img, kk_rct)

        pg.display.update()
        tmr += 1        
        clock.tick(200)
        



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
import pygame as pg
import math

pg.init()
WIN_SIZE = WIN_WIDTH, WIN_HEIGHT = 500, 500
CENTER = (WIN_WIDTH / 2, WIN_HEIGHT / 2)
screen = pg.display.set_mode(WIN_SIZE)

surf = pg.transform.scale_by(
    pg.image.load("box.jpg").convert_alpha(),
    0.25,
)

def main():
    while True:
        mouse_pos = pg.mouse.get_pos()

        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                return

        angle = -math.atan2(mouse_pos[1] - CENTER[1], mouse_pos[0] - CENTER[0])
        rot_surf = pg.transform.rotate(surf, math.degrees(angle))
        rect = rot_surf.get_rect(center=CENTER)

        screen.fill("black")
        screen.blit(rot_surf, rect)
        pg.display.flip()

if __name__ == "__main__":
    main()
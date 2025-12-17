import pygame
from pygame import gfxdraw
import math as M
import random
import numpy as np

goldenRatio = 1.618  # where?

line_margin = 40
end_margin = 10
def drawAxis(screen):   #, x_range, y_range):
    color = (255, 255, 255)
    #x-axis
    pygame.draw.line(screen, color, [end_margin, h - line_margin], [w - end_margin, h - line_margin])
    pygame.draw.line(screen, color, [end_margin, line_margin], [w - end_margin, line_margin])
    #y-axis
    pygame.draw.line(screen, color, [line_margin, end_margin], [line_margin, h - end_margin])
    pygame.draw.line(screen, color, [w - line_margin, end_margin], [w - line_margin, h - end_margin])

def WaveyBackground(screen):
    for x in xrange(0,w+1):
        for y in xrange(0,h+1):
            gr = (abs(M.sin((x+y)/60.0))) * 255
            color = (gr, gr, gr, 120)
            pygame.gfxdraw.pixel(screen, x, y, color)

def GetShuffledArray(length):
    ret = []
    for i in xrange(0,length-1):
        temp = 0

    return ret

# try drawing same data but with interactively more or less columns
# maybe pause countdown and print numbers each time
# learn how to print text on graphics or create an additional window to display data
min_col_space = 2
col_colr = (255,0,0)
def DrawColumns(screen, data):
    num_cols = len(data)
    print_space = w - 2 * (line_margin + min_col_space) # screen width - (l_margin + r_margin + 2 * min_col_space)
    col_incr = print_space // num_cols
    line_width = col_incr - min_col_space
    # print('num_cols', num_cols, 'col_incr', col_incr, 'line_width', line_width)
    print(f"{num_cols=}  {col_incr=}  {line_width=}")

    curr_col = line_margin + col_incr + min_col_space
    scaling_ratio = GetScalingRatio(data, h-(2*line_width+min_col_space) )

    #start @ x=line_margin, h-line_margin,  add min_col_space to line_margin, print up to (h-line_margin) - (data*scaling_ratio)
    for c in data:
        pygame.draw.line(screen, col_colr, [curr_col,h-line_margin], [curr_col, (h-line_margin) - (c*scaling_ratio)], line_width)
        curr_col += col_incr #min_col_space #+ line_width

def GetScalingRatio(data, y_print_space):
    maxVal = max(data)
    scaling = max( [ y_print_space / maxVal, 1])
    print(f"{scaling value=})
    return scaling

column_data = [3,7,14,3,25,35,1000,99,125,45,45,40,35,17,19,23,29,31,37,41,43,16,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,250,175,71,73,79,83,89,91,97]  #  ,250,175
w = 1400
h = 1000

def main():
    pygame.init()
    gray = (127, 127, 127, 255)
    screen = pygame.display.set_mode((w, h), pygame.RESIZABLE) # pygame.NOFRAME|
    videoInfo = pygame.display.Info()
    print('current_h', videoInfo.current_h, 'current_w',  videoInfo.current_w)
    pygame.display.set_caption('First Pygame Title', 'My Icon Title')
    done = False
    is_blue = True
    x = 30
    y = 30
    r = 0
    g = 128
    b = 255
    a = 200
    inc = 4
    mv = 3

    clock = pygame.time.Clock()
    clock_count = 0

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                is_blue = not is_blue

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= mv
        if pressed[pygame.K_DOWN]: y += mv
        if pressed[pygame.K_LEFT]: x -= mv
        if pressed[pygame.K_RIGHT]: x += mv

        if pressed[pygame.K_k]: done = True

        if pressed[pygame.K_q]:
            r += inc
            if r > 255: r = 255
        if pressed[pygame.K_a]:
            r -= inc
            if r < 0: r = 0
        if pressed[pygame.K_w]:
            g += inc
            if g > 255: g = 255
        if pressed[pygame.K_s]:
            g -= inc
            if g < 0: g = 0
        if pressed[pygame.K_e]:
            b += inc
            if b > 255: b = 255
        if pressed[pygame.K_d]:
            b -= inc
            if b < 0: b = 0
        if pressed[pygame.K_r]: #a = 255
            a += inc
            if a > 255: a = 255
        if pressed[pygame.K_f]: #a = 0
            a -= inc
            if a < 0: a = 0


        screen.fill((0, 0, 0))
        # WaveyBackground(screen)
        if is_blue:
            color = (r, g, b, a)
        else:
            color = (15, 115, 215, 25)
        # pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
        end = len(column_data) - clock_count
        DrawColumns(screen, column_data[clock_count:end])
        clock_count += 2
        if clock_count >= end: done = True
        # text = raw_input('waiting for enter')  # Python 2.7 minor=13 and below
        #clock this down to every 5? seconds

        drawAxis(screen)
        #  screen.get
        #  pygame.display.Info()   current_h, current_h:
        #  set font

        videoInfo = pygame.display.Info()  #  stays the same even when the window is resized
        print('current_h', videoInfo.current_h, 'current_w', videoInfo.current_w)

        pygame.time.wait(2300)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()

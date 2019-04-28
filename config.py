import pygame
from main import *
#-------DISPLAY-------#

WINDOW = [1000,600]
WIDTH = 30
MARGIN = 1
BACKGROUND = pygame.image.load('backgrounds/maze1.png')

#--------WALLS--------#
WALL = pygame.image.load('wall/wall.png')
WALL = pygame.transform.scale(WALL, (WIDTH, WIDTH))

W_D = pygame.image.load('wall/w_d.png')
W_D = pygame.transform.scale(W_D, (WIDTH, WIDTH))

W_R = pygame.image.load('wall/w_r.png')
W_R = pygame.transform.scale(W_R, (WIDTH, WIDTH))

W_T = pygame.image.load('wall/w_t.png')
W_T = pygame.transform.scale(W_T, (WIDTH, WIDTH))

W_L = pygame.image.load('wall/w_l.png')
W_L = pygame.transform.scale(W_L, (WIDTH, WIDTH))

W_L_B = pygame.image.load('wall/w_l_b.png')
W_L_B = pygame.transform.scale(W_L_B, (WIDTH, WIDTH))

W_R_B = pygame.image.load('wall/w_r_b.png')
W_R_B = pygame.transform.scale(W_R_B, (WIDTH, WIDTH))

W_T_R = pygame.image.load('wall/w_t_r.png')
W_T_R = pygame.transform.scale(W_T_R, (WIDTH, WIDTH))

W_T_L = pygame.image.load('wall/w_t_l.png')
W_T_L = pygame.transform.scale(W_T_L, (WIDTH, WIDTH))

#--------DOORS--------#
DOORS_START = pygame.image.load('doors/doors_start.png')
DOORS_START = pygame.transform.scale(DOORS_START, (WIDTH, WIDTH))

DOORS_1 = pygame.image.load('doors/doors1.png')
DOORS_1 = pygame.transform.scale(DOORS_1, (WIDTH, WIDTH))

DOORS_3_C = pygame.image.load('doors/d3_closed.png')
DOORS_3_C = pygame.transform.scale(DOORS_3_C, (WIDTH, WIDTH))

DOORS_3_O = pygame.image.load('doors/d3_opened.png')
DOORS_3_O = pygame.transform.scale(DOORS_3_O, (WIDTH, WIDTH))

DOORS_3_O_R = pygame.image.load('doors/d3_opened_r.png')
DOORS_3_O_R = pygame.transform.scale(DOORS_3_O_R, (WIDTH, WIDTH))

GDOORS_UP = pygame.image.load('doors/glow_d_up.png')
GDOORS_UP = pygame.transform.scale(GDOORS_UP, (WIDTH, WIDTH))

GDOORS_DOWN = pygame.image.load('doors/doors2.png')
GDOORS_DOWN = pygame.transform.scale(GDOORS_DOWN, (WIDTH, WIDTH))

GDOORS_RIGHT = pygame.image.load('doors/glow_d_right.png')
GDOORS_RIGHT= pygame.transform.scale(GDOORS_RIGHT, (WIDTH, WIDTH))

#--------FLOORS--------#
FLOOR = pygame.image.load('floor/floor.png')
FLOOR = pygame.transform.scale(FLOOR, (WIDTH, WIDTH))

GFLOOR_L_B = pygame.image.load('floor/glow_f_b_l.png')
GFLOOR_L_B = pygame.transform.scale(GFLOOR_L_B, (WIDTH, WIDTH))

GFLOOR_R_B = pygame.image.load('floor/glow_f_b_r.png')
GFLOOR_R_B = pygame.transform.scale(GFLOOR_R_B, (WIDTH, WIDTH))

GFLOOR_T_L = pygame.image.load('floor/glow_f_t_l.png')
GFLOOR_T_L = pygame.transform.scale(GFLOOR_T_L, (WIDTH, WIDTH))

GFLOOR_T_R = pygame.image.load('floor/glow_f_t_r.png')
GFLOOR_T_R = pygame.transform.scale(GFLOOR_T_R, (WIDTH, WIDTH))

GFLOOR_CENTER = pygame.image.load('floor/glow_f_center.png')
GFLOOR_CENTER = pygame.transform.scale(GFLOOR_CENTER, (WIDTH, WIDTH))

GFLOOR_LEFT = pygame.image.load('floor/glow_f_left.png')
GFLOOR_LEFT = pygame.transform.scale(GFLOOR_LEFT, (WIDTH, WIDTH))

GFLOOR_RIGHT = pygame.image.load('floor/glow_f_right.png')
GFLOOR_RIGHT = pygame.transform.scale(GFLOOR_RIGHT, (WIDTH, WIDTH))

GFLOOR_UP = pygame.image.load('floor/glow_f_up.png')
GFLOOR_UP = pygame.transform.scale(GFLOOR_UP, (WIDTH, WIDTH))

GFLOOR_DOWN = pygame.image.load('floor/glow_f_down.png')
GFLOOR_DOWN = pygame.transform.scale(GFLOOR_DOWN, (WIDTH, WIDTH))

#--------PLAYER---------#
PLAYER_UP = pygame.image.load('hero/dwarf_up.png')
PLAYER_UP = pygame.transform.scale(PLAYER_UP, (WIDTH, WIDTH))

PLAYER_DOWN = pygame.image.load('hero/dwarf_down.png')
PLAYER_DOWN = pygame.transform.scale(PLAYER_DOWN, (WIDTH, WIDTH))

PLAYER_LEFT = pygame.image.load('hero/dwarf_left.png')
PLAYER_LEFT = pygame.transform.scale(PLAYER_LEFT, (WIDTH, WIDTH))

PLAYER_RIGHT = pygame.image.load('hero/dwarf_right.png')
PLAYER_RIGHT = pygame.transform.scale(PLAYER_RIGHT, (WIDTH, WIDTH))

#--------ITEMS---------#
LEVER_C = pygame.image.load('items/lever_closed.png')
LEVER_C = pygame.transform.scale(LEVER_C, (WIDTH, WIDTH))

LEVER_O = pygame.image.load('items/lever_opened.png')
LEVER_O = pygame.transform.scale(LEVER_O, (WIDTH, WIDTH))

LEVER_O_C = pygame.image.load('items/lever_opened_c.png')
LEVER_O_C = pygame.transform.scale(LEVER_O_C, (WIDTH, WIDTH))

LEVER_C_R = pygame.image.load('items/lever_closed_r.png')
LEVER_C_R = pygame.transform.scale(LEVER_C_R, (WIDTH, WIDTH))

LEVER_O_R = pygame.image.load('items/lever_opened_r.png')
LEVER_O_R = pygame.transform.scale(LEVER_O_R, (WIDTH, WIDTH))

#---------COLORS--------#
GREY = (130,130,130)
L_GREY = (200,200,200)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0,255,0)
GRANIT = (3, 22, 66)
DEEP = (18, 79, 2)
BLOODY = (173,39,29)
VIOLET = (79, 2, 61)
L_ORANGE = (193,156,34)
D_ORANGE = (193,95,34)
D_RED = (66,8,3)

#---------FIELDS--------#

class Field:
    def __init__(self):
        self.status = 'dark'
        self.show = False


field = [ [Field() for x in range(18)] for y in range(10) ]
def setup1(field, player):
    player.cords = [1,0] #start player cords
    player.start_cords = [1, 0] #start door cords
    player.end_cords = [9,14] #end door cords
    player.doors_exit = DOORS_3_C
    field[1][0].status = 'empty'
    field[0][0].status = 'wall'
    field[0][1].status = 'wall'
    field[0][2].status = 'wall'
    field[1][1].status = 'empty'
    field[2][0].status = 'wall'
    field[2][2].status = 'empty'
    field[1][2].status = 'empty'
    field[2][2].status = 'empty'
    field[2][3].status = 'empty'
    field[2][4].status = 'empty'
    field[3][4].status = 'empty'
    field[3][5].status = 'empty'
    field[3][6].status = 'empty'
    field[3][7].status = 'empty'
    field[3][8].status = 'empty'
    field[3][9].status = 'empty'
    field[3][10].status = 'empty'
    field[2][7].status = 'empty'
    field[1][7].status = 'empty'
    field[4][10].status = 'empty'
    field[5][10].status = 'empty'
    field[6][10].status = 'empty'
    field[7][10].status = 'empty'
    field[8][10].status = 'empty'
    field[6][9].status = 'empty'
    field[6][8].status = 'empty'
    field[6][7].status = 'empty'
    field[6][6].status = 'empty'
    field[6][11].status = 'empty'
    field[6][12].status = 'empty'
    field[6][13].status = 'empty'
    field[6][14].status = 'empty'
    field[7][14].status = 'empty'
    field[8][14].status = 'empty'
    field[9][14].status = 'empty'
    field[5][14].status = 'empty'
    field[4][14].status = 'empty'
    field[3][14].status = 'empty'
    field[2][14].status = 'empty'
    field[1][14].status = 'empty'
    field[2][13].status = 'empty'
    field[2][12].status = 'empty'
    field[2][1].status = 'wall'
    field[3][2].status = 'wall'
    field[3][3].status = 'wall'
    field[4][3].status = 'wall'
    field[3][1].status = 'wall'
    field[4][4].status = 'wall'
    field[4][5].status = 'wall'
    field[4][6].status = 'wall'
    field[4][7].status = 'wall'
    field[4][8].status = 'wall'
    field[4][9].status = 'wall'
    field[5][9].status = 'wall'
    field[5][8].status = 'wall'
    field[5][7].status = 'wall'
    field[5][6].status = 'wall'
    field[5][5].status = 'wall'
    field[6][5].status = 'wall'
    field[7][5].status = 'wall'
    field[7][6].status = 'wall'
    field[7][7].status = 'wall'
    field[7][8].status = 'wall'
    field[7][9].status = 'wall'
    field[8][9].status = 'wall'
    field[8][11].status = 'wall'
    field[9][9].status = 'wall'
    field[9][10].status = 'wall'
    field[9][11].status = 'wall'
    field[7][11].status = 'wall'
    field[7][12].status = 'wall'
    field[7][13].status = 'wall'
    field[8][13].status = 'wall'
    field[9][13].status = 'wall'
    field[9][15].status = 'wall'
    field[8][15].status = 'wall'
    field[7][15].status = 'wall'
    field[6][15].status = 'wall'
    field[5][15].status = 'wall'
    field[4][15].status = 'wall'
    field[3][15].status = 'wall'
    field[2][15].status = 'wall'
    field[1][15].status = 'wall'
    field[0][15].status = 'wall'
    field[0][14].status = 'wall'
    field[0][13].status = 'wall'
    field[1][13].status = 'wall'
    field[1][12].status = 'wall'
    field[1][11].status = 'wall'
    field[2][11].status = 'wall'
    field[3][12].status = 'wall'
    field[3][11].status = 'wall'
    field[3][13].status = 'wall'
    field[4][13].status = 'wall'
    field[5][13].status = 'wall'
    field[5][12].status = 'wall'
    field[5][11].status = 'wall'
    field[4][11].status = 'wall'
    field[3][11].status = 'wall'
    field[2][11].status = 'wall'
    field[2][10].status = 'wall'
    field[2][9].status = 'wall'
    field[2][8].status = 'wall'
    field[1][8].status = 'wall'
    field[0][8].status = 'wall'
    field[0][7].status = 'wall'
    field[0][6].status = 'wall'
    field[1][6].status = 'wall'
    field[2][6].status = 'wall'
    field[2][5].status = 'wall'
    field[1][5].status = 'wall'
    field[1][4].status = 'wall'
    field[1][3].status = 'wall'
    field[0][3].status = 'wall'

def setup2(field, player):
    player.cords = [0,4]
    player.start_cords = [0, 4]
    player.end_cords = [8,11]
    player.doors_exit = DOORS_3_C
    field[0][0].status = 'wall'
    field[0][1].status = 'wall'
    field[0][2].status = 'wall'
    field[0][3].status = 'wall'
    field[0][4].status = 'empty'
    field[0][5].status = 'wall'
    field[0][6].status = 'wall'
    field[0][7].status = 'wall'
    field[0][8].status = 'wall'
    field[0][9].status = 'wall'
    field[0][10].status = 'wall'
    field[0][11].status = 'wall'
    field[0][12].status = 'wall'
    field[0][13].status = 'wall'
    field[0][14].status = 'wall'
    field[1][0].status = 'wall'
    field[1][1].status = 'empty'
    field[1][2].status = 'leverc'
    field[1][3].status = 'wall'
    field[1][4].status = 'empty'
    field[1][5].status = 'wall'
    field[1][6].status = 'empty'
    field[1][7].status = 'empty'
    field[1][8].status = 'empty'
    field[1][9].status = 'empty'
    field[1][10].status = 'empty'
    field[1][11].status = 'empty'
    field[1][12].status = 'empty'
    field[1][13].status = 'empty'
    field[1][14].status = 'wall'
    field[1][15].status = 'wall'
    field[1][16].status = 'wall'
    field[1][17].status = 'wall'
    field[2][0].status = 'wall'
    field[2][1].status = 'empty'
    field[2][2].status = 'wall'
    field[2][3].status = 'wall'
    field[2][4].status = 'empty'
    field[2][5].status = 'wall'
    field[2][6].status = 'empty'
    field[2][7].status = 'wall'
    field[2][8].status = 'wall'
    field[2][9].status = 'wall'
    field[2][10].status = 'empty'
    field[2][11].status = 'wall'
    field[2][12].status = 'wall'
    field[2][13].status = 'empty'
    field[2][14].status = 'empty'
    field[2][15].status = 'empty'
    field[2][16].status = 'empty'
    field[2][17].status = 'wall'
    field[3][0].status = 'wall'
    field[3][1].status = 'empty'
    field[3][2].status = 'empty'
    field[3][3].status = 'wall'
    field[3][4].status = 'empty'
    field[3][5].status = 'empty'
    field[3][6].status = 'empty'
    field[3][7].status = 'wall'
    field[3][8].status = 'wall'
    field[3][9].status = 'wall'
    field[3][10].status = 'empty'
    field[3][11].status = 'empty'
    field[3][12].status = 'wall'
    field[3][13].status = 'empty'
    field[3][14].status = 'wall'
    field[3][15].status = 'wall'
    field[3][16].status = 'empty'
    field[3][17].status = 'wall'
    field[4][0].status = 'wall'
    field[4][1].status = 'wall'
    field[4][2].status = 'empty'
    field[4][3].status = 'wall'
    field[4][4].status = 'wall'
    field[4][5].status = 'wall'
    field[4][6].status = 'empty'
    field[4][7].status = 'wall'
    field[4][8].status = 'empty'
    field[4][9].status = 'wall'
    field[4][10].status = 'wall'
    field[4][11].status = 'wall'
    field[4][12].status = 'wall'
    field[4][13].status = 'empty'
    field[4][14].status = 'wall'
    field[4][15].status = 'empty'
    field[4][16].status = 'empty'
    field[4][17].status = 'wall'
    field[5][1].status = 'wall'
    field[5][2].status = 'empty'
    field[5][3].status = 'wall'
    field[5][4].status = 'empty'
    field[5][5].status = 'empty'
    field[5][6].status = 'empty'
    field[5][7].status = 'empty'
    field[5][8].status = 'empty'
    field[5][9].status = 'wall'
    field[5][10].status = 'empty'
    field[5][11].status = 'empty'
    field[5][12].status = 'empty'
    field[5][13].status = 'empty'
    field[5][14].status = 'wall'
    field[5][15].status = 'wall'
    field[5][16].status = 'empty'
    field[5][17].status = 'wall'
    field[6][1].status = 'wall'
    field[6][2].status = 'empty'
    field[6][3].status = 'empty'
    field[6][4].status = 'empty'
    field[6][5].status = 'wall'
    field[6][6].status = 'wall'
    field[6][7].status = 'wall'
    field[6][8].status = 'wall'
    field[6][9].status = 'wall'
    field[6][10].status = 'empty'
    field[6][11].status = 'wall'
    field[6][12].status = 'empty'
    field[6][13].status = 'wall'
    field[6][14].status = 'wall'
    field[6][15].status = 'wall'
    field[6][16].status = 'empty'
    field[6][17].status = 'wall'
    field[7][0].status = 'wall'
    field[7][1].status = 'wall'
    field[7][2].status = 'empty'
    field[7][3].status = 'wall'
    field[7][4].status = 'empty'
    field[7][5].status = 'wall'
    field[7][6].status = 'wall'
    field[7][7].status = 'empty'
    field[7][8].status = 'empty'
    field[7][9].status = 'wall'
    field[7][10].status = 'empty'
    field[7][11].status = 'wall'
    field[7][12].status = 'wall'
    field[7][13].status = 'wall'
    field[7][14].status = 'empty'
    field[7][15].status = 'empty'
    field[7][16].status = 'empty'
    field[7][17].status = 'wall'
    field[8][0].status = 'wall'
    field[8][1].status = 'empty'
    field[8][2].status = 'empty'
    field[8][3].status = 'wall'
    field[8][4].status = 'empty'
    field[8][5].status = 'empty'
    field[8][6].status = 'empty'
    field[8][7].status = 'empty'
    field[8][8].status = 'wall'
    field[8][9].status = 'wall'
    field[8][10].status = 'empty'
    field[8][11].status = 'wall'
    field[8][12].status = 'wall'
    field[8][13].status = 'wall'
    field[8][14].status = 'empty'
    field[8][15].status = 'wall'
    field[8][16].status = 'wall'
    field[8][17].status = 'wall'
    field[9][0].status = 'wall'
    field[9][1].status = 'wall'
    field[9][2].status = 'wall'
    field[9][3].status = 'wall'
    field[9][4].status = 'wall'
    field[9][5].status = 'wall'
    field[9][6].status = 'wall'
    field[9][7].status = 'wall'
    field[9][8].status = 'wall'
    field[9][9].status = 'wall'
    field[9][10].status = 'wall'
    field[9][11].status = 'wall'
    field[9][12].status = 'wall'
    field[9][13].status = 'wall'
    field[9][14].status = 'wall'
    field[9][15].status = 'wall'

def setup3(field,player):
    pass

def start_exit(player,grid):
    # start doors 1
    if (player.start_cords[0] == player.cords[0]) and (player.start_cords[1] == player.cords[1]):
        grid.screen.blit(DOORS_START, [((MARGIN + WIDTH) * player.start_cords[1] + MARGIN) + 215,
                                       ((MARGIN + WIDTH) * player.start_cords[0] + MARGIN) + 170])
    elif (player.start_cords[0] == player.cords[0]) and (player.start_cords[1]+1 == player.cords[1]):
        grid.screen.blit(GDOORS_RIGHT, [((MARGIN + WIDTH) * player.start_cords[1] + MARGIN) + 215,
                                        ((MARGIN + WIDTH) * player.start_cords[0] + MARGIN) + 170])
    # start doors 2
    elif (player.start_cords[0] == player.cords[0]-1) and (player.start_cords[1] == player.cords[1]):
        grid.screen.blit(GDOORS_DOWN, [((MARGIN + WIDTH) * player.start_cords[1] + MARGIN) + 215,
                                        ((MARGIN + WIDTH) * player.start_cords[0] + MARGIN) + 170])
    # exit doors 1
    if (player.end_cords[0] == player.cords[0]) and (player.end_cords[1] == player.cords[1]):
        grid.screen.blit(player.doors_exit, [((MARGIN + WIDTH) * player.end_cords[1] + MARGIN) + 215,
                                       ((MARGIN + WIDTH) * player.end_cords[0] + MARGIN) + 170])
        if player.end_cords == [9,14]:
            setup2(field,player)
        elif player.end_cords == [8,11]:
            setup3(field,player)

    elif (player.end_cords[0]-1 == player.cords[0]) and (player.end_cords[1] == player.cords[1]):
        grid.screen.blit(GDOORS_UP, [((MARGIN + WIDTH) * player.end_cords[1] + MARGIN) + 215,
                                     ((MARGIN + WIDTH) * player.end_cords[0] + MARGIN) + 170])
    #exit doors 3
    elif (player.end_cords[0] == player.cords[0]) and (player.end_cords[1] == player.cords[1]+1):
        if player.doors_exit == DOORS_3_C:
            grid.screen.blit(DOORS_3_C, [((MARGIN + WIDTH) * player.end_cords[1] + MARGIN) + 215,
                                         ((MARGIN + WIDTH) * player.end_cords[0] + MARGIN) + 170])
        elif player.doors_exit == DOORS_3_O:
            grid.screen.blit(DOORS_3_O, [((MARGIN + WIDTH) * player.end_cords[1] + MARGIN) + 215,
                                         ((MARGIN + WIDTH) * player.end_cords[0] + MARGIN) + 170])













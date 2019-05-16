import pygame
import os
import time
os.environ['SDL_VIDEO_CENTERED'] = '1'

def setup1(field,player):
    player.cords = [1, 0]  # start player cords
    player.start_cords = [1, 0]  # start door cords
    player.end_cords = [9, 14]  # end door cords
    player.doors_exit = DOORS_START
    for row in range(10):
        for col in range(18):
            field[row][col].status = 'wall'
    field[1][0].status = 'empty'
    field[1][1].status = 'empty'
    field[1][2].status = 'empty'
    field[1][3].status = 'empty'
    field[1][7].status = 'empty'
    field[1][8].status = 'empty'
    field[1][9].status = 'empty'
    field[1][12].status = 'empty'
    field[1][14].status = 'empty'
    field[2][3].status = 'empty'
    field[2][7].status = 'empty'
    field[2][12].status = 'empty'
    field[2][13].status = 'empty'
    field[2][14].status = 'empty'
    field[2][15].status = 'empty'
    field[2][16].status = 'empty'
    field[3][3].status = 'empty'
    field[3][4].status = 'empty'
    field[3][5].status = 'empty'
    field[3][6].status = 'empty'
    field[3][7].status = 'empty'
    field[3][8].status = 'empty'
    field[3][9].status = 'empty'
    field[3][14].status = 'empty'
    field[4][1].status = 'empty'
    field[4][2].status = 'empty'
    field[4][3].status = 'empty'
    field[4][7].status = 'empty'
    field[4][10].status = 'empty'
    field[4][12].status = 'empty'
    field[4][13].status = 'empty'
    field[4][14].status = 'empty'
    field[4][15].status = 'empty'
    field[4][16].status = 'empty'
    field[5][3].status = 'empty'
    field[5][4].status = 'empty'
    field[5][10].status = 'empty'
    field[5][12].status = 'empty'
    field[5][14].status = 'empty'
    field[5][16].status = 'empty'
    field[6][4].status = 'empty'
    field[6][5].status = 'empty'
    field[6][6].status = 'empty'
    field[6][7].status = 'empty'
    field[6][8].status = 'empty'
    field[6][9].status = 'empty'
    field[6][10].status = 'empty'
    field[6][11].status = 'empty'
    field[6][12].status = 'empty'
    field[6][14].status = 'empty'
    field[6][16].status = 'empty'
    field[7][1].status = 'empty'
    field[7][2].status = 'empty'
    field[7][3].status = 'empty'
    field[7][4].status = 'empty'
    field[7][14].status = 'empty'
    field[7][16].status = 'empty'
    field[8][2].status = 'empty'
    field[8][4].status = 'empty'
    field[8][5].status = 'empty'
    field[8][6].status = 'empty'
    field[8][14].status = 'empty'
    field[8][16].status = 'empty'
    field[9][14].status = 'empty'

def setup(field, player):
    player.cords = [1,0] #start player cords
    player.start_cords = [1, 0] #start door cords
    player.end_cords = [9,14] #end door cords
    player.doors_exit = DOORS_START
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
    player.cords = [0, 9] #[8,10] zeby byc na koncu
    player.start_cords = [0, 9]
    player.end_cords = [9, 10]
    player.doors_exit = DOORS_END_U
    for row in range(10):
        for col in range(18):
            field[row][col].status = 'wall'

    field[0][0].status = 'dark'
    field[1][0].status = 'dark'
    field[7][0].status = 'dark'
    field[8][0].status = 'dark'
    field[9][0].status = 'dark'
    field[0][7].status = 'dark'
    field[7][17].status = 'dark'
    field[8][17].status = 'dark'
    field[9][17].status = 'dark'
    field[0][9].status = 'empty'
    field[1][2].status = 'empty'
    field[1][3].status = 'empty'
    field[1][4].status = 'empty'
    field[1][5].status = 'empty'
    field[1][9].status = 'empty'
    field[1][11].status = 'empty'
    field[1][12].status = 'empty'
    field[1][13].status = 'empty'
    field[1][14].status = 'empty'
    field[1][15].status = 'empty'
    field[1][16].status = 'empty'
    field[2][3].status = 'empty'
    field[2][5].status = 'empty'
    field[2][7].status = 'empty'
    field[2][8].status = 'empty'
    field[2][9].status = 'empty'
    field[2][10].status = 'empty'
    field[2][11].status = 'empty'
    field[2][16].status = 'empty'
    field[3][1].status = 'empty'
    field[3][2].status = 'empty'
    field[3][3].status = 'empty'
    field[3][5].status = 'empty'
    field[3][6].status = 'empty'
    field[3][7].status = 'empty'
    field[3][9].status = 'empty'
    field[3][11].status = 'empty'
    field[3][12].status = 'empty'
    field[3][13].status = 'empty'
    field[3][14].status = 'empty'
    field[3][16].status = 'empty'
    field[4][2].status = 'empty'
    field[4][6].status = 'empty'
    field[4][14].status = 'empty'
    field[4][16].status = 'empty'
    field[5][1].status = 'empty'
    field[5][2].status = 'empty'
    field[5][4].status = 'empty'
    field[5][5].status = 'empty'
    field[5][6].status = 'empty'
    field[5][7].status = 'empty'
    field[5][9].status = 'empty'
    field[5][10].status = 'empty'
    field[5][11].status = 'empty'
    field[5][14].status = 'empty'
    field[5][15].status = 'empty'
    field[5][16].status = 'empty'
    field[6][2].status = 'empty'
    field[6][3].status = 'empty'
    field[6][4].status = 'empty'
    field[6][9].status = 'empty'
    field[6][11].status = 'empty'
    field[6][12].status = 'empty'
    field[6][13].status = 'empty'
    field[6][14].status = 'empty'
    field[7][4].status = 'empty'
    field[7][6].status = 'empty'
    field[7][5].status = 'hidden_c' #hidden_c
    field[7][7].status = 'empty'
    field[7][9].status = 'empty'
    field[7][12].status = 'empty'
    field[8][2].status = 'empty'
    field[8][3].status = 'empty'
    field[8][4].status = 'empty'
    field[8][7].status = 'scroll' #spell to beat skeleton
    field[8][9].status = 'empty'
    field[8][10].status = 'skeleton' #skeleton
    field[8][12].status = 'empty'
    field[8][13].status = 'empty'
    field[8][14].status = 'empty'
    field[8][15].status = 'leverc' #lever
    field[9][10].status = 'end'

def end(field,player):
    for row in range(10):
        for col in range(18):
            field[row][col].status = None
    player.cords = [4, 8]
    player.start_cords = [4, 8]
    player.end_cords = [2, 16]
    field[1][7].status = 'w_r_b'
    field[1][8].status = 'w_d'
    field[1][9].status = 'w_d'
    field[1][10].status = 'w_l_b'
    field[2][6].status = 'w_r_b'
    field[2][7].status = 'w_4'
    field[2][8].status = 'empty'
    field[2][9].status = 'empty'
    field[2][10].status = 'w_3'
    field[2][11].status = 'w_l_b'
    field[3][5].status = 'w_r_b'
    field[3][6].status = 'w_4'
    field[3][7].status = 'empty'
    field[3][8].status = 'empty'
    field[3][9].status = 'empty'
    field[3][10].status = 'empty'
    field[3][11].status = 'w_3'
    field[3][12].status = 'w_l_b'
    field[4][5].status = 'w_r'
    field[4][6].status = 'empty'
    field[4][7].status = 'empty'
    field[4][8].status = 'doors'
    field[4][9].status = 'empty'
    field[4][10].status = 'empty'
    field[4][11].status = 'empty'
    field[4][12].status = 'w_l'
    field[5][5].status = 'w_r'
    field[5][6].status = 'empty'
    field[5][7].status = 'empty'
    field[5][8].status = 'empty'
    field[5][9].status = 'empty'
    field[5][10].status = 'empty'
    field[5][11].status = 'empty'
    field[5][12].status = 'w_l'
    field[6][5].status = 'w_t_r'
    field[6][6].status = 'w_1'
    field[6][7].status = 'empty'
    field[6][8].status = 'empty'
    field[6][9].status = 'empty'
    field[6][10].status = 'empty'
    field[6][11].status = 'w_2'
    field[6][12].status = 'w_t_l'
    field[7][6].status = 'w_t_r'
    field[7][7].status = 'w_1'
    field[7][8].status = 'empty'
    field[7][9].status = 'empty'
    field[7][10].status = 'w_2'
    field[7][11].status = 'w_t_l'
    field[8][7].status = 'w_t_r'
    field[8][8].status = 'w_t'
    field[8][9].status = 'w_t'
    field[8][10].status = 'w_t_l'

#-------DISPLAY-------#

WINDOW = [1600,900]
WIDTH = 55
MARGIN = 1
BACKGROUND = pygame.image.load('backgrounds/maze1.png')
INTERFACE = pygame.image.load('interface/empty.png')
#-------LEVELS-------#
LEVEL1 = pygame.image.load('levels/1.png')
LEVEL1 = pygame.transform.scale(LEVEL1, (250, 130))

LEVEL2 = pygame.image.load('levels/2.png')
LEVEL2 = pygame.transform.scale(LEVEL2, (250, 130))

LEVEL3 = pygame.image.load('levels/3.png')
LEVEL3 = pygame.transform.scale(LEVEL3, (250, 130))
#--------WALLS--------#

            #vvv blue walls vvv
WALL = pygame.image.load('wall/wall.png')
WALL = pygame.transform.scale(WALL, (WIDTH, WIDTH))

W_D = pygame.image.load('wall/blue/w_d.png')
W_D = pygame.transform.scale(W_D, (WIDTH, WIDTH))

W_R = pygame.image.load('wall/blue/w_r.png')
W_R = pygame.transform.scale(W_R, (WIDTH, WIDTH))

W_T = pygame.image.load('wall/blue/w_t.png')
W_T = pygame.transform.scale(W_T, (WIDTH, WIDTH))

W_L = pygame.image.load('wall/blue/w_l.png')
W_L = pygame.transform.scale(W_L, (WIDTH, WIDTH))

W_L_B = pygame.image.load('wall/blue/w_l_b.png')
W_L_B = pygame.transform.scale(W_L_B, (WIDTH, WIDTH))

W_R_B = pygame.image.load('wall/blue/w_r_b.png')
W_R_B = pygame.transform.scale(W_R_B, (WIDTH, WIDTH))

W_T_R = pygame.image.load('wall/blue/w_t_r.png')
W_T_R = pygame.transform.scale(W_T_R, (WIDTH, WIDTH))

W_T_L = pygame.image.load('wall/blue/w_t_l.png')
W_T_L = pygame.transform.scale(W_T_L, (WIDTH, WIDTH))

                # vvv yellow walls vvv
Y_W_R_B = pygame.image.load('wall/yellow/w_r_b.png')
Y_W_R_B = pygame.transform.scale(Y_W_R_B, (WIDTH, WIDTH))

Y_W_L_B = pygame.image.load('wall/yellow/w_l_b.png')
Y_W_L_B = pygame.transform.scale(Y_W_L_B, (WIDTH, WIDTH))

Y_W_R_T = pygame.image.load('wall/yellow/w_t_r.png')
Y_W_R_T = pygame.transform.scale(Y_W_R_T, (WIDTH, WIDTH))

Y_W_L_T = pygame.image.load('wall/yellow/w_t_l.png')
Y_W_L_T = pygame.transform.scale(Y_W_L_T, (WIDTH, WIDTH))

Y_W_D = pygame.image.load('wall/yellow/w_d.png')
Y_W_D = pygame.transform.scale(Y_W_D, (WIDTH, WIDTH))

Y_W_T = pygame.image.load('wall/yellow/w_t.png')
Y_W_T = pygame.transform.scale(Y_W_T, (WIDTH, WIDTH))

Y_W_R = pygame.image.load('wall/yellow/w_r.png')
Y_W_R = pygame.transform.scale(Y_W_R, (WIDTH, WIDTH))

Y_W_L = pygame.image.load('wall/yellow/w_l.png')
Y_W_L = pygame.transform.scale(Y_W_L, (WIDTH, WIDTH))

Y_W_1 = pygame.image.load('wall/yellow/w_1.png')
Y_W_1 = pygame.transform.scale(Y_W_1, (WIDTH, WIDTH))

Y_W_2 = pygame.image.load('wall/yellow/w_2.png')
Y_W_2 = pygame.transform.scale(Y_W_2, (WIDTH, WIDTH))

Y_W_3 = pygame.image.load('wall/yellow/w_3.png')
Y_W_3 = pygame.transform.scale(Y_W_3, (WIDTH, WIDTH))

Y_W_4 = pygame.image.load('wall/yellow/w_4.png')
Y_W_4 = pygame.transform.scale(Y_W_4, (WIDTH, WIDTH))

#--------DOORS--------#
DOORS_START = pygame.image.load('doors/blue/doors_start.png')
DOORS_START = pygame.transform.scale(DOORS_START, (WIDTH, WIDTH))

DOORS_START3 = pygame.image.load('doors/blue/doors_start3.png')
DOORS_START3 = pygame.transform.scale(DOORS_START3, (WIDTH, WIDTH))

DOORS_START3_D = pygame.image.load('doors/blue/doors_start3_d.png')
DOORS_START3_D = pygame.transform.scale(DOORS_START3_D, (WIDTH, WIDTH))

DOORS_1 = pygame.image.load('doors/doors1.png')
DOORS_1 = pygame.transform.scale(DOORS_1, (WIDTH, WIDTH))

DOORS_3_C = pygame.image.load('doors/blue/d3_closed.png')
DOORS_3_C = pygame.transform.scale(DOORS_3_C, (WIDTH, WIDTH))

DOORS_3_IN = pygame.image.load('doors/blue/d3_in.png')
DOORS_3_IN = pygame.transform.scale(DOORS_3_IN, (WIDTH, WIDTH))

DOORS_3_O = pygame.image.load('doors/blue/d3_opened.png')
DOORS_3_O = pygame.transform.scale(DOORS_3_O, (WIDTH, WIDTH))

DOORS_3_O_R = pygame.image.load('doors/blue/d3_opened_r.png')
DOORS_3_O_R = pygame.transform.scale(DOORS_3_O_R, (WIDTH, WIDTH))

DOORS_3_C_R = pygame.image.load('doors/blue/d3_closed_r.png')
DOORS_3_C_R = pygame.transform.scale(DOORS_3_C_R, (WIDTH, WIDTH))

DOORS_3_C_UP = pygame.image.load('doors/blue/d3_closed_up.png')
DOORS_3_C_UP = pygame.transform.scale(DOORS_3_C_UP, (WIDTH, WIDTH))

GDOORS_UP = pygame.image.load('doors/blue/glow_d_up.png')
GDOORS_UP = pygame.transform.scale(GDOORS_UP, (WIDTH, WIDTH))

GDOORS_DOWN = pygame.image.load('doors/blue/doors2.png')
GDOORS_DOWN = pygame.transform.scale(GDOORS_DOWN, (WIDTH, WIDTH))

GDOORS_RIGHT = pygame.image.load('doors/blue/glow_d_right.png')
GDOORS_RIGHT= pygame.transform.scale(GDOORS_RIGHT, (WIDTH, WIDTH))

HIDDEN_C = pygame.image.load('doors/blue/hidden_c.png')
HIDDEN_C = pygame.transform.scale(HIDDEN_C, (WIDTH, WIDTH))

HIDDEN_C_B = pygame.image.load('doors/blue/hidden_c_b.png')
HIDDEN_C_B = pygame.transform.scale(HIDDEN_C_B, (WIDTH, WIDTH))

HIDDEN_C_T = pygame.image.load('doors/blue/hidden_c_t.png')
HIDDEN_C_T = pygame.transform.scale(HIDDEN_C_T, (WIDTH, WIDTH))

DOORS_END_U = pygame.image.load('doors/blue/end_u.png')
DOORS_END_U= pygame.transform.scale(DOORS_END_U, (WIDTH, WIDTH))

DOORS_END_C = pygame.image.load('doors/blue/end_c.png')
DOORS_END_C= pygame.transform.scale(DOORS_END_C, (WIDTH, WIDTH))

DOORS_END_DR = pygame.image.load('doors/blue/end_dr.png')
DOORS_END_DR= pygame.transform.scale(DOORS_END_DR, (WIDTH, WIDTH))

DOORS_END = pygame.image.load('doors/yellow/y_end.png')
DOORS_END= pygame.transform.scale(DOORS_END, (WIDTH, WIDTH))

DOORS_END_IN = pygame.image.load('doors/yellow/y_end_in.png')
DOORS_END_IN = pygame.transform.scale(DOORS_END_IN, (WIDTH, WIDTH))

#--------FLOORS--------#
FLOOR = pygame.image.load('floor/floor.png')
FLOOR = pygame.transform.scale(FLOOR, (WIDTH, WIDTH))

GFLOOR_L_B = pygame.image.load('floor/blue/glow_f_b_l.png')
GFLOOR_L_B = pygame.transform.scale(GFLOOR_L_B, (WIDTH, WIDTH))

GFLOOR_R_B = pygame.image.load('floor/blue/glow_f_b_r.png')
GFLOOR_R_B = pygame.transform.scale(GFLOOR_R_B, (WIDTH, WIDTH))

GFLOOR_T_L = pygame.image.load('floor/blue/glow_f_t_l.png')
GFLOOR_T_L = pygame.transform.scale(GFLOOR_T_L, (WIDTH, WIDTH))

GFLOOR_T_R = pygame.image.load('floor/blue/glow_f_t_r.png')
GFLOOR_T_R = pygame.transform.scale(GFLOOR_T_R, (WIDTH, WIDTH))

GFLOOR_CENTER = pygame.image.load('floor/blue/glow_f_center.png')
GFLOOR_CENTER = pygame.transform.scale(GFLOOR_CENTER, (WIDTH, WIDTH))

GFLOOR_LEFT = pygame.image.load('floor/blue/glow_f_left.png')
GFLOOR_LEFT = pygame.transform.scale(GFLOOR_LEFT, (WIDTH, WIDTH))

GFLOOR_RIGHT = pygame.image.load('floor/blue/glow_f_right.png')
GFLOOR_RIGHT = pygame.transform.scale(GFLOOR_RIGHT, (WIDTH, WIDTH))

GFLOOR_UP = pygame.image.load('floor/blue/glow_f_down.png')
GFLOOR_UP = pygame.transform.scale(GFLOOR_UP, (WIDTH, WIDTH))

GFLOOR_DOWN = pygame.image.load('floor/blue/glow_f_up.png')
GFLOOR_DOWN = pygame.transform.scale(GFLOOR_DOWN, (WIDTH, WIDTH))

#--------PLAYER---------#
PLAYER_UP = pygame.image.load('characters/hero/mage/mage_up.png')
PLAYER_UP = pygame.transform.scale(PLAYER_UP, (WIDTH, WIDTH))

PLAYER1 = pygame.image.load('characters/hero/mage/mage1.png')
PLAYER1= pygame.transform.scale(PLAYER1, (WIDTH, WIDTH))

PLAYER2 = pygame.image.load('characters/hero/mage/mage2.png')
PLAYER2 = pygame.transform.scale(PLAYER2, (WIDTH, WIDTH))

PLAYER3 = pygame.image.load('characters/hero/mage/mage3.png')
PLAYER3 = pygame.transform.scale(PLAYER3, (WIDTH, WIDTH))

PLAYER4 = pygame.image.load('characters/hero/mage/mage4.png')
PLAYER4 = pygame.transform.scale(PLAYER4, (WIDTH, WIDTH))

PLAYER_DOWN = pygame.image.load('characters/hero/mage/mage_d.png')
PLAYER_DOWN = pygame.transform.scale(PLAYER_DOWN, (WIDTH, WIDTH))

PLAYER_LEFT = pygame.image.load('characters/hero/mage/mage_l.png')
PLAYER_LEFT = pygame.transform.scale(PLAYER_LEFT, (WIDTH, WIDTH))

PLAYER_RIGHT = pygame.image.load('characters/hero/mage/mage_r.png')
PLAYER_RIGHT = pygame.transform.scale(PLAYER_RIGHT, (WIDTH, WIDTH))

PLAYER_SCROLL = pygame.image.load('characters/hero/mage/mage_scroll2.png')
PLAYER_SCROLL = pygame.transform.scale(PLAYER_SCROLL, (WIDTH, WIDTH))

#------CHARACTERS------#
SKELETON_DR = pygame.image.load('characters/skeleton/skeleton_d_r.png')
SKELETON_DR = pygame.transform.scale(SKELETON_DR, (WIDTH, WIDTH))

SKELETON_R = pygame.image.load('characters/skeleton/skeleton_r.png')
SKELETON_R = pygame.transform.scale(SKELETON_R, (WIDTH, WIDTH))

SKELETON_K_R = pygame.image.load('characters/skeleton/skeleton_killed_r.png')
SKELETON_K_R = pygame.transform.scale(SKELETON_K_R, (WIDTH, WIDTH))

SKELETON_KILL = pygame.image.load('characters/skeleton/skeleton_killing.png')
SKELETON_KILL = pygame.transform.scale(SKELETON_KILL, (WIDTH, WIDTH))

SKELETON_K_DR = pygame.image.load('characters/skeleton/skeleton_killed_dr.png')
SKELETON_K_DR = pygame.transform.scale(SKELETON_K_DR, (WIDTH, WIDTH))

SKELETON_K_U = pygame.image.load('characters/skeleton/skeleton_killed_u.png')
SKELETON_K_U = pygame.transform.scale(SKELETON_K_U, (WIDTH, WIDTH))

SKELETON_K_C = pygame.image.load('characters/skeleton/skeleton_killed_c.png')
SKELETON_K_C = pygame.transform.scale(SKELETON_K_C, (WIDTH, WIDTH))
#--------ITEMS---------#
LEVER_C = pygame.image.load('items/blue/lever/lever_closed.png')
LEVER_C = pygame.transform.scale(LEVER_C, (WIDTH, WIDTH))

LEVER_O = pygame.image.load('items/blue/lever/lever_opened.png')
LEVER_O = pygame.transform.scale(LEVER_O, (WIDTH, WIDTH))

LEVER_O_C = pygame.image.load('items/blue/lever/lever_opened_c.png')
LEVER_O_C = pygame.transform.scale(LEVER_O_C, (WIDTH, WIDTH))

LEVER_C_R = pygame.image.load('items/blue/lever/lever_closed_r.png')
LEVER_C_R = pygame.transform.scale(LEVER_C_R, (WIDTH, WIDTH))

LEVER_O_R = pygame.image.load('items/blue/lever/lever_opened_r.png')
LEVER_O_R = pygame.transform.scale(LEVER_O_R, (WIDTH, WIDTH))

SCROLL = pygame.image.load('items/blue/scroll/scroll_up.png')
SCROLL = pygame.transform.scale(SCROLL, (WIDTH, WIDTH))

SCROLL_EQ = pygame.image.load('interface/scroll_eq.png')
SCROLL_EQ = pygame.transform.scale(SCROLL_EQ, (WIDTH-20, WIDTH-20))

SCROLL_L_R = pygame.image.load('items/blue/scroll/scroll_l_r.png')
SCROLL_L_R = pygame.transform.scale(SCROLL_L_R, (WIDTH, WIDTH))

GOLD = pygame.image.load('items/treasuers/1.png')
GOLD = pygame.transform.scale(GOLD, (WIDTH*2, WIDTH*2))

#---------SOUNDS--------#
pygame.init()
BOLT = pygame.mixer.Sound('sounds/bolt.wav')
pygame.mixer.music.load('sounds/music.wav')
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














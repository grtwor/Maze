from config import *

class Grid:
    def __init__(self, grid):
        self.screen = pygame.display.set_mode(WINDOW)
        self.bg = BACKGROUND
        self.bg =pygame.transform.scale(self.bg, (WINDOW[0], WINDOW[1]))
        self.grid = grid
        self.tries = 0
        self.bad_roads = []
        self.interface = []

    def checkpoints(self):
        for row in range(10):
            for col in range(18):
                x = self.mask_checkpoints(row,col)
                if x > 2:
                    self.grid[row][col].checkpoint = [row,col]
                    self.grid[row][col].roads_c = x-1
                    #print(row, col, self.grid[row][col].checkpoint)
                elif x == 1 and ([row,col] != [1,0]):
                    self.grid[row][col].bad_road = [row,col]

    def mask_checkpoints(self, row, col):
        neight = 0
        if (self.isValid(row-1, col) == True):
            if self.grid[row-1][col].status == 'empty':
                neight += 1
        if (self.isValid(row + 1, col) == True):
            if self.grid[row + 1][col].status == 'empty':
                neight += 1
        if (self.isValid(row, col+1) == True):
            if self.grid[row][col+1].status == 'empty':
                neight += 1
        if (self.isValid(row, col-1) == True):
            if self.grid[row][col-1].status == 'empty':
                neight += 1
        return neight

    def draw(self, player, level):
        if player.won == True:
            self.screen.blit(self.bg, (0, 0))
            for row in range(10):
                for col in range(18):
                    x = ((MARGIN + WIDTH) * col + MARGIN) + 215
                    y = ((MARGIN + WIDTH) * row + MARGIN) + 170
                    if self.grid[row][col].status == 'w_r_b':
                        self.screen.blit(Y_W_R_B, (x, y))
                    elif self.grid[row][col].status == 'w_l_b':
                        self.screen.blit(Y_W_L_B, (x, y))
                    elif self.grid[row][col].status == 'w_t_r':
                        self.screen.blit(Y_W_R_T, (x, y))
                    elif self.grid[row][col].status == 'w_t_l':
                        self.screen.blit(Y_W_L_T, (x, y))
                    elif self.grid[row][col].status == 'w_r':
                        self.screen.blit(Y_W_R, (x, y))
                    elif self.grid[row][col].status == 'w_l':
                        self.screen.blit(Y_W_L, (x, y))
                    elif self.grid[row][col].status == 'w_t':
                        self.screen.blit(Y_W_T, (x, y))
                    elif self.grid[row][col].status == 'w_d':
                        self.screen.blit(Y_W_D, (x, y))
                    elif self.grid[row][col].status == 'wall':
                        self.screen.blit(WALL, (x, y))
                    elif self.grid[row][col].status == 'w_1':
                        self.screen.blit(Y_W_1, (x, y))
                    elif self.grid[row][col].status == 'w_2':
                        self.screen.blit(Y_W_2, (x, y))
                    elif self.grid[row][col].status == 'w_3':
                        self.screen.blit(Y_W_3, (x, y))
                    elif self.grid[row][col].status == 'w_4':
                        self.screen.blit(Y_W_4, (x, y))
                    elif self.grid[row][col].status == 'doors':
                        self.screen.blit(DOORS_END, (x, y))

                    elif self.grid[row][col].status == 'empty':
                        self.screen.blit(FLOOR, (x, y))
                    self.screen.blit(GOLD, (780, 360))
                    if row == player.cords[0] and col == player.cords[1]:
                        self.screen.blit(player.img, (x, y))
                        if player.cords == [4, 8]:
                            self.screen.blit(DOORS_END_IN, (x, y))

        else:
            self.screen.fill(GREY)
            self.screen.blit(self.bg, (0, 0))
            for row in range(10):
                for col in range(18):
                    x = (( MARGIN + WIDTH ) * col + MARGIN ) + 300
                    y = ((MARGIN + WIDTH) * row + MARGIN)+ 135
                    if self.grid[row][col].show == False:
                        pygame.draw.rect(self.screen, BLACK, (x, y, WIDTH, WIDTH))
                    if row == player.cords[0] and col == player.cords[1]:
                        self.mask(row,col,player, level)
                        self.screen.blit(player.img, (x, y))
                    self.start_exit(player,self)
            for row in range(10):
                for col in range(18):
                     self.grid[row][col].show = False

    def start_exit(self,player,grid):
        # start doors 1

        if (player.start_cords[0] == player.cords[0]) and (player.start_cords[1] == player.cords[1]):
            if player.start_cords == [1, 0]:
                grid.screen.blit(DOORS_START, [((MARGIN + WIDTH) * player.start_cords[1] + MARGIN) + 300,
                                               ((MARGIN + WIDTH) * player.start_cords[0] + MARGIN) + 135])
            elif player.start_cords == [0, 4]:
                grid.screen.blit(DOORS_START, [((MARGIN + WIDTH) * player.start_cords[1] + MARGIN) + 300,
                                               ((MARGIN + WIDTH) * player.start_cords[0] + MARGIN) + 135])
            elif player.start_cords == [0,9]:
                grid.screen.blit(DOORS_START3, [((MARGIN + WIDTH) * player.start_cords[1] + MARGIN) + 300,
                                               ((MARGIN + WIDTH) * player.start_cords[0] + MARGIN) + 135])
        elif (player.start_cords[0] == player.cords[0]) and (player.start_cords[1] + 1 == player.cords[1]):
            grid.screen.blit(GDOORS_RIGHT, [((MARGIN + WIDTH) * player.start_cords[1] + MARGIN) + 300,
                                            ((MARGIN + WIDTH) * player.start_cords[0] + MARGIN) + 135])
        # start doors 2
        elif (player.start_cords[0] == player.cords[0] - 1) and (player.start_cords[1] == player.cords[1]):
            if player.start_cords == [0,4]:
                grid.screen.blit(GDOORS_DOWN, [((MARGIN + WIDTH) * player.start_cords[1] + MARGIN) + 300,
                                               ((MARGIN + WIDTH) * player.start_cords[0] + MARGIN) + 135])
            elif player.start_cords == [0,9]:
                grid.screen.blit(DOORS_START3_D, [((MARGIN + WIDTH) * player.start_cords[1] + MARGIN) + 300,
                                               ((MARGIN + WIDTH) * player.start_cords[0] + MARGIN) + 135])

        # exit doors
        if (player.end_cords[0] == player.cords[0]) and (player.end_cords[1] == player.cords[1]):
            grid.screen.blit(player.doors_exit, [((MARGIN + WIDTH) * player.end_cords[1] + MARGIN) + 300,
                                                 ((MARGIN + WIDTH) * player.end_cords[0] + MARGIN) + 135])
        elif (player.end_cords[0] - 1 == player.cords[0]) and (player.end_cords[1] == player.cords[1]):
            if player.end_cords == [9,14]:
                grid.screen.blit(GDOORS_UP, [((MARGIN + WIDTH) * player.end_cords[1] + MARGIN) + 300,
                                             ((MARGIN + WIDTH) * player.end_cords[0] + MARGIN) + 135])
            elif player.end_cords == [9,10]:
                grid.screen.blit(DOORS_END_U, [((MARGIN + WIDTH) * player.end_cords[1] + MARGIN) + 300,
                                             ((MARGIN + WIDTH) * player.end_cords[0] + MARGIN) + 135])
        # exit doors 3
        elif (player.end_cords[0] == player.cords[0]) and (player.end_cords[1] == player.cords[1] + 1):
            if player.doors_exit == DOORS_3_C:
                grid.screen.blit(DOORS_3_C, [((MARGIN + WIDTH) * player.end_cords[1] + MARGIN) + 300,
                                             ((MARGIN + WIDTH) * player.end_cords[0] + MARGIN) + 135])
            elif player.doors_exit == DOORS_3_O:
                grid.screen.blit(DOORS_3_O, [((MARGIN + WIDTH) * player.end_cords[1] + MARGIN) + 300,
                                             ((MARGIN + WIDTH) * player.end_cords[0] + MARGIN) + 135])

        elif (player.end_cords[0] == player.cords[0] + 1) and (player.end_cords[1] == player.cords[1] + 1):
            if player.end_cords == [8, 11]:
                if player.doors_exit == DOORS_3_C:
                    grid.screen.blit(DOORS_3_C_R, [((MARGIN + WIDTH) * player.end_cords[1] + MARGIN) + 300,
                                                   ((MARGIN + WIDTH) * player.end_cords[0] + MARGIN) + 135])
                elif player.doors_exit == DOORS_3_O:
                    grid.screen.blit(DOORS_3_O_R, [((MARGIN + WIDTH) * player.end_cords[1] + MARGIN) + 300,
                                                   ((MARGIN + WIDTH) * player.end_cords[0] + MARGIN) + 135])
            elif player.end_cords == [9,10]:
                grid.screen.blit(DOORS_END_DR, [((MARGIN + WIDTH) * player.end_cords[1] + MARGIN) + 300,
                                               ((MARGIN + WIDTH) * player.end_cords[0] + MARGIN) + 135])

    def getxy(self,row,col):
        x = ((MARGIN + WIDTH) * col + MARGIN) + 300
        y = ((MARGIN + WIDTH) * row + MARGIN) + 135
        l = [x,y]
        return l

    def isValid(self,row,col):
        return (row >= 0) and (row <= 9) and (col >= 0) and (col <= 17)

    def mask(self,row,col,player, level):
        if (self.isValid(row, col) == True):
            if level == LEVEL1:
                if self.grid[row][col].checkpoint == player.cords:
                    if player.cords != player.c_checkpoint:
                        player.prev_checkpoint = player.c_checkpoint
                        self.bad_roads.clear()
                    print(player.prev_checkpoint, self.grid[row][col].roads_c, len(self.bad_roads))
                    player.c_checkpoint = [row,col]

                #print(player.c_checkpoint)

                if (self.grid[row][col].bad_road == player.cords) and (player.cords != player.end_cords):
                    if not((row,col) in self.bad_roads):
                        self.bad_roads.append((row, col))
                    player.cords = player.c_checkpoint

                if len(self.bad_roads) == self.grid[player.c_checkpoint[0]][player.c_checkpoint[1]].roads_c:
                    #print(self.bad_roads)
                    player.cords = player.prev_checkpoint
                    self.bad_roads.clear()


            l = self.getxy(row, col)
            if (self.grid[row][col].status == 'empty'):
                self.screen.blit(GFLOOR_CENTER, (l[0], l[1]))
            elif (self.grid[row][col].status == 'leverc'):
                self.grid[row][col].status = 'levero'
                self.screen.blit(LEVER_O, (l[0], l[1]))
            elif (self.grid[row][col].status == 'levero'):
                self.screen.blit(LEVER_O_C, (l[0], l[1]))
                if player.end_cords == [8,11]:
                    player.doors_exit = DOORS_3_O
                    self.grid[8][11].status = 'door_o'
                elif player.end_cords == [9,10]:
                    self.grid[7][5].status = 'empty'
            elif self.grid[row][col].status == 'door_o':
                player.doors_exit = DOORS_3_IN
            elif (self.grid[row][col].status == 'scroll'):
                self.grid[row][col].status = 'empty'
                #self.grid[row][col]
                player.scroll = True
                player.eq['scroll'] = SCROLL_EQ
            elif (self.grid[row][col].status == 'skeleton_killed'):
                self.screen.blit(SKELETON_K_C, (l[0], l[1]))
            elif (self.grid[row][col].status == 'end'):
                player.doors_exit = DOORS_END_C

            self.grid[row][col].show = True

        if (self.isValid(row - 1, col) == True):
            l = self.getxy(row-1, col)
            if (self.grid[row-1][col].status == 'wall'):
                self.screen.blit(W_D, (l[0], l[1]))
            elif (self.grid[row-1][col].status == 'dark'):
                pygame.draw.rect(self.screen, BLACK, (l[0], l[1], WIDTH, WIDTH))
            elif (self.grid[row-1][col].status == 'empty'):
                self.screen.blit(GFLOOR_DOWN, (l[0], l[1]))
            elif (self.grid[row-1][col].status == 'skeleton_killed'):
                self.screen.blit(SKELETON_K_U, (l[0], l[1]))
            self.grid[row-1][col].show = True

        if (self.isValid(row + 1, col) == True):
            l = self.getxy(row+1,col)
            if (self.grid[row+1][col].status == 'wall'):
                self.screen.blit(W_T, (l[0], l[1]))
            elif (self.grid[row+1][col].status == 'dark'):
                pygame.draw.rect(self.screen, BLACK, (l[0], l[1], WIDTH, WIDTH))
            elif (self.grid[row+1][col].status == 'empty'):
                self.screen.blit(GFLOOR_UP, (l[0], l[1]))
            elif (self.grid[row+1][col].status == 'scroll'):
                self.screen.blit(SCROLL, (l[0], l[1]))

            self.grid[row+1][col].show = True

        if (self.isValid(row, col+1) == True):
            l = self.getxy(row,col+1)
            if (self.grid[row][col+1].status == 'wall'):
                self.screen.blit(W_L, (l[0], l[1]))
            elif (self.grid[row][col+1].status == 'dark'):
                pygame.draw.rect(self.screen, BLACK, (l[0], l[1], WIDTH, WIDTH))
            elif (self.grid[row][col+1].status == 'empty'):
                self.screen.blit(GFLOOR_LEFT, (l[0], l[1]))
            elif (self.grid[row][col + 1].status == 'leverc'):
                self.screen.blit(LEVER_C, (l[0], l[1]))
            elif (self.grid[row][col + 1].status == 'levero'):
                self.screen.blit(LEVER_O, (l[0], l[1]))
            elif (self.grid[row][col+1].status == 'door_o'):
                self.screen.blit(DOORS_3_O, (l[0],l[1]))
            elif (self.grid[row][col+1].status == 'skeleton'):
                if player.scroll == True:
                    self.grid[row][col+1].status = 'skeleton_killed'
                    self.screen.blit(SKELETON_KILL, (l[0], l[1]))
                    player.img = PLAYER_SCROLL
                    player.scroll = False
                    player.eq['scroll'] = None
                else:
                    self.screen.blit(SKELETON_R, (l[0],l[1]))
            elif (self.grid[row][col + 1].status == 'hidden_c'):
                self.screen.blit(HIDDEN_C, (l[0], l[1]))
            elif (self.grid[row][col + 1].status == 'skeleton_killed'):
                self.screen.blit(SKELETON_K_R, (l[0], l[1]))
            self.grid[row][col+1].show = True

        if (self.isValid(row, col-1) == True):
            l = self.getxy(row,col-1)
            if (self.grid[row][col-1].status == 'wall'):
                self.screen.blit(W_R, (l[0], l[1]))
            elif (self.grid[row][col-1].status == 'dark'):
                pygame.draw.rect(self.screen, BLACK, (l[0], l[1], WIDTH, WIDTH))
            elif (self.grid[row][col-1].status == 'empty'):
                self.screen.blit(GFLOOR_RIGHT, (l[0], l[1]))
            self.grid[row][col-1].show = True

        if (self.isValid(row - 1, col+1) == True):
            l = self.getxy(row-1, col+1)
            if (self.grid[row-1][col+1].status == 'wall'):
                self.screen.blit(W_L_B, (l[0], l[1]))
            elif (self.grid[row-1][col+1].status == 'dark'):
                pygame.draw.rect(self.screen, BLACK, (l[0], l[1], WIDTH, WIDTH))
            elif (self.grid[row-1][col+1].status == 'empty'):
                self.screen.blit(GFLOOR_L_B, (l[0], l[1]))
            elif (self.grid[row-1][col + 1].status == 'leverc'):
                self.screen.blit(LEVER_C_R, (l[0], l[1]))
            elif (self.grid[row-1][col + 1].status == 'levero'):
                self.screen.blit(LEVER_O_R, (l[0], l[1]))
            elif (self.grid[row-1][col+1].status == 'hidden_c'):
                self.screen.blit(HIDDEN_C_B, (l[0], l[1]))
            self.grid[row-1][col+1].show = True

        if (self.isValid(row - 1, col-1) == True):
            l = self.getxy(row-1, col-1)
            if (self.grid[row-1][col-1].status == 'wall'):
                self.screen.blit(W_R_B, (l[0], l[1]))
            elif (self.grid[row-1][col-1].status == 'dark'):
                pygame.draw.rect(self.screen, BLACK, (l[0], l[1], WIDTH, WIDTH))
            elif (self.grid[row-1][col-1].status == 'empty'):
                self.screen.blit(GFLOOR_R_B, (l[0], l[1]))
            self.grid[row-1][col-1].show = True

        if (self.isValid(row + 1, col+1) == True):
            l = self.getxy(row+1, col+1)
            if (self.grid[row+1][col+1].status == 'wall'):
                self.screen.blit(W_T_L, (l[0], l[1]))
            elif (self.grid[row+1][col+1].status == 'dark'):
                pygame.draw.rect(self.screen, BLACK, (l[0], l[1], WIDTH, WIDTH))
            elif (self.grid[row+1][col+1].status == 'empty'):
                self.screen.blit(GFLOOR_T_L, (l[0], l[1]))
            elif (self.grid[row+1][col+1].status == 'door_o'):
                self.screen.blit(DOORS_3_O_R, (l[0], l[1]))
            elif (self.grid[row+1][col+1].status == 'skeleton'):
                self.screen.blit(SKELETON_DR, (l[0], l[1]))
            elif (self.grid[row+1][col+1].status == 'scroll'):
                self.screen.blit(SCROLL_L_R, (l[0], l[1]))
            elif (self.grid[row+1][col+1].status == 'hidden_c'):
                self.screen.blit(HIDDEN_C_T, (l[0], l[1]))
            elif (self.grid[row + 1][col + 1].status == 'skeleton_killed'):
                self.screen.blit(SKELETON_K_DR, (l[0], l[1]))
            self.grid[row+1][col+1].show = True

        if (self.isValid(row + 1, col-1) == True):
            l = self.getxy(row+1, col-1)
            if (self.grid[row+1][col-1].status == 'wall'):
                self.screen.blit(W_T_R, (l[0], l[1]))
            elif (self.grid[row+1][col-1].status == 'dark'):
                pygame.draw.rect(self.screen, BLACK, (l[0], l[1], WIDTH, WIDTH))
            elif (self.grid[row+1][col-1].status == 'empty'):
                self.screen.blit(GFLOOR_T_R, (l[0], l[1]))
            self.grid[row+1][col-1].show = True


class Field:
    def __init__(self):
        self.status = 'dark'
        self.show = False
        self.checkpoint = []
        self.roads_c = None
        self.bad_road = []

class Player:
    def __init__(self):
        self.cords = []
        self.start_cords = []
        self.end_cords = []
        self.eq = {}
        self.dir = ''
        self.img = PLAYER_DOWN
        self.doors_exit = DOORS_1
        self.scroll = False
        self.won = False
        self.prev_checkpoint = self.start_cords
        self.c_checkpoint = self.start_cords

    def move(self, grid):
        row = self.cords[0]
        col = self.cords[1]
        if self.dir == 'left':
            if grid.grid[row][col-1].status == 'empty' and col != 0:
                self.cords[1] -= 1
                if player.won == False:
                    self.img = PLAYER_LEFT
                else:
                    self.img = PLAYER4
        elif self.dir == 'right':
            if grid.grid[row][col + 1].status == 'empty' or grid.grid[row][col + 1].status == 'leverc' or grid.grid[row][col + 1].status == 'door_o'\
                    or grid.grid[row][col + 1].status == 'hidden_o' or grid.grid[row][col+1].status == 'skeleton_killed':
                self.cords[1] +=1
                if player.won == False:
                    self.img = PLAYER_RIGHT
                else:
                    self.img = PLAYER3
        elif self.dir == 'up':
            if grid.grid[row - 1][col].status == 'empty' or grid.grid[row - 1][col].status == 'end' or grid.grid[row - 1][col].status == 'doors':
                self.cords[0] -=1
                if player.won == False:
                    self.img = PLAYER_UP
                else:
                    self.img = PLAYER2
        elif self.dir == 'down':
            if grid.grid[row + 1][col].status == 'empty' or grid.grid[row + 1][col].status == 'end' or grid.grid[row + 1][col].status == 'scroll'  :
                self.cords[0] +=1
                if player.won == False:
                    self.img = PLAYER_DOWN
                else:
                    self.img = PLAYER1

class Main:
    def __init__(self, grid, player):
        self.level = LEVEL1
        pygame.init()
        #pygame.mixer.music.play(-1)
        grid.checkpoints()
        grid.grid[1][0].checkpoint = [1,0]
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player.dir = 'left'
                    elif event.key == pygame.K_RIGHT:
                        player.dir = 'right'
                    elif event.key == pygame.K_UP:
                        player.dir = 'up'
                    elif event.key == pygame.K_DOWN:
                        player.dir = 'down'
                    player.move(grid)
            grid.draw(player,self.level)
            grid.screen.blit(self.level,(1300,700))
            grid.screen.blit(INTERFACE, (1250,800))
            self.slot = 1257
            for value in player.eq.values():
                if value != None:
                    grid.screen.blit(value,(self.slot,807))
                    self.slot+=37
            pygame.display.update()
            if player.img == PLAYER_SCROLL:
                pygame.mixer.Sound.play(BOLT)
                time.sleep(1.2)
                player.img = PLAYER_DOWN
                grid.grid[8][10].status = 'skeleton_killed'

            # exit doors 1
            if player.cords == [9,14]:
                self.level = LEVEL2
                time.sleep(1)
                setup2(field,player)
            # exit doors 3
            elif player.cords == [8,11]:
                self.level = LEVEL3
                time.sleep(1)
                setup3(field,player)
            #end
            elif player.cords == [9,10]:
                #level = WON
                time.sleep(1)
                player.won = True
                player.img = PLAYER1
                end(field,player)

        pygame.quit()



if __name__ == '__main__':
    field = [[Field() for x in range(18)] for y in range(10)]
    player = Player()
    setup1(field, player)
    grid1 = Grid(field)
    Main(grid1, player)
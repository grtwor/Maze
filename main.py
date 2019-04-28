from config import *

class Grid:
    def __init__(self, grid):
        self.screen = pygame.display.set_mode(WINDOW)
        self.bg = BACKGROUND
        self.bg =pygame.transform.scale(self.bg, (WINDOW[0], WINDOW[1]))
        self.grid = grid

    def draw(self, player):
        self.screen.fill(GREY)
        self.screen.blit(self.bg, (0, 0))
        for row in range(10):
            for col in range(18):
                x = (( MARGIN + WIDTH ) * col + MARGIN ) + 215
                y = ((MARGIN + WIDTH) * row + MARGIN)+ 170
                if self.grid[row][col].show == False:
                    pygame.draw.rect(self.screen, BLACK, (x, y, WIDTH, WIDTH))
                if row == player.cords[0] and col == player.cords[1]:
                    self.mask(row,col,player)
                    self.screen.blit(player.img, (x, y))
                start_exit(player,self)

        for row in range(10):
            for col in range(18):
                 self.grid[row][col].show = False

    def getxy(self,row,col):
        x = ((MARGIN + WIDTH) * col + MARGIN) + 215
        y = ((MARGIN + WIDTH) * row + MARGIN) + 170
        l = [x,y]
        return l

    def isValid(self,row,col):
        return (row >= 0) and (row <= 9) and (col >= 0) and (col <= 17)

    def mask(self,row,col,player):
        if (self.isValid(row, col) == True):
            l = self.getxy(row, col)
            if (self.grid[row][col].status == 'empty'):
                self.screen.blit(GFLOOR_CENTER, (l[0], l[1]))
            elif (self.grid[row][col].status == 'leverc'):
                self.grid[row][col].status = 'levero'
                self.screen.blit(LEVER_O, (l[0], l[1]))
            elif (self.grid[row][col].status == 'levero'):
                self.screen.blit(LEVER_O_C, (l[0], l[1]))
                player.doors_exit = DOORS_3_O
                self.grid[8][11].status = 'door_o'
            self.grid[row][col].show = True

        if (self.isValid(row - 1, col) == True):
            l = self.getxy(row-1, col)
            if (self.grid[row-1][col].status == 'wall'):
                self.screen.blit(W_D, (l[0], l[1]))
            elif (self.grid[row-1][col].status == 'dark'):
                pygame.draw.rect(self.screen, BLACK, (l[0], l[1], WIDTH, WIDTH))
            elif (self.grid[row-1][col].status == 'empty'):
                self.screen.blit(GFLOOR_DOWN, (l[0], l[1]))
            self.grid[row-1][col].show = True

        if (self.isValid(row + 1, col) == True):
            l = self.getxy(row+1,col)
            if (self.grid[row+1][col].status == 'wall'):
                self.screen.blit(W_T, (l[0], l[1]))
            elif (self.grid[row+1][col].status == 'dark'):
                pygame.draw.rect(self.screen, BLACK, (l[0], l[1], WIDTH, WIDTH))
            elif (self.grid[row+1][col].status == 'empty'):
                self.screen.blit(GFLOOR_UP, (l[0], l[1]))
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

class Player:
    def __init__(self):
        self.cords = []
        self.start_cords = []
        self.end_cords = []
        self.dir = ''
        self.img = PLAYER_DOWN
        self.doors_exit = DOORS_1

    def move(self, grid):
        row = self.cords[0]
        col = self.cords[1]
        if self.dir == 'left':
            if grid.grid[row][col-1].status != 'wall':
                self.cords[1] -= 1
                self.img = PLAYER_LEFT
        elif self.dir == 'right':
            if grid.grid[row][col + 1].status != 'wall':
                self.cords[1] +=1
                self.img = PLAYER_RIGHT
        elif self.dir == 'up':
            if grid.grid[row - 1][col].status != 'wall':
                self.cords[0] -=1
                self.img = PLAYER_UP
        elif self.dir == 'down':
            if grid.grid[row + 1][col].status != 'wall':
                self.cords[0] +=1
                self.img = PLAYER_DOWN

class Main:
    def __init__(self, grid, player):

        pygame.init()
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
            grid.draw(player)
            pygame.display.update()
        pygame.quit()


if __name__ == '__main__':


    player = Player()
    setup1(field, player)
    grid1 = Grid(field)
    Main(grid1, player)
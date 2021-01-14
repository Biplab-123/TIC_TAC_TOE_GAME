#required libaries
import pygame
import sys
import numpy as np

pygame.init()

#constant like color and height and width
WIDTH=600
HEIGHT=600
RED=(255,0,0)
BLACK=(0,0,0)
BG_COLOR=(28,170,156)
LINE_COLOR=(23,145,135)
LINE_WIDTH=15
BOARD_ROW=3
BOARD_COL=3
CIRCLE_RADIUS=60
CIRCLE_WIDTH=15
CROSS_WIDTH=25
SPACE=55
CROSS_COLOR=(0,255,0)
CIRCLE_COLOR=(0,0,255)


##pygame screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOR)

#Board
board=np.zeros((BOARD_ROW,BOARD_COL))



##make 9 boxes by draw line (argument need to pass (screen,line color,starting position,ending position,width))
def draw_lines():
    #1 horizontal line
    pygame.draw.line(screen,LINE_COLOR,(0,200),(600,200),LINE_WIDTH)
    
    #2nd Horizontal line
    pygame.draw.line(screen,LINE_COLOR,(0,400),(600,400),LINE_WIDTH)

    #1st vertical line
    pygame.draw.line(screen,LINE_COLOR,(200,0),(200,600),LINE_WIDTH)
    
    #2nd vertical line
    pygame.draw.line(screen,LINE_COLOR,(400,0),(400,600),LINE_WIDTH)



##draw figures circle and cross
def draw_figures():
    for row in range(BOARD_ROW):
        for col in range(BOARD_COL):
            if(board[row][col]==1): #when 1st player click it becomes a circle
                pygame.draw.circle(screen,RED,(int(col*200+ 200/2),int(row*200 + 200/2)),CIRCLE_RADIUS,CIRCLE_WIDTH)
                
            elif(board[row][col]==2):#when 2nd player click it becomes a cross
                pygame.draw.line(screen,BLACK,(col*200+SPACE,row*200+200-SPACE),(col*200+200-SPACE,row*200+SPACE),CROSS_WIDTH) #need to take two line to make a cross
                pygame.draw.line(screen,BLACK,(col*200+SPACE,row*200+SPACE),(col*200+200-SPACE,row*200+200-SPACE),CROSS_WIDTH)






##marking  square by the player
def mark_square(row,col,player):
    board[row][col]=player




##available_square(How many position left)
def available_square(row,col):
    if(board[row][col]==0):
        return True
    else:
        return False



##board Full(No space left)
def is_board_full():
    for row in range(BOARD_ROW):
        for col in range(BOARD_COL):
            if board[row][col]==0:
                return False   ##return false as the board is not yet fill
    return True







##win lose or draw
def check_win(player):

    #vertical winner
    for col in range(BOARD_COL):
        if(board[0][col]==player and board[1][col]==player and board[2][col]==player):
            draw_vertical_winning_line(col,player)
            return True #to break the function

    ##Horizontal Winner
    for row in range(BOARD_ROW):
        if(board[row][0]==player and board[row][1]==player and board[row][2]==player):
            draw_horizontal_winning_line(row,player)
            return True

    ##ascending diagonal
    if(board[2][0]==player and board[1][1]==player and board[0][2]==player):
        draw_asc_digonal(player)
        return True

    ##descending digonal
    if(board[0][0]==player and board[1][1]==player and board[2][2]==player):
        draw_desc_digonal(player)
        return True
    
    return False  ##if  nothing return means its a tie
        





##draw a straight line when 3 figures match in a sequence
def draw_vertical_winning_line(col,player):
    posx=col*200 + 100
    if(player==1):
        color=CIRCLE_COLOR
    elif(player==2):
        color=CROSS_COLOR
    pygame.draw.line(screen,color,(posx,15),(posx,HEIGHT-15),15) ##argument are (screen, color, starting position,ending position,width)


    
def draw_horizontal_winning_line(row,player):
    posy=row*200 + 100
    if(player==1):
        color=CIRCLE_COLOR
    elif(player==2):
        color=CROSS_COLOR
    pygame.draw.line(screen,color,(15,posy),(WIDTH-15,posy),15)


def draw_asc_digonal(player):
    if(player==1):
        color=CIRCLE_COLOR
    elif(player==2):
        color=CROSS_COLOR
    pygame.draw.line(screen,color,(15,HEIGHT-15),(WIDTH-15,15),15)

    
def draw_desc_digonal(player):
    if(player==1):
        color=CIRCLE_COLOR
    elif(player==2):
        color=CROSS_COLOR
    pygame.draw.line(screen,color,(15,15),(WIDTH-15,HEIGHT-15),15)

#restart the game    
def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    player=1
    for row in range(BOARD_ROW):
        for col in range(BOARD_COL):
                board[row][col]=0

draw_lines() #call the function   

player=1
game_over=False
#main loop
while True:
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            sys.exit()

        if (event.type==pygame.MOUSEBUTTONDOWN and not game_over): #checking that we click the screen or not
            mouseX=event.pos[0] #x
            mouseY=event.pos[1] #y

            clicked_row=int(mouseY // 200) #click each time different block
            clicked_col=int(mouseX // 200)

            if(available_square(clicked_row,clicked_col)):
                if(player==1):
                    mark_square(clicked_row,clicked_col,1)
                    if(check_win(player)):
                        game_over=True
                    player=2
                
                elif(player==2):
                    mark_square(clicked_row,clicked_col,2)
                    if(check_win(player)):
                        game_over=True
                    player=1
                    
                draw_figures()
        if(event.type==pygame.KEYDOWN):
            if(event.key==pygame.K_r):
                restart()
                player=1
                game_over=False
                
    pygame.display.update() ##to update the screen change everytime














































































    

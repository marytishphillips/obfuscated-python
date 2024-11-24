import numpy as np #line:1
import pygame #line:2
import sys #line:3
import math #line:4
BLUE =(0 ,0 ,255 )#line:6
BLACK =(0 ,0 ,0 )#line:7
RED =(255 ,0 ,0 )#line:8
YELLOW =(255 ,255 ,0 )#line:9
ROW_COUNT =6 #line:11
COLUMN_COUNT =7 #line:12
def create_board ():#line:15
    O0OO00O000O00O00O =np .zeros ((ROW_COUNT ,COLUMN_COUNT ))#line:16
    return O0OO00O000O00O00O #line:17
def drop_piece (O00OOOO0OO0OO0OOO ,OO0O00O0OOO00OOO0 ,O00OO0OOO0OOO00O0 ,O0O00O0O0O0O0OO0O ):#line:20
    O00OOOO0OO0OO0OOO [OO0O00O0OOO00OOO0 ][O00OO0OOO0OOO00O0 ]=O0O00O0O0O0O0OO0O #line:21
def is_valid_location (OOOOOOO0OO0O00000 ,OO0OOOOOOO000O0O0 ):#line:24
    return OOOOOOO0OO0O00000 [ROW_COUNT -1 ][OO0OOOOOOO000O0O0 ]==0 #line:25
def get_next_open_row (OOOO0O0OOOOOO0OOO ,O000O00OO0O0OOO00 ):#line:28
    for O0OO0OO0OOOO00000 in range (ROW_COUNT ):#line:29
        if OOOO0O0OOOOOO0OOO [O0OO0OO0OOOO00000 ][O000O00OO0O0OOO00 ]==0 :#line:30
            return O0OO0OO0OOOO00000 #line:31
def print_board (OO0O0000O0OO0O0OO ):#line:34
    print (np .flip (OO0O0000O0OO0O0OO ,0 ))#line:35
def winning_move (O000O0O000OOOOO00 ,OOO00O00O0OOO00O0 ):#line:38
    for OO0OO00OOO00O00OO in range (COLUMN_COUNT -3 ):#line:40
        for O0O00OO0OOOOO0000 in range (ROW_COUNT ):#line:41
            if O000O0O000OOOOO00 [O0O00OO0OOOOO0000 ][OO0OO00OOO00O00OO ]==OOO00O00O0OOO00O0 and O000O0O000OOOOO00 [O0O00OO0OOOOO0000 ][OO0OO00OOO00O00OO +1 ]==OOO00O00O0OOO00O0 and O000O0O000OOOOO00 [O0O00OO0OOOOO0000 ][OO0OO00OOO00O00OO +2 ]==OOO00O00O0OOO00O0 and O000O0O000OOOOO00 [O0O00OO0OOOOO0000 ][OO0OO00OOO00O00OO +3 ]==OOO00O00O0OOO00O0 :#line:42
                return True #line:43
    for OO0OO00OOO00O00OO in range (COLUMN_COUNT ):#line:45
        for O0O00OO0OOOOO0000 in range (ROW_COUNT -3 ):#line:46
            if O000O0O000OOOOO00 [O0O00OO0OOOOO0000 ][OO0OO00OOO00O00OO ]==OOO00O00O0OOO00O0 and O000O0O000OOOOO00 [O0O00OO0OOOOO0000 +1 ][OO0OO00OOO00O00OO ]==OOO00O00O0OOO00O0 and O000O0O000OOOOO00 [O0O00OO0OOOOO0000 +2 ][OO0OO00OOO00O00OO ]==OOO00O00O0OOO00O0 and O000O0O000OOOOO00 [O0O00OO0OOOOO0000 +3 ][OO0OO00OOO00O00OO ]==OOO00O00O0OOO00O0 :#line:47
                return True #line:48
    for OO0OO00OOO00O00OO in range (COLUMN_COUNT -3 ):#line:51
        for O0O00OO0OOOOO0000 in range (ROW_COUNT -3 ):#line:52
            if O000O0O000OOOOO00 [O0O00OO0OOOOO0000 ][OO0OO00OOO00O00OO ]==OOO00O00O0OOO00O0 and O000O0O000OOOOO00 [O0O00OO0OOOOO0000 +1 ][OO0OO00OOO00O00OO +1 ]==OOO00O00O0OOO00O0 and O000O0O000OOOOO00 [O0O00OO0OOOOO0000 +2 ][OO0OO00OOO00O00OO +2 ]==OOO00O00O0OOO00O0 and O000O0O000OOOOO00 [O0O00OO0OOOOO0000 +3 ][OO0OO00OOO00O00OO +3 ]==OOO00O00O0OOO00O0 :#line:53
                return True #line:54
    for OO0OO00OOO00O00OO in range (COLUMN_COUNT -3 ):#line:57
        for O0O00OO0OOOOO0000 in range (3 ,ROW_COUNT ):#line:58
            if O000O0O000OOOOO00 [O0O00OO0OOOOO0000 ][OO0OO00OOO00O00OO ]==OOO00O00O0OOO00O0 and O000O0O000OOOOO00 [O0O00OO0OOOOO0000 -1 ][OO0OO00OOO00O00OO +1 ]==OOO00O00O0OOO00O0 and O000O0O000OOOOO00 [O0O00OO0OOOOO0000 -2 ][OO0OO00OOO00O00OO +2 ]==OOO00O00O0OOO00O0 and O000O0O000OOOOO00 [O0O00OO0OOOOO0000 -3 ][OO0OO00OOO00O00OO +3 ]==OOO00O00O0OOO00O0 :#line:59
                return True #line:60
def draw_board (O0OOOOO0OO0O00O00 ):#line:63
    for OO00000OO00OO00OO in range (COLUMN_COUNT ):#line:64
        for O00O0O0000OO0OO00 in range (ROW_COUNT ):#line:65
            pygame .draw .rect (screen ,BLUE ,(OO00000OO00OO00OO *SQUARESIZE ,O00O0O0000OO0OO00 *SQUARESIZE +SQUARESIZE ,SQUARESIZE ,SQUARESIZE ))#line:67
            pygame .draw .circle (screen ,BLACK ,(int (OO00000OO00OO00OO *SQUARESIZE +SQUARESIZE /2 ),int (O00O0O0000OO0OO00 *SQUARESIZE +SQUARESIZE +SQUARESIZE /2 )),RADIUS )#line:69
    for OO00000OO00OO00OO in range (COLUMN_COUNT ):#line:71
        for O00O0O0000OO0OO00 in range (ROW_COUNT ):#line:72
            if O0OOOOO0OO0O00O00 [O00O0O0000OO0OO00 ][OO00000OO00OO00OO ]==1 :#line:73
                pygame .draw .circle (screen ,RED ,(int (OO00000OO00OO00OO *SQUARESIZE +SQUARESIZE /2 ),height -int (O00O0O0000OO0OO00 *SQUARESIZE +SQUARESIZE /2 )),RADIUS )#line:75
            elif O0OOOOO0OO0O00O00 [O00O0O0000OO0OO00 ][OO00000OO00OO00OO ]==2 :#line:77
                pygame .draw .circle (screen ,YELLOW ,(int (OO00000OO00OO00OO *SQUARESIZE +SQUARESIZE /2 ),height -int (O00O0O0000OO0OO00 *SQUARESIZE +SQUARESIZE /2 )),RADIUS )#line:79
    pygame .display .update ()#line:81
board =create_board ()#line:84
print_board (board )#line:85
game_over =False #line:86
turn =0 #line:87
pygame .init ()#line:89
SQUARESIZE =100 #line:91
width =COLUMN_COUNT *SQUARESIZE #line:93
height =(ROW_COUNT +1 )*SQUARESIZE #line:94
size =(width ,height )#line:96
RADIUS =int (SQUARESIZE /2 -5 )#line:98
pygame .display .set_caption ("CONNECT FOUR GAME")#line:100
screen =pygame .display .set_mode (size )#line:101
draw_board (board )#line:102
pygame .display .update ()#line:103
myfont =pygame .font .SysFont ("monosoace",75 )#line:105
while not game_over :#line:107
    for event in pygame .event .get ():#line:108
        if event .type ==pygame .QUIT :#line:109
            sys .exit ()#line:110
        if event .type ==pygame .MOUSEMOTION :#line:112
            pygame .draw .rect (screen ,BLACK ,(0 ,0 ,width ,SQUARESIZE ))#line:113
            posx =event .pos [0 ]#line:114
            if turn ==0 :#line:115
                pygame .draw .circle (screen ,RED ,(posx ,int (SQUARESIZE /2 )),RADIUS )#line:117
            else :#line:118
                pygame .draw .circle (screen ,YELLOW ,(posx ,int (SQUARESIZE /2 )),RADIUS )#line:120
        pygame .display .update ()#line:121
        if event .type ==pygame .MOUSEBUTTONDOWN :#line:123
            pygame .draw .rect (screen ,BLACK ,(0 ,0 ,width ,SQUARESIZE ))#line:125
            if turn ==0 :#line:127
                posx =event .pos [0 ]#line:128
                col =int (math .floor (posx /SQUARESIZE ))#line:129
                if is_valid_location (board ,col ):#line:131
                    row =get_next_open_row (board ,col )#line:132
                    drop_piece (board ,row ,col ,1 )#line:133
                    if winning_move (board ,1 ):#line:135
                        label =myfont .render ("Player 1 wins!!",1 ,RED )#line:137
                        screen .blit (label ,(40 ,10 ))#line:138
                        game_over =True #line:139
            else :#line:141
                posx =event .pos [0 ]#line:142
                col =int (math .floor (posx /SQUARESIZE ))#line:143
                if is_valid_location (board ,col ):#line:145
                    row =get_next_open_row (board ,col )#line:146
                    drop_piece (board ,row ,col ,2 )#line:147
                    if winning_move (board ,2 ):#line:149
                        label =myfont .render ("Player 2 wins!!",1 ,YELLOW )#line:151
                        screen .blit (label ,(40 ,10 ))#line:152
                        game_over =True #line:153
            print_board (board )#line:155
            draw_board (board )#line:156
            turn +=1 #line:158
            turn =turn %2 #line:159
            if game_over :#line:161
                pygame .time .wait (3000 )#line:162

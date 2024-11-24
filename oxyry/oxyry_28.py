from random import choice #line:1
from turtle import *#line:2
from freegames import floor ,vector #line:4
state ={'score':0 }#line:6
path =Turtle (visible =False )#line:7
writer =Turtle (visible =False )#line:8
aim =vector (5 ,0 )#line:9
pacman =vector (-40 ,-80 )#line:10
ghosts =[[vector (-180 ,160 ),vector (5 ,0 )],[vector (-180 ,-160 ),vector (0 ,5 )],[vector (100 ,160 ),vector (0 ,-5 )],[vector (100 ,-160 ),vector (-5 ,0 )],]#line:16
tiles =[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,0 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,0 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,]#line:39
def square (OO000O0O0000000OO ,OO00O00O0O0000O0O ):#line:43
    ""#line:44
    path .up ()#line:45
    path .goto (OO000O0O0000000OO ,OO00O00O0O0000O0O )#line:46
    path .down ()#line:47
    path .begin_fill ()#line:48
    for O00OOO0O0O00OOOO0 in range (4 ):#line:50
        path .forward (20 )#line:51
        path .left (90 )#line:52
    path .end_fill ()#line:54
def offset (O00OOO0O000O0OO0O ):#line:57
    ""#line:58
    OOO0O0OOO0O00000O =(floor (O00OOO0O000O0OO0O .x ,20 )+200 )/20 #line:59
    O0OOOOO0O00OOO0O0 =(180 -floor (O00OOO0O000O0OO0O .y ,20 ))/20 #line:60
    OO0O000O0O00O0O00 =int (OOO0O0OOO0O00000O +O0OOOOO0O00OOO0O0 *20 )#line:61
    return OO0O000O0O00O0O00 #line:62
def valid (OO0O0OOOOOO000OO0 ):#line:65
    ""#line:66
    OOO00O0000OOO0OOO =offset (OO0O0OOOOOO000OO0 )#line:67
    if tiles [OOO00O0000OOO0OOO ]==0 :#line:69
        return False #line:70
    OOO00O0000OOO0OOO =offset (OO0O0OOOOOO000OO0 +19 )#line:72
    if tiles [OOO00O0000OOO0OOO ]==0 :#line:74
        return False #line:75
    return OO0O0OOOOOO000OO0 .x %20 ==0 or OO0O0OOOOOO000OO0 .y %20 ==0 #line:77
def world ():#line:80
    ""#line:81
    bgcolor ('black')#line:82
    path .color ('blue')#line:83
    for OO00OO0OOOO0O00OO in range (len (tiles )):#line:85
        OO00OOOO00O0OOOOO =tiles [OO00OO0OOOO0O00OO ]#line:86
        if OO00OOOO00O0OOOOO >0 :#line:88
            O0O00000000000OOO =(OO00OO0OOOO0O00OO %20 )*20 -200 #line:89
            O0O0OO0O000O0OOOO =180 -(OO00OO0OOOO0O00OO //20 )*20 #line:90
            square (O0O00000000000OOO ,O0O0OO0O000O0OOOO )#line:91
            if OO00OOOO00O0OOOOO ==1 :#line:93
                path .up ()#line:94
                path .goto (O0O00000000000OOO +10 ,O0O0OO0O000O0OOOO +10 )#line:95
                path .dot (2 ,'white')#line:96
def move ():#line:99
    ""#line:100
    writer .undo ()#line:101
    writer .write (state ['score'])#line:102
    clear ()#line:104
    if valid (pacman +aim ):#line:106
        pacman .move (aim )#line:107
    O0OOOOOO0OO0OOOOO =offset (pacman )#line:109
    if tiles [O0OOOOOO0OO0OOOOO ]==1 :#line:111
        tiles [O0OOOOOO0OO0OOOOO ]=2 #line:112
        state ['score']+=1 #line:113
        OOO00OOO00OOO0000 =(O0OOOOOO0OO0OOOOO %20 )*20 -200 #line:114
        O0OOO00OO00O0O0O0 =180 -(O0OOOOOO0OO0OOOOO //20 )*20 #line:115
        square (OOO00OOO00OOO0000 ,O0OOO00OO00O0O0O0 )#line:116
    up ()#line:118
    goto (pacman .x +10 ,pacman .y +10 )#line:119
    dot (20 ,'yellow')#line:120
    for O00OO0000O0OOOO0O ,OOO00O00O0OO0O0OO in ghosts :#line:122
        if valid (O00OO0000O0OOOO0O +OOO00O00O0OO0O0OO ):#line:123
            O00OO0000O0OOOO0O .move (OOO00O00O0OO0O0OO )#line:124
        else :#line:125
            OO0OOOO000O00000O =[vector (5 ,0 ),vector (-5 ,0 ),vector (0 ,5 ),vector (0 ,-5 ),]#line:131
            OOOO0O0O0OOO00000 =choice (OO0OOOO000O00000O )#line:132
            OOO00O00O0OO0O0OO .x =OOOO0O0O0OOO00000 .x #line:133
            OOO00O00O0OO0O0OO .y =OOOO0O0O0OOO00000 .y #line:134
        up ()#line:136
        goto (O00OO0000O0OOOO0O .x +10 ,O00OO0000O0OOOO0O .y +10 )#line:137
        dot (20 ,'red')#line:138
    update ()#line:140
    for O00OO0000O0OOOO0O ,OOO00O00O0OO0O0OO in ghosts :#line:142
        if abs (pacman -O00OO0000O0OOOO0O )<20 :#line:143
            return #line:144
    ontimer (move ,100 )#line:146
def change (OO0000O000OO00O0O ,OOO00OOO0000O0O00 ):#line:149
    ""#line:150
    if valid (pacman +vector (OO0000O000OO00O0O ,OOO00OOO0000O0O00 )):#line:151
        aim .x =OO0000O000OO00O0O #line:152
        aim .y =OOO00OOO0000O0O00 #line:153
setup (420 ,420 ,370 ,0 )#line:156
hideturtle ()#line:157
tracer (False )#line:158
writer .goto (160 ,160 )#line:159
writer .color ('white')#line:160
writer .write (state ['score'])#line:161
listen ()#line:162
onkey (lambda :change (5 ,0 ),'Right')#line:163
onkey (lambda :change (-5 ,0 ),'Left')#line:164
onkey (lambda :change (0 ,5 ),'Up')#line:165
onkey (lambda :change (0 ,-5 ),'Down')#line:166
world ()#line:167
move ()#line:168
done ()
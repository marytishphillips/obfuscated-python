import random #line:1
import sys #line:2
board =[O0O000OO0OOO00O00 for O0O000OO0OOO00O00 in range (0 ,9 )]#line:3
player ,computer ='',''#line:4
moves =((1 ,7 ,3 ,9 ),(5 ,),(2 ,4 ,6 ,8 ))#line:6
winners =((0 ,1 ,2 ),(3 ,4 ,5 ),(6 ,7 ,8 ),(0 ,3 ,6 ),(1 ,4 ,7 ),(2 ,5 ,8 ),(0 ,4 ,8 ),(2 ,4 ,6 ))#line:8
tab =range (1 ,10 )#line:10
def print_board ():#line:11
    OO0OO00O00OOOO00O =1 #line:12
    for OOOO0OOO0O0OO0OOO in board :#line:13
        OO0O0OOOO00O0OO00 =' | '#line:14
        if OO0OO00O00OOOO00O %3 ==0 :#line:15
            OO0O0OOOO00O0OO00 =' \n'#line:16
            if OOOO0OOO0O0OO0OOO !=1 :OO0O0OOOO00O0OO00 +='---------\n'#line:17
        O0OO00OO0O0000O0O =' '#line:18
        if OOOO0OOO0O0OO0OOO in ('X','O'):O0OO00OO0O0000O0O =OOOO0OOO0O0OO0OOO #line:19
        OO0OO00O00OOOO00O +=1 #line:20
        print (O0OO00OO0O0000O0O ,end =OO0O0OOOO00O0OO00 )#line:21
def select_char ():#line:22
    OOO0000OOO0OOO0OO =('X','O')#line:23
    if random .randint (0 ,1 )==0 :#line:24
        return OOO0000OOO0OOO0OO [::-1 ]#line:25
    return OOO0000OOO0OOO0OO #line:26
def can_move (OO0O0O00OO0O0OOO0 ,OOO0OOOO00O00OO00 ,OOO00000OO0000O0O ):#line:27
    if OOO00000OO0000O0O in tab and OO0O0O00OO0O0OOO0 [OOO00000OO0000O0O -1 ]==OOO00000OO0000O0O -1 :#line:28
        return True #line:29
    return False #line:30
def can_win (O00OO0OO0OO00000O ,OOOOOOO00OOO000O0 ,O0OOOO0O0000OOO0O ):#line:31
    OOO000O00OOO00O0O =[]#line:32
    OO0O0O0OO0OOOOO0O =0 #line:33
    for OOO0O0000OOOO00O0 in O00OO0OO0OO00000O :#line:34
        if OOO0O0000OOOO00O0 ==OOOOOOO00OOO000O0 :OOO000O00OOO00O0O .append (OO0O0O0OO0OOOOO0O )#line:35
        OO0O0O0OO0OOOOO0O +=1 #line:36
    OO0O000OO00O0OOO0 =True #line:37
    for O0OOO0O0OOO0O0000 in winners :#line:38
        OO0O000OO00O0OOO0 =True #line:39
        for O0O00OO00OOO000OO in O0OOO0O0OOO0O0000 :#line:40
            if O00OO0OO0OO00000O [O0O00OO00OOO000OO ]!=OOOOOOO00OOO000O0 :#line:41
                OO0O000OO00O0OOO0 =False #line:42
                break #line:43
        if OO0O000OO00O0OOO0 ==True :#line:44
            break #line:45
    return OO0O000OO00O0OOO0 #line:46
def make_move (OOOOO0O000O0O0O00 ,O0OO00O00O00OOOOO ,O00000OO0OOO00O0O ,undo =False ):#line:47
    if can_move (OOOOO0O000O0O0O00 ,O0OO00O00O00OOOOO ,O00000OO0OOO00O0O ):#line:48
        OOOOO0O000O0O0O00 [O00000OO0OOO00O0O -1 ]=O0OO00O00O00OOOOO #line:49
        OO0OOOOOOO0OOO0O0 =can_win (OOOOO0O000O0O0O00 ,O0OO00O00O00OOOOO ,O00000OO0OOO00O0O )#line:50
        if undo :#line:51
            OOOOO0O000O0O0O00 [O00000OO0OOO00O0O -1 ]=O00000OO0OOO00O0O -1 #line:52
        return (True ,OO0OOOOOOO0OOO0O0 )#line:53
    return (False ,False )#line:54
def computer_move ():#line:56
    O0O000OOO0OOO0OOO =-1 #line:57
    for OOOO0OOO00000OOOO in range (1 ,10 ):#line:59
        if make_move (board ,computer ,OOOO0OOO00000OOOO ,True )[1 ]:#line:60
            O0O000OOO0OOO0OOO =OOOO0OOO00000OOOO #line:61
            break #line:62
    if O0O000OOO0OOO0OOO ==-1 :#line:63
        for OOOO0OOO00000OOOO in range (1 ,10 ):#line:65
            if make_move (board ,player ,OOOO0OOO00000OOOO ,True )[1 ]:#line:66
                O0O000OOO0OOO0OOO =OOOO0OOO00000OOOO #line:67
                break #line:68
    if O0O000OOO0OOO0OOO ==-1 :#line:69
        for O0O0O0OOOO0OOOOO0 in moves :#line:71
            for O0O00OOOO0OOO00OO in O0O0O0OOOO0OOOOO0 :#line:72
                if O0O000OOO0OOO0OOO ==-1 and can_move (board ,computer ,O0O00OOOO0OOO00OO ):#line:73
                    O0O000OOO0OOO0OOO =O0O00OOOO0OOO00OO #line:74
                    break #line:75
    return make_move (board ,computer ,O0O000OOO0OOO0OOO )#line:76
def space_exist ():#line:77
    return board .count ('X')+board .count ('O')!=9 #line:78
player ,computer =select_char ()#line:79
print ('Player is [%s] and computer is [%s]'%(player ,computer ))#line:80
result ='%%% Deuce ! %%%'#line:81
while space_exist ():#line:82
    print_board ()#line:83
    print ('#Make your move ! [1-9] : ',end ='')#line:84
    move =int (input ())#line:85
    moved ,won =make_move (board ,player ,move )#line:86
    if not moved :#line:87
        print (' Invalid number ! Try again !')#line:88
        continue #line:89
    if won :#line:90
        result ='*** Congratulations ! You won ! ***'#line:91
        break #line:92
    elif computer_move ()[1 ]:#line:93
        result ='=== You lose ! =='#line:94
        break #line:95
print_board ()#line:96
print (result )
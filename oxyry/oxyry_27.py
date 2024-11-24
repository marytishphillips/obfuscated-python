import random #line:1
class Player :#line:3
    def __init__ (O00OOO0OOO000O00O ,O0OOO0O00OO00000O ,OOOO00O000OO0OO0O ,O0OOOOOOOO0OOOO00 ):#line:4
        O00OOO0OOO000O00O .name =O0OOO0O00OO00000O #line:5
        O00OOO0OOO000O00O .age =OOOO00O000OO0OO0O #line:6
        O00OOO0OOO000O00O .cards =[]#line:7
        O00OOO0OOO000O00O .score =0 #line:8
        O00OOO0OOO000O00O .money =1000 #line:9
        O00OOO0OOO000O00O .bet =0 #line:10
        O00OOO0OOO000O00O .playerType =O0OOOOOOOO0OOOO00 #line:11
        O00OOO0OOO000O00O .scoreDictionary ={'2':2 ,'3':3 ,'4':4 ,'5':5 ,'6':6 ,'7':7 ,'8':8 ,'9':9 ,'10':10 ,'J':10 ,'Q':10 ,'K':10 ,'A':11 }#line:26
    def placeBet (O000OOOOOO0OO0O0O ):#line:28
        while True :#line:29
            try :#line:30
                O0000OO0OOO0O000O =int (input ("Enter your bet amount: "))#line:31
                if O0000OO0OOO0O000O <min_bet or O0000OO0OOO0O000O >max_bet :#line:32
                    print ("Invalid bet amount. Please enter a bet between",min_bet ,"and",max_bet )#line:33
                elif O0000OO0OOO0O000O >O000OOOOOO0OO0O0O .money :#line:34
                    print ("You don't have enough money for that bet.")#line:35
                else :#line:36
                    O000OOOOOO0OO0O0O .bet =O0000OO0OOO0O000O #line:37
                    break #line:38
            except ValueError :#line:39
                print ("Invalid input. Please enter a valid number.")#line:40
    def playRound (O0OO00O0OOOOO0O00 ):#line:42
        if O0OO00O0OOOOO0O00 .playerType =='human':#line:43
            while O0OO00O0OOOOO0O00 .score <21 :#line:44
                O0OOO000OOOO00OO0 =input ("Do you want to draw extra card? Answer yes or no: ")#line:45
                if O0OOO000OOOO00OO0 .lower ()=='yes':#line:46
                    OO00O00OO000OOO0O =O0OO00O0OOOOO0O00 .drawCard ()#line:47
                    O0OO00O0OOOOO0O00 .drawCards (OO00O00OO000OOO0O )#line:48
                    print (O0OO00O0OOOOO0O00 .cards )#line:49
                    O0OO00O0OOOOO0O00 .getScore ()#line:50
                else :#line:51
                    break #line:52
    def drawCards (O0O0O00OOO0000O00 ,O00O000OO0OO00OO0 ):#line:54
        O0O0O00OOO0000O00 .cards .append (O00O000OO0OO00OO0 )#line:55
    def getScore (OO0OO00O000OOOO00 ):#line:57
        OO0OO00O000OOOO00 .score =0 #line:58
        for O0OOO0O0000OO00OO in OO0OO00O000OOOO00 .cards :#line:59
            OO0OO00O000OOOO00 .score +=OO0OO00O000OOOO00 .scoreDictionary [O0OOO0O0000OO00OO ]#line:60
        OO0OO00O000OOOO00 .adjustAceValue ()#line:61
        return OO0OO00O000OOOO00 .score #line:62
    def adjustAceValue (OOOOOO0O0O0OO0000 ):#line:64
        while OOOOOO0O0O0OO0000 .score >21 and 'A'in OOOOOO0O0O0OO0000 .cards :#line:65
            OOOOOO0O0O0OO0000 .score -=10 #line:66
class GameBlackJack :#line:68
    def __init__ (OOO00OOOO00OOOO0O ,O000OO0OOO0O0O0OO ,O0000O0OO0000OO00 ):#line:69
        OOO00OOOO00OOOO0O .playerlist =O0000O0OO0000OO00 #line:70
        OOO00OOOO00OOOO0O .dealer =O000OO0OOO0O0O0OO #line:71
        OOO00OOOO00OOOO0O .cardDeck =[]#line:72
        OOO00OOOO00OOOO0O .genDeck ()#line:73
    def startRound (OO00O00OO00O0O00O ):#line:75
        for OO0OOOO0OOO0O0OOO in OO00O00OO00O0O00O .playerlist :#line:76
            OO0OOOO0OOO0O0OOO .placeBet ()#line:77
    def drawCardsRound1 (OOOO0000000OOO00O ):#line:79
        for OO000OO00OO00O000 in range (2 ):#line:80
            for O0OOO0OO0O0OO0OOO in OOOO0000000OOO00O .playerlist :#line:81
                OOOOO0OOO0O0OOO0O =OOOO0000000OOO00O .drawCard ()#line:82
                O0OOO0OO0O0OO0OOO .drawCards (OOOOO0OOO0O0OOO0O )#line:83
            OOOOO0OOO0O0OOO0O =OOOO0000000OOO00O .drawCard ()#line:85
            OOOO0000000OOO00O .dealer .drawCards (OOOOO0OOO0O0OOO0O )#line:86
        for O0OOO0OO0O0OO0OOO in OOOO0000000OOO00O .playerlist :#line:88
            if O0OOO0OO0O0OO0OOO .playerType =='human':#line:89
                print (O0OOO0OO0O0OO0OOO .cards )#line:90
    def drawCard (O0O0000O00O00OO00 ):#line:92
        OOO00O0000000000O =random .randint (0 ,len (O0O0000O00O00OO00 .cardDeck )-1 )#line:93
        OO0O0000O00OO00OO =O0O0000O00O00OO00 .cardDeck .pop (OOO00O0000000000O )#line:94
        return OO0O0000O00OO00OO #line:95
    def drawCardsRound2 (OOOO0O0OOOOO0OO00 ):#line:97
        for OO0O000O000OOO0O0 in OOOO0O0OOOOO0OO00 .playerlist :#line:98
            if OO0O000O000OOO0O0 .playerType =='AI':#line:99
                while OO0O000O000OOO0O0 .getScore ()<14 :#line:100
                    O00OO0OO0000OO0O0 =OOOO0O0OOOOO0OO00 .drawCard ()#line:101
                    OO0O000O000OOO0O0 .drawCards (O00OO0OO0000OO0O0 )#line:102
            elif OO0O000O000OOO0O0 .playerType =='human':#line:103
                O00O0O0O0O0O0O0OO ='yes'#line:104
                while O00O0O0O0O0O0O0OO =='yes':#line:105
                    O00O0O0O0O0O0O0OO =input ("Do you want to draw extra card? Answer yes or no: ")#line:106
                    if O00O0O0O0O0O0O0OO =='yes':#line:107
                        O00OO0OO0000OO0O0 =OOOO0O0OOOOO0OO00 .drawCard ()#line:108
                        OO0O000O000OOO0O0 .drawCards (O00OO0OO0000OO0O0 )#line:109
                        print (OO0O000O000OOO0O0 .cards )#line:110
    def playRound3 (O0OOO00OOO0O000O0 ):#line:112
        while O0OOO00OOO0O000O0 .dealer .getScore ()<14 :#line:113
            O0OO0OO00OO0O0000 =O0OOO00OOO0O000O0 .drawCard ()#line:114
            O0OOO00OOO0O000O0 .dealer .drawCards (O0OO0OO00OO0O0000 )#line:115
        print ("dealer.cards: "+str (O0OOO00OOO0O000O0 .dealer .cards ))#line:117
        for O0OO0O0O0OOOO0000 in O0OOO00OOO0O000O0 .playerlist :#line:119
            if (O0OOO00OOO0O000O0 .dealer .getScore ()<=21 )and (O0OO0O0O0OOOO0000 .getScore ()<=21 ):#line:120
                if O0OOO00OOO0O000O0 .dealer .getScore ()>O0OO0O0O0OOOO0000 .getScore ():#line:121
                    O0OOO00OOO0O000O0 .dealer .money +=O0OO0O0O0OOOO0000 .bet #line:122
                    O0OO0O0O0OOOO0000 .money -=O0OO0O0O0OOOO0000 .bet #line:123
                    print ('dealer wins '+O0OO0O0O0OOOO0000 .name )#line:124
                elif O0OOO00OOO0O000O0 .dealer .getScore ()<O0OO0O0O0OOOO0000 .getScore ():#line:125
                    O0OOO00OOO0O000O0 .dealer .money -=O0OO0O0O0OOOO0000 .bet #line:126
                    O0OO0O0O0OOOO0000 .money +=O0OO0O0O0OOOO0000 .bet #line:127
                    print ('dealer loses '+O0OO0O0O0OOOO0000 .name )#line:128
                else :#line:129
                    print ('dealer draw '+O0OO0O0O0OOOO0000 .name )#line:130
            elif (O0OOO00OOO0O000O0 .dealer .getScore ()<=21 )and (O0OO0O0O0OOOO0000 .getScore ()>21 ):#line:132
                print ('dealer wins '+O0OO0O0O0OOOO0000 .name )#line:133
            elif (O0OOO00OOO0O000O0 .dealer .getScore ()>21 )and (O0OO0O0O0OOOO0000 .getScore ()<=21 ):#line:135
                print ('dealer loses '+O0OO0O0O0OOOO0000 .name )#line:136
                O0OOO00OOO0O000O0 .dealer .money -=O0OO0O0O0OOOO0000 .bet #line:137
                O0OO0O0O0OOOO0000 .money +=O0OO0O0O0OOOO0000 .bet #line:138
            elif (O0OOO00OOO0O000O0 .dealer .getScore ()>21 )and (O0OO0O0O0OOOO0000 .getScore ()>21 ):#line:140
                print ('dealer wins '+O0OO0O0O0OOOO0000 .name )#line:141
                O0OO0O0O0OOOO0000 .money +=O0OO0O0O0OOOO0000 .bet #line:142
                print ('dealer loses '+O0OO0O0O0OOOO0000 .name )#line:143
            if O0OO0O0O0OOOO0000 .playerType =="human":#line:145
                print ("My Money: "+str (O0OO0O0O0OOOO0000 .money ))#line:146
    def removeLossers (O000OO0O0OO0O0O00 ):#line:148
        O000OO0O0OO0O0O00 .playerlist =[OOO0O0OOOOO00O000 for OOO0O0OOOOO00O000 in O000OO0O0OO0O0O00 .playerlist if OOO0O0OOOOO00O000 .money >0 ]#line:149
    def refreshPlayerCard (O00O00O00000OOOO0 ):#line:151
        for OOOOO0O00000OOO0O in O00O00O00000OOOO0 .playerlist :#line:152
            OOOOO0O00000OOO0O .cards =[]#line:153
        O00O00O00000OOOO0 .dealer .cards =[]#line:154
    def genDeck (O00O0O00O0OO0OO00 ):#line:156
        OO000O0O0OO0OO00O =['2','3','4','5','6','7','8','9','10','J','Q','K','A']#line:157
        O00O0O00O0OO0OO00 .cardDeck =[O0O0O0OO0OO000O0O for O0O0O0OO0OO000O0O in OO000O0O0OO0OO00O for _O0O00OO00OO000OOO in range (4 )]#line:158
        random .shuffle (O00O0O00O0OO0OO00 .cardDeck )#line:159
min_bet =5 #line:162
max_bet =100 #line:163
player1 =Player ('George',22 ,'human')#line:166
player2 =Player ('soon',21 ,'AI')#line:167
player3 =Player ('PAXI',28 ,'AI')#line:168
player4 =Player ('cactus',41 ,'AI')#line:169
dealer =Player ('Mc Donald',78 ,'AI')#line:171
playerlist =[player1 ,player2 ,player3 ,player4 ]#line:173
game1 =GameBlackJack (dealer ,playerlist )#line:175
gameRound =0 #line:177
while gameRound <2 :#line:179
    print ("Round "+str (gameRound +1 ))#line:180
    game1 .startRound ()#line:181
    game1 .genDeck ()#line:182
    game1 .refreshPlayerCard ()#line:183
    game1 .drawCardsRound1 ()#line:184
    game1 .drawCardsRound2 ()#line:185
    game1 .playRound3 ()#line:186
    game1 .removeLossers ()#line:187
    gameRound +=1 
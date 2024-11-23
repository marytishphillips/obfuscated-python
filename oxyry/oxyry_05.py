import random #line:1
choices =["rock","paper","scissors","lizard","spock"]#line:3
def get_user_choice ():#line:5
    O0000O0OOO0OO000O =input ("Enter your choice (rock, paper, scissors, lizard, spock): ").lower ()#line:6
    while O0000O0OOO0OO000O not in choices :#line:7
        O0000O0OOO0OO000O =input ("Invalid choice. Please enter rock, paper, scissors, lizard, or spock: ").lower ()#line:8
    return O0000O0OOO0OO000O #line:9
def get_computer_choice ():#line:12
    return random .choice (choices )#line:13
def determine_winner (O0O0O00O00O0OO0OO ,OOOO00O0O0O0OOO0O ):#line:16
    O0OO00O0O0OO00OOO ={"scissors":["paper","lizard"],"paper":["rock","spock"],"rock":["lizard","scissors"],"lizard":["spock","paper"],"spock":["scissors","rock"]}#line:23
    if O0O0O00O00O0OO0OO ==OOOO00O0O0O0OOO0O :#line:25
        return "tie"#line:26
    elif OOOO00O0O0O0OOO0O in O0OO00O0O0OO00OOO [O0O0O00O00O0OO0OO ]:#line:27
        return "user"#line:28
    else :#line:29
        return "computer"#line:30
def play_game ():#line:33
    print ("Welcome to Rock, Paper, Scissors, Lizard, Spock!")#line:34
    while True :#line:36
        while True :#line:37
            try :#line:38
                OOOO00OO00OOO00O0 =int (input ("Enter the number of rounds you want to play: "))#line:39
                if OOOO00OO00OOO00O0 <=0 :#line:40
                    print ("Please enter a positive number.")#line:41
                    continue #line:42
                break #line:43
            except ValueError :#line:44
                print ("Invalid input. Please enter a number.")#line:45
        OOOOO00O0OOO0OOOO =0 #line:47
        OOOO0O0OOOO000O0O =0 #line:48
        OOOOOO00OO000OOO0 =0 #line:49
        for OOO0O00OOO000OOO0 in range (1 ,OOOO00OO00OOO00O0 +1 ):#line:51
            print (f"\nRound {OOO0O00OOO000OOO0}/{OOOO00OO00OOO00O0}")#line:52
            OOOOOOO00O000O00O =get_user_choice ()#line:54
            O0O00O00OO00000O0 =get_computer_choice ()#line:55
            print (f"\nYou chose: {OOOOOOO00O000O00O}")#line:57
            print (f"Computer chose: {O0O00O00OO00000O0}")#line:58
            OOO0OO00O00O00OOO =determine_winner (OOOOOOO00O000O00O ,O0O00O00OO00000O0 )#line:60
            if OOO0OO00O00O00OOO =="tie":#line:62
                print ("It's a tie!")#line:63
                OOOOOO00OO000OOO0 +=1 #line:64
            elif OOO0OO00O00O00OOO =="user":#line:65
                print ("You win!")#line:66
                OOOOO00O0OOO0OOOO +=1 #line:67
            else :#line:68
                print ("Computer wins!")#line:69
                OOOO0O0OOOO000O0O +=1 #line:70
            print (f"\nScores:\nUser: {OOOOO00O0OOO0OOOO}\nComputer: {OOOO0O0OOOO000O0O}\nTies: {OOOOOO00OO000OOO0}")#line:72
        print ("\nFinal Scores:")#line:74
        print (f"User: {OOOOO00O0OOO0OOOO}")#line:75
        print (f"Computer: {OOOO0O0OOOO000O0O}")#line:76
        print (f"Ties: {OOOOOO00OO000OOO0}")#line:77
        while True :#line:79
            O0O0O0000O00O000O =input ("\nDo you want to play again? (y/n): ").lower ()#line:80
            if O0O0O0000O00O000O in ["y","n"]:#line:81
                break #line:82
            print ("Invalid input. Please enter 'y' or 'n'.")#line:83
        if O0O0O0000O00O000O !="y":#line:85
            print ("Thanks for playing!")#line:86
            break #line:87
if __name__ =="__main__":#line:89
    play_game ()
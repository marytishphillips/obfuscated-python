import math #line:1
def is_valid (OO0O00OOOO0OOO0O0 ,O000000O00OOOOOO0 ,O00OOOO0O00000000 ,O0OOO000O000000OO ,O0000000O00OOOOOO ):#line:4
    for O000O0O00OOOO0O0O in range (len (OO0O00OOOO0OOO0O0 )):#line:7
        if OO0O00OOOO0OOO0O0 [O000O0O00OOOO0O0O ][O00OOOO0O00000000 ]==O0OOO000O000000OO or OO0O00OOOO0OOO0O0 [O000000O00OOOOOO0 ][O000O0O00OOOO0O0O ]==O0OOO000O000000OO :#line:8
            return False #line:9
    O0O0O00O0OO0O00OO ,OOO00O00OO000O00O =O000000O00OOOOOO0 -O000000O00OOOOOO0 %O0000000O00OOOOOO ,O00OOOO0O00000000 -O00OOOO0O00000000 %O0000000O00OOOOOO #line:13
    for O000O0O00OOOO0O0O in range (O0000000O00OOOOOO ):#line:14
        for OOOOO0OO000O0OO0O in range (O0000000O00OOOOOO ):#line:15
            if OO0O00OOOO0OOO0O0 [O0O0O00O0OO0O00OO +O000O0O00OOOO0O0O ][OOO00O00OO000O00O +OOOOO0OO000O0OO0O ]==O0OOO000O000000OO :#line:16
                return False #line:17
    return True #line:19
def find_empty_cell (O00OO00OO000O00OO ):#line:22
    for O00O0000O00O0OOOO in range (len (O00OO00OO000O00OO )):#line:24
        for OO0O000000O0OOOO0 in range (len (O00OO00OO000O00OO )):#line:25
            if O00OO00OO000O00OO [O00O0000O00O0OOOO ][OO0O000000O0OOOO0 ]==0 :#line:26
                return O00O0000O00O0OOOO ,OO0O000000O0OOOO0 #line:27
    return None #line:28
def solve_kenken (OO00O00OOOO0OOOO0 ,O00OOO00OOOO0OOO0 ):#line:31
    OOO00OOOOO000OO0O =find_empty_cell (OO00O00OOOO0OOOO0 )#line:33
    if not OOO00OOOOO000OO0O :#line:34
        return True #line:36
    O0OO0OO0O0OO0O0OO ,O0000O00O00O0OOO0 =OOO00OOOOO000OO0O #line:38
    for OOOO00O0OO00O00O0 in range (1 ,len (OO00O00OOOO0OOOO0 )+1 ):#line:40
        if is_valid (OO00O00OOOO0OOOO0 ,O0OO0OO0O0OO0O0OO ,O0000O00O00O0OOO0 ,OOOO00O0OO00O00O0 ,O00OOO00OOOO0OOO0 ):#line:41
            OO00O00OOOO0OOOO0 [O0OO0OO0O0OO0O0OO ][O0000O00O00O0OOO0 ]=OOOO00O0OO00O00O0 #line:42
            if solve_kenken (OO00O00OOOO0OOOO0 ,O00OOO00OOOO0OOO0 ):#line:44
                return True #line:45
            OO00O00OOOO0OOOO0 [O0OO0OO0O0OO0O0OO ][O0000O00O00O0OOO0 ]=0 #line:47
    return False #line:49
def validate_puzzle_input (O000OO0OOO0O0O0O0 ,O0OO000O0O0OO00O0 ):#line:52
    if O000OO0OOO0O0O0O0 <=1 or int (O000OO0OOO0O0O0O0 **0.5 )**2 !=O000OO0OOO0O0O0O0 :#line:60
        print ("Invalid board size. The size should be greater than 1 and a perfect square.")#line:61
        return False #line:62
    if len (O0OO000O0O0OO00O0 )!=O000OO0OOO0O0O0O0 :#line:64
        print (f"Invalid number of groups. Expected {O000OO0OOO0O0O0O0} groups.")#line:65
        return False #line:66
    OOO000O0O00OO00OO ={'+','-','*','/'}#line:68
    for OOOOOO000O0000OOO ,OOOOO0O000O0000O0 in O0OO000O0O0OO00O0 :#line:69
        if OOOOOO000O0000OOO <=0 :#line:70
            print ("Invalid target number. The target number should be greater than 0 for each group.")#line:72
            return False #line:73
        if OOOOO0O000O0000O0 not in OOO000O0O00OO00OO :#line:74
            print ("Invalid operation. Valid operations are '+', '-', '*', or '/'.")#line:75
            return False #line:76
    return True #line:78
def get_puzzle_input ():#line:81
    O00OO000OOO00OOO0 =int (input ("Enter the size of the grid (e.g., 5 for a 5x5 puzzle): "))#line:83
    O0OO0O000OO0O0O00 =int (input ("Enter the size of each group (e.g., 3 for a standard 9x9 puzzle): "))#line:85
    O0000O000OOOO0OOO =[]#line:87
    for OOOOOO000OOO00000 in range (O00OO000OOO00OOO0 ):#line:88
        while True :#line:89
            try :#line:90
                O00OOO0OOOO0O0000 =int (input (f"Enter the target number for group {OOOOOO000OOO00000 + 1}: "))#line:92
                O0O000OOOOO0O000O =input (f"Enter the operation for group {OOOOOO000OOO00000 + 1} (+, -, *, /): ")#line:94
                O0000O000OOOO0OOO .append ((O00OOO0OOOO0O0000 ,O0O000OOOOO0O000O ))#line:95
                break #line:96
            except ValueError :#line:97
                print ("Invalid input. Please enter a valid target number and operation.")#line:98
    if validate_puzzle_input (O00OO000OOO00OOO0 ,O0000O000OOOO0OOO ):#line:100
        return O00OO000OOO00OOO0 ,O0OO0O000OO0O0O00 ,O0000O000OOOO0OOO #line:101
    else :#line:102
        print ("Invalid puzzle input. Please try again.")#line:103
        return None #line:104
def print_board (O0OO0000OOO00OO00 ):#line:107
    for OOO0O0O0OOO00000O in O0OO0000OOO00OO00 :#line:109
        print (" ".join (str (O0O0OOO0OOO00O000 )if O0O0OOO0OOO00O000 !=0 else "-"for O0O0OOO0OOO00O000 in OOO0O0O0OOO00000O ))#line:110
    print ()#line:111
def main ():#line:114
    print ("KenKen Puzzle Solver")#line:116
    O000OOOO000O00000 =get_puzzle_input ()#line:118
    if O000OOOO000O00000 :#line:119
        OOO0O0O0O0OO00O0O ,O0O00O0OO0O0OOOOO ,OOOOOO000OOOOO0O0 =O000OOOO000O00000 #line:120
        OOO00OO0000O0000O =[[0 for _O0OO0000OOO000OOO in range (OOO0O0O0O0OO00O0O )]for _OOO00O0O000OO0OO0 in range (OOO0O0O0O0OO00O0O )]#line:123
        if solve_kenken (OOO00OO0000O0000O ,O0O00O0OO0O0OOOOO ):#line:125
            print ("Solved KenKen Puzzle:")#line:126
            print_board (OOO00OO0000O0000O )#line:127
        else :#line:128
            print ("No solution exists.")#line:129
if __name__ =="__main__":#line:132
    main ()
class ChessBoard :#line:1
    def __init__ (OOO000O0O0OO0O000 ):#line:2
        OOO000O0O0OO0O000 .board =OOO000O0O0OO0O000 .create_board ()#line:3
        OOO000O0O0OO0O000 .turn ='white'#line:4
    def create_board (O00OO0000000OOO0O ):#line:6
        OO0OO0OO0OO0O0O0O =[['♜','♞','♝','♛','♚','♝','♞','♜'],['♟','♟','♟','♟','♟','♟','♟','♟'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['♙','♙','♙','♙','♙','♙','♙','♙'],['♖','♘','♗','♕','♔','♗','♘','♖']]#line:17
        return OO0OO0OO0OO0O0O0O #line:18
    def print_board (OO0O0OOO0O00OOOO0 ):#line:20
        print ('      Player 1')#line:22
        print ('  a b c d e f g h')#line:23
        for OOO00OO0O0OOOOO0O ,OOOOOO00OO000OOO0 in enumerate (OO0O0OOO0O00OOOO0 .board ):#line:26
            print (f'{8 - OOO00OO0O0OOOOO0O} ',end ='')#line:28
            for OO0OO0O0OOOO00OO0 in OOOOOO00OO000OOO0 :#line:30
                print (OO0OO0O0OOOO00OO0 ,end =' ')#line:31
            print (f'{8 - OOO00OO0O0OOOOO0O}')#line:33
        print ('  a b c d e f g h')#line:36
        print ('      Player 2\n')#line:37
    def move_piece (O00O00O0O0OO00O00 ,O00O0OO00O00O0OOO ,O0OOOOO00O00O0O00 ):#line:39
        O0000O0OOOO00O0OO ,O0O0OOOOO00O0O0OO =O00O0OO00O00O0OOO #line:40
        OO00O00OO000OO00O ,O0OO0OO0OOO00OO0O =O0OOOOO00O00O0O00 #line:41
        OOOO00O0O0O0O000O =O00O00O0O0OO00O00 .board [O0000O0OOOO00O0OO ][O0O0OOOOO00O0O0OO ]#line:43
        O00O00O0O0OO00O00 .board [O0000O0OOOO00O0OO ][O0O0OOOOO00O0O0OO ]='.'#line:44
        O00O00O0O0OO00O00 .board [OO00O00OO000OO00O ][O0OO0OO0OOO00OO0O ]=OOOO00O0O0O0O000O #line:45
        O00O00O0O0OO00O00 .turn ='black'if O00O00O0O0OO00O00 .turn =='white'else 'white'#line:48
def parse_position (O0OO0OOO0OO0O0000 ):#line:50
    OO000O0O0O0000000 ,O00O00OO0OOOOO0OO =O0OO0OOO0OO0O0000 #line:51
    return 8 -int (O00O00OO0OOOOO0OO ),ord (OO000O0O0O0000000 )-ord ('a')#line:52
def main ():#line:54
    O0000000O00OO0O0O =ChessBoard ()#line:55
    O0000000O00OO0O0O .print_board ()#line:56
    while True :#line:58
        O0OOO00OOO0O0O0OO ='Player 1'if O0000000O00OO0O0O .turn =='white'else 'Player 2'#line:59
        O0O00OOOOO0OO0OO0 =input (f"{O0OOO00OOO0O0O0OO}, enter the start position (e.g., 'e2'): ")#line:60
        O00O0O0OO0O0O0O0O =input (f"{O0OOO00OOO0O0O0OO}, enter the end position (e.g., 'e4'): ")#line:61
        O0O00OOOOO0OO0OO0 =parse_position (O0O00OOOOO0OO0OO0 )#line:63
        O00O0O0OO0O0O0O0O =parse_position (O00O0O0OO0O0O0O0O )#line:64
        O0000000O00OO0O0O .move_piece (O0O00OOOOO0OO0OO0 ,O00O0O0OO0O0O0O0O )#line:66
        O0000000O00OO0O0O .print_board ()#line:67
if __name__ =="__main__":#line:69
    main ()#line:70

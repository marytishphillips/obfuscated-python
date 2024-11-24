import sys #line:1
import copy #line:2
import argparse #line:3
import itertools #line:4
def parse_arguments ():#line:7
    O00OO000OOOOOOOOO =argparse .ArgumentParser (description ='Countdown - Numbers Game',add_help =False )#line:9
    O00OO000OOOOOOOOO ._optionals .title ='Target and List Numbers'#line:11
    O00OO000OOOOOOOOO .add_argument ('-h','--help',action ='help',default =argparse .SUPPRESS ,help ='Countdown Numbers Game. Inform a list of six numbers (-l) and a target (-t).')#line:15
    O00OO000OOOOOOOOO .add_argument ('-t','--target',type =int ,action ='store',dest ='target',default =100 ,help ='The target of the game.')#line:18
    O00OO000OOOOOOOOO .add_argument ('-l','--list',type =int ,nargs ='+',default =[1 ,2 ,4 ,8 ,10 ,25 ],help ='List with six integers.')#line:21
    OOO0O00O00OO0OOO0 =O00OO000OOOOOOOOO .parse_args ()#line:23
    return OOO0O00O00OO0OOO0 #line:25
pd ={}#line:28
def nubmers_game (OO00O00O0O000OO0O ,O0OOOO0000000OO0O ,O0O0000OO0OO0OOOO ,OO00O0O00OO00O0O0 ):#line:29
    global pd #line:30
    O0OOOO00O000O0O0O =['+','-','*','/']#line:31
    O0OOOO000O000O000 =copy .deepcopy (O0O0000OO0OO0OOOO )#line:32
    OO0O00O0O00OOO0OO =str ((O0OOOO000O000O000 ,OO00O00O0O000OO0O ))#line:33
    if OO0O00O0O00OOO0OO in pd :#line:34
        return pd [OO0O00O0O00OOO0OO ]#line:35
    if len (OO00O00O0O000OO0O )==1 :#line:37
        if OO00O00O0O000OO0O [0 ]==O0OOOO0000000OO0O :#line:38
            print (f'Target: {O0OOOO0000000OO0O}\nNumbers: {OO00O0O00OO00O0O0}\nSolution: {O0OOOO000O000O000}')#line:39
            return True #line:40
        else :#line:41
            pd [OO0O00O0O00OOO0OO ]=False #line:42
            return False #line:43
    else :#line:44
        for OOOO000OOOO0OOOOO in itertools .combinations (OO00O00O0O000OO0O ,2 ):#line:45
            if not OOOO000OOOO0OOOOO [0 ]or not OOOO000OOOO0OOOOO [1 ]:#line:46
                continue #line:47
            O0O000OOO0O0O00OO =OO00O00O0O000OO0O [:]#line:48
            O0O000OOO0O0O00OO .remove (OOOO000OOOO0OOOOO [0 ])#line:49
            O0O000OOO0O0O00OO .remove (OOOO000OOOO0OOOOO [1 ])#line:50
            OO0O0OO00000O00O0 =f'{OOOO000OOOO0OOOOO[0]} %s {OOOO000OOOO0OOOOO[1]}'#line:51
            O0OO00O0O00000OO0 =f'{OOOO000OOOO0OOOOO[1]} %s {OOOO000OOOO0OOOOO[0]}'#line:52
            if nubmers_game (O0O000OOO0O0O00OO +[OOOO000OOOO0OOOOO [0 ]+OOOO000OOOO0OOOOO [1 ]],O0OOOO0000000OO0O ,O0OOOO000O000O000 +[OO0O0OO00000O00O0 %('+')],OO00O0O00OO00O0O0 ):#line:53
                return True #line:54
            elif nubmers_game (O0O000OOO0O0O00OO +[OOOO000OOOO0OOOOO [0 ]-OOOO000OOOO0OOOOO [1 ]],O0OOOO0000000OO0O ,O0OOOO000O000O000 +[OO0O0OO00000O00O0 %('-')],OO00O0O00OO00O0O0 ):#line:55
                return True #line:56
            elif nubmers_game (O0O000OOO0O0O00OO +[OOOO000OOOO0OOOOO [1 ]-OOOO000OOOO0OOOOO [0 ]],O0OOOO0000000OO0O ,O0OOOO000O000O000 +[O0OO00O0O00000OO0 %('-')],OO00O0O00OO00O0O0 ):#line:57
                return True #line:58
            elif nubmers_game (O0O000OOO0O0O00OO +[OOOO000OOOO0OOOOO [0 ]*OOOO000OOOO0OOOOO [1 ]],O0OOOO0000000OO0O ,O0OOOO000O000O000 +[OO0O0OO00000O00O0 %('*')],OO00O0O00OO00O0O0 ):#line:59
                return True #line:60
            elif OOOO000OOOO0OOOOO [0 ]%OOOO000OOOO0OOOOO [1 ]==0 and nubmers_game (O0O000OOO0O0O00OO +[OOOO000OOOO0OOOOO [0 ]//OOOO000OOOO0OOOOO [1 ]],O0OOOO0000000OO0O ,O0OOOO000O000O000 +[OO0O0OO00000O00O0 %('/')],OO00O0O00OO00O0O0 ):#line:61
                return True #line:62
            elif OOOO000OOOO0OOOOO [1 ]%OOOO000OOOO0OOOOO [0 ]==0 and nubmers_game (O0O000OOO0O0O00OO +[OOOO000OOOO0OOOOO [1 ]//OOOO000OOOO0OOOOO [0 ]],O0OOOO0000000OO0O ,O0OOOO000O000O000 +[O0OO00O0O00000OO0 %('/')],OO00O0O00OO00O0O0 ):#line:63
                return True #line:64
            elif nubmers_game (O0O000OOO0O0O00OO +[OOOO000OOOO0OOOOO [0 ]],O0OOOO0000000OO0O ,O0OOOO000O000O000 ,OO00O0O00OO00O0O0 ):#line:65
                return True #line:66
            elif nubmers_game (O0O000OOO0O0O00OO +[OOOO000OOOO0OOOOO [1 ]],O0OOOO0000000OO0O ,O0OOOO000O000O000 ,OO00O0O00OO00O0O0 ):#line:67
                return True #line:68
    pd [OO0O00O0O00OOO0OO ]=False #line:69
    return False #line:70
if __name__ =='__main__':#line:73
    args =parse_arguments ()#line:75
    if len (args .list )!=6 :#line:77
        print (f'The set of numbers in Countdown is 6.')#line:78
        sys .exit (-1 )#line:79
    if args .target <0 or args .target >999 :#line:81
        print (f'The target number in Countdown is between 0 and 999.')#line:82
        sys .exit (-1 )#line:83
    if not nubmers_game (args .list ,args .target ,[],args .list ):#line:85
        print (f'Target: {args.target}')#line:86
        print (f'Numbers: {args.list}')#line:87
        print (f'Solution: Not found.')
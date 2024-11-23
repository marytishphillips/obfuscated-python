class DLL :#line:1
    ""#line:6
    def __init__ (O000OOOOO00O0O0O0 ,val :str =None ):#line:7
        O000OOOOO00O0O0O0 .val =val #line:8
        O000OOOOO00O0O0O0 .nxt =None #line:9
        O000OOOOO00O0O0O0 .prev =None #line:10
class BrowserHistory :#line:13
    ""#line:18
    def __init__ (OO0OO00OOO0O0OO0O ,OOOO0O0OOO0O000O0 :str ):#line:20
        ""#line:27
        OO0OO00OOO0O0OO0O .head =DLL (OOOO0O0OOO0O000O0 )#line:28
        OO0OO00OOO0O0OO0O .curr =OO0OO00OOO0O0OO0O .head #line:29
    def visit (O00O0O0O0OOO00O0O ,O0O0OO0000OO00O0O :str )->None :#line:31
        ""#line:38
        O0OO00000O00OO0OO =DLL (O0O0OO0000OO00O0O )#line:39
        O00O0O0O0OOO00O0O .curr .nxt =O0OO00000O00OO0OO #line:40
        O0OO00000O00OO0OO .prev =O00O0O0O0OOO00O0O .curr #line:41
        O00O0O0O0OOO00O0O .curr =O0OO00000O00OO0OO #line:43
    def back (O0OO0O0O0OO00O0OO ,OO00OO0000O0O0O0O :int )->str :#line:46
        ""#line:53
        while OO00OO0000O0O0O0O >0 and O0OO0O0O0OO00O0OO .curr .prev :#line:54
            O0OO0O0O0OO00O0OO .curr =O0OO0O0O0OO00O0OO .curr .prev #line:55
            OO00OO0000O0O0O0O -=1 #line:56
        return O0OO0O0O0OO00O0OO .curr .val #line:57
    def forward (O0O0O0000000000O0 ,OOO0OO0OO0OO0000O :int )->str :#line:60
        ""#line:67
        while OOO0OO0OO0OO0000O >0 and O0O0O0000000000O0 .curr .nxt :#line:68
            O0O0O0000000000O0 .curr =O0O0O0000000000O0 .curr .nxt #line:69
            OOO0OO0OO0OO0000O -=1 #line:70
        return O0O0O0000000000O0 .curr .val #line:71
if __name__ =="__main__":#line:74
    obj =BrowserHistory ("google.com")#line:75
    obj .visit ("twitter.com")#line:76
    param_2 =obj .back (1 )#line:77
    param_3 =obj .forward (1 )#line:78
    print (param_2 )#line:80
    print (param_3 )
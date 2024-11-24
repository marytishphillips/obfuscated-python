import os #line:1
import sys #line:2
import time #line:3
import threading #line:4
import subprocess #line:5
import tkinter #line:6
import tkinter .messagebox #line:7
def monitor (O00OOO0OO0O00O000 ,OOO00O0OO0OOOOOO0 ):#line:10
    OOOO0OOOOO0O0000O ="vnstat"#line:11
    O0OO00OO00OOOOOO0 =subprocess .Popen (OOOO0OOOOO0O0000O ,shell =True ,stdout =subprocess .PIPE )#line:12
    OOO0OO0000OOOOO00 =O0OO00OO00OOOOOO0 .communicate ()#line:13
    OOO0OO0000OOOOO00 =str (OOO0OO0000OOOOO00 )#line:14
    OOOO0OO0000O0OO0O =[]#line:16
    for O0OOO00OO0O0000OO in OOO0OO0000OOOOO00 .split ():#line:17
        try :#line:18
            if O0OOO00OO0O0000OO =="MiB"or O0OOO00OO0O0000OO =="GiB":#line:19
                OOOO0OO0000O0OO0O .append (O0OOO00OO0O0000OO )#line:20
            else :#line:21
                OOOO0OO0000O0OO0O .append (float (O0OOO00OO0O0000OO ))#line:22
        except ValueError :#line:23
            pass #line:24
    if OOO00O0OO0OOOOOO0 ==OOOO0OO0000O0OO0O [5 ]and O00OOO0OO0O00O000 <OOOO0OO0000O0OO0O [4 ]:#line:26
        print ("\nnetwork usage limit exceeded!\n")#line:27
        O00OOOO0000OO0000 =tkinter .Tk ()#line:28
        def O00OO000O0OOO0O00 ():#line:30
            tkinter .messagebox .showinfo ("Warning!","Network usage limit exceeded!!!!")#line:32
        O00O00OOO000O00O0 =tkinter .Button (O00OOOO0000OO0000 ,text ="Warning",command =O00OO000O0OOO0O00 )#line:34
        O00O00OOO000O00O0 .pack ()#line:35
        O00OOOO0000OO0000 .mainloop ()#line:36
    O000OO00O0OOOO0O0 =[O00OOO0OO0O00O000 ,OOO00O0OO0OOOOOO0 ]#line:37
    threading .Timer (60.0 ,monitor ,O000OO00O0OOOO0O0 ).start ()#line:38
def main ():#line:41
    if len (sys .argv )>3 or len (sys .argv )<3 :#line:42
        print ('command usage: python3 bandwidth_py3.py <data usage in MiB or GiB>')#line:45
        print ('example: python3 bandwidth_py3.py 500 MiB')#line:46
        print ('or python3 bandwidth_py3.py 2 GiB')#line:47
        exit (1 )#line:48
    else :#line:49
        O0000O00OOO00OO0O =float (sys .argv [1 ])#line:50
        O0O00O0O0000OO0OO =str (sys .argv [2 ])#line:51
        monitor (O0000O00OOO00OO0O ,O0O00O0O0000OO0OO )#line:53
if __name__ =="__main__":#line:56
    main ()
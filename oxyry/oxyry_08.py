import math #line:1
def from_cel ():#line:3
    OOOO0000O00O0OOOO =float (input ("Enter Temperature: "))#line:4
    O0O0O0OOOOOO00O00 =input ("You want to convert it into: \n (a)fahrenheit (b)Kelvin ")#line:5
    if O0O0O0OOOOOO00O00 =='a':#line:7
        O00000OOOO0O00O00 =(OOOO0000O00O0OOOO *(9 /5 ))+32 #line:8
        print (f"The temperature is: {O00000OOOO0O00O00} °F")#line:9
    else :#line:11
        O00000OOOO0O00O00 =OOOO0000O00O0OOOO +273.15 #line:12
        print (f"The temperature is: {O00000OOOO0O00O00} K")#line:13
def from_fah ():#line:17
    OOOOO00OOOOO0O0OO =float (input ("Enter Temperature: "))#line:18
    OOOO0000000O0O0OO =input ("You want to convert it into: \n (a)celsius (b)Kelvin ")#line:19
    if OOOO0000000O0O0OO =='a':#line:21
        OOOOOO000O0O000O0 =(OOOOO00OOOOO0O0OO -32 )*(5 /9 )#line:22
        print (f"The temperature is: {OOOOOO000O0O000O0} °C")#line:23
    else :#line:26
        OOOOOO000O0O000O0 =(OOOOO00OOOOO0O0OO -32 )*(5 /9 )+273.15 #line:27
        print (f"The temperature is: {OOOOOO000O0O000O0} K")#line:28
def from_Kel ():#line:31
    OOOO0OO0OO0OOO0OO =float (input ("Enter Temperature: "))#line:32
    OO0O000OOO0OO000O =input ("You want to convert it into: \n (a)celsius (b)fahrenheit ")#line:33
    if OO0O000OOO0OO000O =='a':#line:35
        O000OO0O0OOOO0OO0 =OOOO0OO0OO0OOO0OO -273.15 #line:36
        print (f"The temperature is: {O000OO0O0OOOO0OO0} °C")#line:37
    else :#line:39
        O000OO0O0OOOO0OO0 =(OOOO0OO0OO0OOO0OO -273.15 )*(5 /9 )+32 #line:40
        print (f"The temperature is: {O000OO0O0OOOO0OO0} °F")#line:41
def get_temp ():#line:46
    global t #line:47
    t =input ("What would you like to convert from? (input no.): \n (1)Celsius (2)fahrenheit (3)Kelvin ")#line:48
get_temp ()#line:50
if t =="1":#line:53
    from_cel ()#line:54
elif t =='2':#line:56
    from_fah ()#line:57
elif t =='3':#line:59
    from_Kel ()#line:60
else :#line:62
    print ("please enter a correct input")#line:63
    get_temp ()#line:64
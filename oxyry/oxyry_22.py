FibArray =[0 ,1 ]#line:1
def fibonacci (OO00O0O00OO00OO0O ):#line:3
    if OO00O0O00OO00OO0O <0 :#line:4
        print ("Incorrect input")#line:5
    elif OO00O0O00OO00OO0O <len (FibArray ):#line:6
        return FibArray [OO00O0O00OO00OO0O ]#line:7
    else :#line:8
        FibArray .append (fibonacci (OO00O0O00OO00OO0O -1 )+fibonacci (OO00O0O00OO00OO0O -2 ))#line:9
        return FibArray [OO00O0O00OO00OO0O ]#line:10
print (fibonacci (9 ))
from datetime import date #line:1
def calculate_age (O0O0OOOOOOO000OOO ):#line:4
    OO0O000O0OOOO0000 =date .today ()#line:5
    if OO0O000O0OOOO0000 <O0O0OOOOOOO000OOO :#line:8
        return "Invalid birthdate. Please enter a valid date."#line:9
    O0OO000OO0OOO00O0 =((OO0O000O0OOOO0000 .month ,OO0O000O0OOOO0000 .day )<(O0O0OOOOOOO000OOO .month ,O0O0OOOOOOO000OOO .day ))#line:11
    O0000O000O0O00OO0 =OO0O000O0OOOO0000 .year -O0O0OOOOOOO000OOO .year -O0OO000OO0OOO00O0 #line:12
    OOO00O0O0OO00OOOO =abs ((12 -O0O0OOOOOOO000OOO .month )+OO0O000O0OOOO0000 .month )#line:13
    O00OOOOO0O000000O =abs (OO0O000O0OOOO0000 .day -O0O0OOOOOOO000OOO .day )#line:14
    O0OO000OOOO0OOO0O =f"Age: {O0000O000O0O00OO0} years, {OOO00O0O0OO00OOOO} months, and {O00OOOOO0O000000O} days"#line:17
    return O0OO000OOOO0OOO0O #line:18
if __name__ =="__main__":#line:21
    print (" Age Calculator By Python")#line:22
    try :#line:24
        birthYear =int (input ("Enter the birth year: "))#line:25
        birthMonth =int (input ("Enter the birth month: "))#line:26
        birthDay =int (input ("Enter the birth day: "))#line:27
        dateOfBirth =date (birthYear ,birthMonth ,birthDay )#line:28
        age =calculate_age (dateOfBirth )#line:29
        print (age )#line:30
    except ValueError :#line:31
        print ("Invalid input. Please enter valid integers for the year, month, and day.")
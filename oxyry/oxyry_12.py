def encrypt (O000OOOO0O0OOOO00 ,O00OO000OOOOO0OO0 ):#line:1
    ""#line:2
    O0O0OO00O0O0OOOO0 =''#line:3
    for OOO0O00O0O0OO0O00 in O000OOOO0O0OOOO00 :#line:7
        if OOO0O00O0O0OO0O00 .isalpha ():#line:8
            O00OOOO000OOO0OOO =ord (OOO0O00O0O0OO0O00 )#line:14
            if OOO0O00O0O0OO0O00 .isupper ():#line:16
                OOOOO0OOO00OO00O0 =ord ('A')#line:17
            else :#line:18
                assert OOO0O00O0O0OO0O00 .islower ()#line:19
                OOOOO0OOO00OO00O0 =ord ('a')#line:20
            O00OOOO000OOO0OOO =(O00OOOO000OOO0OOO -OOOOO0OOO00OO00O0 +O00OO000OOOOO0OO0 )%26 +OOOOO0OOO00OO00O0 #line:24
            O0O0OO00O0O0OOOO0 +=chr (O00OOOO000OOO0OOO )#line:26
        elif OOO0O00O0O0OO0O00 .isdigit ():#line:28
            O0O0OO00O0O0OOOO0 +=OOO0O00O0O0OO0O00 #line:31
        else :#line:33
            O0O0OO00O0O0OOOO0 +=OOO0O00O0O0OO0O00 #line:34
    return O0O0OO00O0O0OOOO0 #line:36
def decrypt (OO00OO00OO0O0OO00 ,O0O0OO000O0OOOOO0 ):#line:39
    ""#line:40
    return encrypt (OO00OO00OO0O0OO00 ,-O0O0OO000O0OOOOO0 )#line:41
def decode (O0OO0000OOO0O00O0 ):#line:44
    ""#line:45
    pass #line:46
def get_key ():#line:49
    ""#line:50
    try :#line:51
        OOO0O0O0O0000OO0O =input ('Enter a key (1 - 25): ')#line:52
        O000O0OOOOOO000O0 =int (OOO0O0O0O0000OO0O )#line:53
        return O000O0OOOOOO000O0 #line:54
    except :#line:55
        print ('Invalid key. Using key: 0.')#line:56
        return 0 #line:57
print ('Do you wish to encrypt, decrypt, or decode a message?')#line:60
choice =input ()#line:61
if choice =='encrypt':#line:63
    phrase =input ('Message: ')#line:64
    code =get_key ()#line:65
    print ('Encrypted message:',encrypt (phrase ,code ))#line:66
elif choice =='decrypt':#line:67
    phrase =input ('Message: ')#line:68
    code =get_key ()#line:69
    print ('Decrypted message:',decrypt (phrase ,code ))#line:70
elif choice =='decode':#line:71
    phrase =input ('Message: ')#line:72
    print ('Decoding message:')#line:73
    decode (phrase )#line:74
else :#line:75
    print ('Error: Unrecognized Command')
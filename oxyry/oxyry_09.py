class MorseCode :#line:1
    morse_dict ={'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.','0':'-----',' ':'/'}#line:12
    @classmethod #line:14
    def encode (O00OO0O0O0OO0OO0O ,text =""):#line:15
        ""#line:16
        if not text :#line:17
            text ="SOS"#line:18
        try :#line:19
            return ' '.join (O00OO0O0O0OO0OO0O .morse_dict [O000000000O000O0O .upper ()]for O000000000O000O0O in text )#line:20
        except KeyError as OO0OO000O0O00OOOO :#line:21
            print (f"Error: Character '{OO0OO000O0O00OOOO.args[0]}' cannot be encoded in Morse code.")#line:22
            return None #line:23
    @classmethod #line:25
    def decode (OOOOOO0O000O0OOOO ,morse_code =""):#line:26
        ""#line:27
        if not morse_code :#line:28
            morse_code ="... --- ..."#line:29
        try :#line:30
            O0O000O00OO0O0000 ={OO0OOO0OO000OO00O :O000O0OO0OO0O0O00 for O000O0OO0OO0O0O00 ,OO0OOO0OO000OO00O in OOOOOO0O000O0OOOO .morse_dict .items ()}#line:31
            return ''.join (O0O000O00OO0O0000 [O00O00O0OO00OO0O0 ]for O00O00O0OO00OO0O0 in morse_code .split ())#line:32
        except KeyError as O00OO0O0O00O0O0O0 :#line:33
            print (f"Error: Morse code '{O00OO0O0O00O0O0O0.args[0]}' cannot be decoded.")#line:34
            return None #line:35
if __name__ =="__main__":#line:37
    text =input ("Enter text to encode (leave blank for default 'SOS'): ")#line:39
    morse_code =MorseCode .encode (text )#line:40
    print (f"Morse Code: {morse_code}")#line:41
    morse_input =input ("Enter Morse code to decode (leave blank for default '... --- ...'): ")#line:43
    decoded_text =MorseCode .decode (morse_input )#line:44
    print (f"Decoded Text: {decoded_text}")
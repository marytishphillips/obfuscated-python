import hashlib #line:1
import os #line:2
def hashFile (O00O0OOO00O0OO000 ):#line:7
    O0OOO0O000O0OO0OO =65536 #line:9
    O000000OOOO0O0O00 =hashlib .md5 ()#line:10
    with open (O00O0OOO00O0OO000 ,'rb')as O0OO0OO00O0O00OO0 :#line:11
        O0O000O0O00OOO000 =O0OO0OO00O0O00OO0 .read (O0OOO0O000O0OO0OO )#line:13
        while (len (O0O000O0O00OOO000 )>0 ):#line:14
            O000000OOOO0O0O00 .update (O0O000O0O00OOO000 )#line:15
            O0O000O0O00OOO000 =O0OO0OO00O0O00OO0 .read (O0OOO0O000O0OO0OO )#line:16
    return O000000OOOO0O0O00 .hexdigest ()#line:17
if __name__ =="__main__":#line:20
    hashMap ={}#line:22
    deletedFiles =[]#line:25
    filelist =[OO0OOO0OOOOO00000 for OO0OOO0OOOOO00000 in os .listdir ()if os .path .isfile (OO0OOO0OOOOO00000 )]#line:26
    for f in filelist :#line:27
        key =hashFile (f )#line:28
        if key in hashMap .keys ():#line:30
            deletedFiles .append (f )#line:31
            os .remove (f )#line:32
        else :#line:33
            hashMap [key ]=f #line:34
    if len (deletedFiles )!=0 :#line:35
        print ('Deleted Files')#line:36
        for i in deletedFiles :#line:37
            print (i )#line:38
    else :#line:39
        print ('No duplicate files found')
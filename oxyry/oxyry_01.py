import io #line:1
import base64 #line:2
from PyPDF2 import PdfReader #line:3
def main (OO000000OO000OO00 :bytes )->dict :#line:5
    OO0OO0O00OO00O0O0 =PdfReader (io .BytesIO (OO000000OO000OO00 ))#line:7
    OOOO000000OOO00OO =""#line:10
    for O00OOO0OO00O00OO0 in OO0OO0O00OO00O0O0 .pages :#line:13
        OOOOOO0OO0O000000 =O00OOO0OO00O00OO0 .extract_text ()#line:14
        if OOOOOO0OO0O000000 :#line:15
            OOOO000000OOO00OO +=OOOOOO0OO0O000000 +"\n"#line:16
    O0O0OO0O00OOO0000 =base64 .b64encode (OOOO000000OOO00OO .encode ('utf-8')).decode ('utf-8')#line:19
    return {"file":{"content":O0O0OO0O00OOO0000 ,"filename":"content.txt"}}
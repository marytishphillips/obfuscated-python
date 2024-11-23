import re #line:1
def check_password (O000O00O0000OOOO0 ):#line:2
  if len (O000O00O0000OOOO0 )<8 :#line:3
    return False #line:4
  elif re .search ('[0-9]',O000O00O0000OOOO0 )is None :#line:5
    return False #line:6
  elif re .search ('[a-z]',O000O00O0000OOOO0 )is None :#line:7
    return False #line:8
  elif re .search ('[A-Z]',O000O00O0000OOOO0 )is None :#line:9
    return False #line:10
  elif re .search ('[@#$^&]',O000O00O0000OOOO0 )is None :#line:11
    return False #line:12
  return True #line:13
for password in ["12345678","Abcd@1234"]:#line:15
  if (check_password (password )):#line:16
    print (password ," is a strong password.")#line:17
  else :#line:18
    print (password ,"is a weak password.")
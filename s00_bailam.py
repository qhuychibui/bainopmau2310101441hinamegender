#region debai
"""
--- ma debai / id
hi(name,gender)

--- nopbai
00 fork tu bainopmau tren replit tu trang web duoiday 
   https://replit.com/@NamG1/bainopmau2310101441hinamegender

01 lam bai vao tep s00_bailam.py, chay Run de co ketqua tatca la 1
02a tao github repo, mo kiemtra tep s00_bailam.py, va lay diachi/url aka githubrepourl

02b dan diachi githubrepourl tu trang web duoiday
    https://forms.gle/vEPwvDJQNm1ddMfh8

--- debai / problem
Hay viet ham hi(name, gender) xuat ra cau chao theo mota benduoi

--- vidu mau / testcase
Khi chay voi input    | Ketqua output
--------------------- | ------------
hi('Mom', 'f')        | Hi Ms Mom!
hi('Dad', 'm')        | Hi Mr Dad!
hi('AI-BTX', None)    | Hi AI-BTX!
hi(None, None)        | Hi!
"""
#endregion debai

#region bailam
def hi(name, gender):
  if gender == 'f':
    xung_ho = 'Ms'
    return f'Hi {xung_ho} {name}!'
  elif gender == 'm':
    xung_ho = 'Mr'
    return f'Hi {xung_ho} {name}!'
  elif gender == None and name == None :
    return f'Hi!'
  else:
    return f'Hi {name}!'
#endregion bailam
  
  
#endregion bailam

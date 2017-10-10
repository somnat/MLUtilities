import math
num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety', 0: 'Zero', 100:'Hundred', 1000:'Thousand'}
mathsym={'-','.'}
mathsym1={'NEGATIVE','POINT'}

def n2w100(n):
        if n<=20:
            return num2words[n].upper()
        elif n>20 and n<=99:
            return num2words[n-n%10].upper() +" "+ num2words[n%10].upper()
        else: 
            print "out"
def n2w200(n):
        if n>=100 and n<=199:
             x=n%100
             if x!=0:
               return "ONE"+" "+ num2words[n-n%100].upper()+"AND"+" "+n2w100(x)
             else:
               return "ONE"+" "+ num2words[n-n%100].upper()
        else:
             print "out"
def n2w201(n):
        if n>=200 and n<=999:
             x=n%100
             y=n/100
             if x!=0:
              return num2words[y].upper()+" "+"HUNDRED AND"+" "+n2w100(x)
             else:
              return num2words[y].upper()+" "+"HUNDRED"
        else:
             print "out"
def n2w2000(n):
        if n>=1000 and n<=1999:
             x=n%1000
             y=n/1000
             if x>0 and x<99:
              return "ONE"+" "+num2words[y].upper()+" "+ "THOUSAND"+" "+n2w100(x)
             elif x>=100 and x<199:
              return "ONE"+" "+num2words[y].upper()+" "+ "THOUSAND"+" "+n2w200(x)
             elif x>=200 and x<999:
              return "ONE"+" "+num2words[y].upper()+" "+ "THOUSAND"+" "+n2w201(x)
             else:
              return num2words[y].upper()+" "+ "THOUSAND"
        else:
            print "Error" 
def n2w2001(n):
        if n>=2000 and n<=9999:
             x=n%1000
             y=n/1000
             if x>0 and x<99:
              return num2words[y].upper()+" "+ "THOUSAND"+" "+n2w100(x)
             elif x>=100 and x<199:
              return num2words[y].upper()+" "+ "THOUSAND"+" "+n2w200(x)
             elif x>=200 and x<999:
              return num2words[y].upper()+" "+ "THOUSAND"+" "+n2w201(x)
             else:
              return num2words[y].upper()+" "+ "THOUSAND"
        else:
             print "out"
def realnum2words(n):
     #if n<0:
       #d,i=math.modf(float(n))
       #leni=len(str(i))-3
       #lend=len(str(d))-2
       #d=abs(d)
       num=str(float(n))
       i,d=num.split('.')
       z=abs(int(i))
       if z<=99:
          p=n2w100(z)
       elif z>=100 and z<=199:
          p=n2w200(z)
       elif z>=200 and z<=999:
          p=n2w201(z)
       elif z>=1000 and z<=1999:
          p=n2w2000(z)
       elif z>=2000 and z<=9999:
          p=n2w2001(z)
       else:
          print "Error"
       q=""

       if "0" in d and len(d)==1:
        return p
       else:
       	for t in d:
           q=q+" "+num2words[int(t)]
        if n<0:
          return "NEGATIVE"+" "+p +" "+"POINT"+q.upper()
        else:
          return p +" "+"POINT"+q.upper()

print realnum2words(1000.67)
print realnum2words(3797.00071)
print realnum2words(1000)
print realnum2words(3797)

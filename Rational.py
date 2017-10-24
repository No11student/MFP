import sys 
class Rational0:
    def __init__(self,num,den = 1):
       
        num1, den1 = Rational0.check(num,den)
        gcd = Rational0.get_gcd(num1,den1)
        self.num = num1/gcd 
        self.den = den1/gcd 
    
    def plus(self,another):
        den = self.den * another.den 
        num = self.num * another.den +self.den * another.num 
        return Rational0(num,den)
    
    def out(self):
        print(str(self. num)+'/'+str(self.den))
        
    def num(self):
        return self.num
    
    def den(self):
        return self.den
    
    def __add__(self,another):
        num = self.num * another.den +self.den * another.num
        den = self.den * another.den 
        return Rational0(num, den) 
    def __mul__(self,another):
        num = self.num * another.num 
        den = self.den * another.den 
        return Rational0(num, den) 
    def __floordiv__(self,another):
        if another.num == 0:
            sys.exit('The dived num can not be zero!')
        return Rational0(self.num * another.den, self.den * another.num)
        
    @staticmethod
    def get_gcd(m,n):#求最大公约数
        M = max(m,n)
        m = min(m,n)
        if M % m == 0:
            return m 
        else :
            y = M % m 
            while y != 0 :
                s = m % y
                if s == 0:
                    return y
                else :
                    y = s

    @staticmethod
    def check(m,n):
        if isinstance(m, int) and isinstance(n, int):
            if abs(n) != 0:
                if m < 0:
                    m = -m 
                    n = -n
                return m,n    
            else :
                sys.exit('The den of Rational can not be zero!')
        else:
            sys.exit('The type of num and den must be init! ')
    
    def __eq__(self):
        pass
    
    def __lt__(self):
        pass 
    
    
r1 = Rational0(-3, 2)
r1.out()
r2 = Rational0(4,5)
r2 = r2.plus(r1)
r2.out() 
r3 = r1 + r2
r3.out()
r4 = r2 // r1
r4.out()

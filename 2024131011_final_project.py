class Fraction(object):
    """Class to represent a number as a fraction"""
    def __init__(self, n, d):
        """ Method to construct a Fraction object """
        if type(n) != int or type(d) != int: # Check that n and d are of type int
            raise ValueError('requires type int')
        if d <= 0:
            raise ZeroDivisionError('requires positive integer denominator')
        # If we get here, n and d are ok => initialize Fraction:
        self.num = n
        self.denom = d
        self.reduce()

    ### Your work begins here ...

    def reduce(self):
        """Reduces self to simplest terms. This is done by dividing both
        numerator and denominator by their greatest common divisor (GCD)."""
        g=self.__gcd(self.num, self.denom) # To make reduced fraction
        self.num//=g
        self.denom//=g
    
    def __str__(self):
        """ Returns a string representation of the fraction object (self) """
        if self.num!=0:
            if self.denom!=1:
                return str(self.num) + '/' + str(self.denom)
            else:
                return str(self.num)
        else:
            return '0'

    def __add__(self, other):
        """ Returns new Fraction representing self + other """
        if isinstance(other, int):
            other=Fraction(other, 1)
        new_num = self.num * other.denom + other.num * self.denom
        new_denom = self.denom * other.denom
        return Fraction(new_num, new_denom)

    def __mul__(self, other):
        """ Returns new Fraction representing self * other """
        if isinstance(other, int):
            other=Fraction(other, 1)
        new_num = self.num * other.num
        new_denom = self.denom * other.denom
        return Fraction(new_num, new_denom)

    def __sub__(self, other):
        """ Returns new Fraction representing self - other """
        if isinstance(other, int):
            other=Fraction(other, 1)
        new_num=self.num*other.denom - self.denom*other.num
        new_denom=self.denom*other.denom
        return Fraction(new_num, new_denom)
    
    def __truediv__(self, other):
        """ Returns new Fraction representing self / other """
        if isinstance(other, int):
            other=Fraction(other, 1)
        new_num=self.num*other.denom
        new_denom=self.denom*other.num
        new=Fraction(new_num, new_denom)
        new.reduce() # To make reduced fraction
        return new
    
    def __lt__(self, other):
        """ Returns boolean representing self < other """
        if isinstance(other, int):
            other=Fraction(other, 1)
        if self.num*other.denom<self.denom*other.num:
            return True
        else:
            return False
    
    def __le__(self, other):
        """ Returns boolean representing self <= other """
        if isinstance(other, int):
            other=Fraction(other, 1)
        if self.num*other.denom<=self.denom*other.num:
            return True
        else:
            return False
    
    def __gt__(self, other):
        """ Returns boolean representing self > other """
        if isinstance(other, int):
            other=Fraction(other, 1)
        if self.num*other.denom>self.denom*other.num:
            return True
        else:
            return False
    
    def __ge__(self, other):
        """ Returns boolean representing self >= other """
        if isinstance(other, int):
            other=Fraction(other, 1)
        if self.num*other.denom>=self.denom*other.num:
            return True
        else:
            return False
    
    def __eq__(self, other):
        """ Returns boolean representing self = other """
        if isinstance(other, int):
            other=Fraction(other, 1)
        if self.num*other.denom==self.denom*other.num:
            return True
        else:
            return False
    
    ### Your work ends here ...
    # ----- You don't have to modify below
    def __gcd(self, _a, _b):
        """Get Greatest Common Division of _a and _b"""
        a, b = abs(_a), abs(_b)
        if b > a: a, b = b, a
        while b != 0:
            [a, b] = [b, a%b]
        if a == 0: a = 1
        return a

    def __neg__(self):
        """ Returns new Fraction representing (-1)*self """
        # Returns -self
        return Fraction(-self.num, self.denom)

    __radd__ = __add__
    __rmul__ = __mul__
    
    def __rsub__(self, other):
        """ Returns new Fraction representing self - other including cases that other is integer"""
        # Handles int - Fraction
        if isinstance(other, int):
            return Fraction(other, 1).__sub__(self)
        elif isinstance(other, Fraction):
            return other.__sub__(self)
        else:
            raise ValueError('requires type int or Fraction')
    
    def __rtruediv__(self, other):
        """ Returns new Fraction representing self / other including cases that other is integer"""
        # Handles int / Fraction
        if isinstance(other, int):
            return Fraction(other, 1).__truediv__(self)
        elif isinstance(other, Fraction):
            return other.__truediv__(self)
        else:
            raise ValueError('requires type int or Fraction')
    
    def __pow__(self, other):
        """ Returns new Fraction representing self ^ other """
        if isinstance(other, int):
            if other == 0:
                return Fraction(1, 1)
            else:
                ret = self
                for _ in range(abs(other) - 1):
                    ret = ret.__mul__(self)
                if other < 0:
                    ret = ret.__rtruediv__(1)
            return ret
        else:
            raise ValueError('requires type int')

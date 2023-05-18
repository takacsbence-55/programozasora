import math
class haromszog:
    def __init__(self, a=0,b=0,c=0):
        self.a = a
        self.b = b
        self.c = c

    def terulet(self):
        return (self.a*self.b)/2

    def pitagorasz(self):
        db = 0
        if self.a == 0:
            db = db + 1

        if self.b == 0:
            db = db + 1

        if self.c == 0:
            db = db + 1

        if db == 0:
            return "Minden oldal ismert"
        elif db > 1:
            return "Több ismeretlen hiba"
        else:
            if self.a == 0:
                self.a = math.sqrt(self.c**2-self.b**2)
                return self.a
            if self.b == 0:
                self.b = math.sqrt(self.c**2-self.a**2)
                return self.b
            if self.c == 0:
                self.c = math.sqrt(self.a**2+self.b**2)
                return self.c
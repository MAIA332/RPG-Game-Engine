import random

class formulas:
    A = random.choice(range(1,3))
    B = random.choice(range(1,3))
    
    def ataque(self,Def_2,Atk_1, h):
       
        DanoT = abs((Def_2*self.A)/4 - (Atk_1 * self.B)/4)
        Percent_DanoT = int((DanoT * 100)/h)
        

        if(DanoT >= h) or (h<0):
            h = 0
        else:

            h -= DanoT

        return DanoT, Percent_DanoT,h



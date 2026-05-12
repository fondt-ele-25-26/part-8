import numpy as np

class DrugDosage:
    def __init__(self, half_life):
        self.half_life = half_life
        self.alpha = 0.5**(1/half_life)
    
    def __call__(self, x, k):
        xnext = self.alpha * x
        return xnext
    

class DrugDosage2:
    def __init__(self, half_life, repeat):
        self.half_life = half_life
        self.alpha = 0.5**(1/half_life)
        self.repeat = repeat
    
    def __call__(self, x, k):
        if k % self.repeat == 0:
            xnext = self.alpha * x + 1
        else:
            xnext = self.alpha * x
        return xnext

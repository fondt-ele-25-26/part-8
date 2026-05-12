import numpy as np

class Ricker:
    def __init__(self, r, N=1):
        self.r = r
        self.N = N
    
    def __call__(self, x, k):
        r, N = self.r, self.N # Rinomino per compattezza
        xnext = x * np.exp(r * (1 - x/N)) # Calcolo il prossimo stato
        return xnext
    

import numpy as np

class VolpiConigli:

    def __init__(self, rv, rc, p):
        self.p = p
        self.rv = rv
        self.rc = rc

    def __call__(self, X, k): # Funzione di transizione
        # "Spacchetto" lo stato
        v, c = X
        # Calcolo il numero di volpi al prossimo passo
        nv = v + self.rv * (c - self.p * v)
        # Calcolo il numero di conigli al prossimo passo
        nc = self.rc*c - self.p * v
        # Restituisco il prossimo stato
        return np.array([nv, nc])


def volpi_conigli(X, k, rv=1.05, rc=2, p=2.5):
    v, c = X # "Spacchetto" lo stato
    nv = v + rv * (c - p * v) # volpi al prossimo passo
    nc = rc*c - p * v # conigli al prossimo passo
    return np.array([nv, nc])

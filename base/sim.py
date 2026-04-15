from matplotlib import pyplot as plt
import numpy as np

def simulate(f, X0, n):
    res = [X0] # Lo stato al passo 0 è x0
    for k in range(0, n):
        xnext = f(res[k], k) # Ottengo il prossimo stato
        res.append(xnext) # Aggiungo il nuovo stato in fondo alla lista
    return np.array(res) # Converto in numpy array e restituisco


def plot_sim(X, title=None, names=None, figsize=(15, 3)):
    # Costruisco una figure
    plt.figure(figsize=figsize)
    # Gestisco il caso in cui X sia un vettore mono-dimensionale
    if len(X.shape) == 1:
        X = X.reshape((len(X), 1))
    for j in range(X.shape[1]):
        # Definisco una etichetta per questa curva
        label = None
        if names is not None:
            label = names[j]
        # Disegno l'evoluzione della j-ma componente dello stato
        x = X[:, j]
        plt.plot(range(len(x)), x, label=label)
    # Aggiungo un titolo
    if title is not None:
        plt.title(title)
    # Aggiungo una legenda
    if names is not None:
        plt.legend(names)
    # Aggiugo una griglia
    plt.grid()
    # Disegno
    plt.show()

    
def plot_2d_trajectory(x, y, xlabel=None, ylabel=None, figsize=None, title=None):
    plt.figure(figsize=figsize)
    plt.plot(x, y)
    if xlabel is not None:
        plt.xlabel(xlabel) # Nome dell'asse x
    if ylabel is not None:
        plt.ylabel(ylabel) # Nome dell'asse y
    if title is not None:
        plt.title(title)
    plt.grid()
    plt.show()

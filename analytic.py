import numpy as np 
import matplotlib.pyplot as plt
import tqdm
e = np.exp(1)
def prob(x):
    return (1+e)/(1+e**(x+1))
def f(x):
    if(len(x)==0):return -1
    return prob(x[0])*(x[0]-1)+(1-prob(x[0]))*f(x[1:])

# sale days
N=2
# price range (0,2) 
s = np.linspace(0,2,21)
# input grid
g = np.meshgrid(*[s for i in range(N)])
# fix price for all N days
fixed = False
steps=1 if not fixed else 22

# reshuffle grid to array of input arrays for func f
input = np.transpose(g).reshape(int(len(np.transpose(g).flatten())/N),N)
result = [f(input[k]) for k in tqdm.tqdm(range(0,len(input),steps))]

ind = np.argmax(result)
print(input[ind*steps] , " => ", result[ind])
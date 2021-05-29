import numpy as np 
import matplotlib.pyplot as plt
import tqdm
e = np.exp(1)
def prob(x):
    return (1+e)/(1+e**(x+1))
def f(x):
    if(len(x)==0):return -1
    return prob(x[0])*(x[0]-1)+(1-prob(x[0]))*f(x[1:])

N=4
s = np.linspace(0,2,21)
g = np.meshgrid(*[s for i in range(N)])

input = np.transpose(g).reshape(int(len(np.transpose(g).flatten())/N),N)
result = [f(input[k]) for k in tqdm.tqdm(range(len(input)))]

ind = np.argmax(result)
print(input[ind] , " => ", result[ind])
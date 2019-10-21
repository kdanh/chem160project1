import numpy as np
ntrials=10000
sum=0
for N in range (1,201):
    sum=0
    for trial in range(ntrials):
        vars=np.random.normal(size=N)
        vars.sort()
        sum+=vars[N-1]
    sum/=ntrials
    print(N,sum)
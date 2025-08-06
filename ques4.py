import numpy as np

def stationary_distribution(p, q, r, N):
    """
    Return a list of size N+1 containing the stationary distribution of the Markov chain.
    
    p : array of size N+1, 0 < p[i] < 1, probability of price increase
    q : array of size N+1, 0 < q[i] < 1, probability of price decrease
    r : array of size N+1, r[i] = 1 - p[i] - q[i], probability of price remaining the same
    N : int, the maximum price of the stock
    
    """
    ans=[]
    p_multiple=1
    q_multiple=1
    sum=1
    for x in range(N):
        p_multiple*=(p[x])
        q_multiple*=(q[x+1])
        sum+=(p_multiple/q_multiple)
    pie_not=1/sum
    ans.append(pie_not)
    p_multiple=1
    q_multiple=1
    for x in range(N):
        p_multiple*=(p[x])
        q_multiple*=(q[x+1])
        ans.append(pie_not*(p_multiple/q_multiple))
    return ans

def helper_func(p, q, r, N, a, b):
    if(a==b):
        return 0
    if a <= 0 or a > N:
        return 1e2000000000
    return (1 + p[a]* helper_func(p,q, r, N, a+1, b) + q[a] *helper_func(p, q, r, N, a-1, b) )/ (1 - r[a])


def expected_wealth(p, q, r, N):
    """
    Return the expected wealth of the gambler in the long run.

    p : array of size N+1, 0 < p[i] < 1, probability of price increase
    q : array of size N+1, 0 < q[i] < 1, probability of price decrease
    r : array of size N+1, r[i] = 1 - p[i] - q[i], probability of price remaining the same
    N : int, the maximum price of the stock
    """
    stat_dist=stationary_distribution(p, q, r, N)
    ans=0
    for x in range(len(stat_dist)):
        ans+=(x*stat_dist[x])
    return ans

    
    

def expected_time( p, q,r, N, a, b):
    """
    Calculate expected time to reach price b starting from price a
    
    Args:
    N: Maximum price state
    p: List of probabilities of price increasing from each state
    q: List of probabilities of price decreasing from each state
    a: Initial price state
    b: Target price state
    
    Returns:
    float: Expected number of steps to reach target price
    """
        
    if a == b:
        return 0
        
    size = b
    A = np.zeros((size, size))
    c = np.ones(size)
    
    for i in range(size):
        if i == b:  
            c[i]=0
            A[i, i] = 1
        
        else:
            A[i, i]=1-r[i]
            if i > 0:  
                A[i, i-1] = -q[i]
            
            if i < b-1:  
                A[i, i+1] = -p[i]
            
    
    expected_times = np.linalg.solve(A, c)
    
    return expected_times[a]


p=[0.3,0.3,0.4,0.5,0.0 , 0.4]
q=[0.0,0.2,0.5,0.1,0.3 , 0.1]
r=[0.7,0.5,0.1,0.4,0.7,0.5]
N=5
a=2
b=3


print(stationary_distribution(p,q,r,N))
print(expected_wealth(p,q,r,N))
print(expected_time(p,q,r,N,a,b))
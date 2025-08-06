import math
def win_probability(p, q, k, N):
    """
    Return the probability of winning a game of chance.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    N : int, maximum wealth
    """
    ratio=q/p
    if(p!=q):
        return (1-ratio**k)/(1-ratio**N)
    else:
        return k/N
    

def limit_win_probability(p, q, k):
    """
    Return the probability of winning when the maximum wealth is infinity.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    """

    ratio=q/p
    if(q<p):
        return 1-ratio**k
    else :
        return 0
    return 0

def game_duration(p, q, k, N):
    """
    Return the expected number of rounds to either win or get ruined.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    """
    if(p==q):
        return k*(N-k)
    else:
        prob=win_probability(p, q, k, N)
        return ((k/(q-p))-(N/(q-p))*prob )




# p=0.65
# q=1-p
# k=3
# N=51
# print(win_probability(p,q,k,N))
# print(limit_win_probability(p,q,k))
# print(game_duration(p,q,k,N))
# p=0.69
# q=1-p
# k=13
# N=21
# print(win_probability(p,q,k,N))
# print(limit_win_probability(p,q,k))
# print(game_duration(p,q,k,N))
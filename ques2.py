"""
Use the following function to convert the decimal fraction of k/N into it's binary representation
using k_prec number of bits after the decimal point. You may assume that the expansion of 
k/N terminates before k_prec bits after the decimal point.
"""
def decimalToBinary(num, k_prec) : 
  
    binary = ""  
    Integral = int(num)    
    fractional = num - Integral 
   
    while (Integral) :       
        rem = Integral % 2
        binary += str(rem);  
        Integral //= 2

    binary = binary[ : : -1]  
    binary += '.'

    while (k_prec) : 
        fractional *= 2
        fract_bit = int(fractional)  
  
        if (fract_bit == 1) :  
            fractional -= fract_bit  
            binary += '1'       
        else : 
            binary += '0'
        k_prec -= 1
        
    return binary 

def Q2_a_helper(p, q, k, N, temp=None):
    binary_rep=decimalToBinary(k/N, 100)[1: ]
    binary_rep.removeprefix("")
    ans=0
    prob_total=1
    for i in range(99, -1, -1):
        if(binary_rep[i]=='1'):
            ans=p+q*ans
        else:
            ans=(p*ans)    
    return ans

# def checker(p, q, k, N):
#     if(k<=0):
#         return 0
#     if(k>=N):
#         return 1
#     ans=0
#     if(k<N/2):
#         #win
#         ans = p*checker(p, q, 2*k, N)
#     else:
#         ans=p+q*checker(p, q, 2*k-N, N)
#     return ans




def win_probability(p, q, k, N):
    """
    Return the probability of winning while gambling aggressively.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    N : int, maximum wealth
    """
    if(k==N):
        return 1
    if(k==0):
        return 0
    return(Q2_a_helper(p,q, k , N))

def checker_b(p, q, k, N):
    if(k<=0):
        return 0
    if(k>=N):
        return 0
    ans=0
    if(k<N/2):
        ans=1+p*checker_b(p, q, 2*k , N)
    else:
        ans=1+q*checker_b(p, q, 2*k-N, N)
    return ans


def game_duration(p, q, k, N):
    """
    Return the expected number of rounds to either win or get ruined while gambling aggressively.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    N : int, maximum wealth
    """
    # print(checker_b(p, q, k , N))
    if(k==N or k==0):
        return 0
    binary_rep=decimalToBinary(k/N, 32)[1: ]
    temp=31
    for x in range(31, -1, -1):
        if(binary_rep[x]=='0'):
            temp=x
        if(binary_rep[x]=='1'):
            break
    ans=0
    for i in range(temp-1, -1, -1):
        if(binary_rep[i]=='1'):
            ans=1+q*ans
        else:
            ans=(1+p*ans)
    
    return ans
    
 
p=0.6
q=1-p
k=523
N=4096
# print(decimalToBinary(7/9, 1200))
print(win_probability(p,q,k,N))
print(game_duration(p,q,k,N))

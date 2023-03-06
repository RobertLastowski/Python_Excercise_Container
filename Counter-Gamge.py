from math import *

#Counter_game task form HackerRank
# It's a game where we strat from number 5 and if it's a power of 2 player divide it by 2 and pass it to the next player
# but if not a power of 2 we're searching for the closest power of 2(but lower than n) and substract
# player wins if he/she reaches the n = 1 in his/her round

def counterGame(n):
    winner = 0 # non even for Richard, even for Louise
    if n == 1:
        return "Richard"
    else:
        while n >= 1:
            winner += 1
            logarytm = log2(n)
            if logarytm.is_integer() == False:
                n -= pow(2, floor(log(n)/log(2)))
            else:
                n = n/2
            
    
    if winner % 2 != 0:
        return "Richard"
    else:
        return "Louise"
    

n = 1463674015
print(counterGame(n))
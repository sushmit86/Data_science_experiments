# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 19:28:15 2015

@author: sushmitroy
"""

def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
   for cents in range(change+1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   return minCoins,coinsUsed



def main():
    amnt = 66
    clist = [1,5,10,22,25]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)

    print("Making change for",amnt,"requires")
    print(dpMakeChange(clist,amnt,coinCount,coinsUsed)[0][amnt],"coins")
    print("They are:")
    
    while (amnt >0):
        coin=dpMakeChange(clist,amnt,coinCount,coinsUsed)[1][amnt]
        print(coin)
        amnt = amnt - coin
    
   
    #print("The used list is as follows:")
    #print(coinsUsed)

main()

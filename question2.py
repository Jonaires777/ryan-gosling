coins = [1,2,5,10,20,50,100]

def greedy_search(change, coins):
    changesToGiveBack = [0] * len(coins)
    
    for pos, coin in enumerate(reversed(coins)):
        while coin <= change:
            change = change - coin
            changesToGiveBack[len(coins)-pos-1] = 1
    return changesToGiveBack

result = greedy_search(30, coins)

print("O array com o resultado do troco eh este:")
print(result)
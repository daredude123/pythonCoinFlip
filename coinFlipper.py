import random

print("Flip a coin")

class Coin:
    side = "kron" #default side
    def printside(self):
        if self.side == 1:
            return "kron"
        else:
            return "mynt"

def flipCoin(coin):
    coin.side = random.randint(1,2)
    print(coin.printside())

coin = Coin()
flipCoin(coin)
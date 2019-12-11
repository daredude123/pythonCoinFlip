import random
import cv2

print("Flip a coin")

class Coin:
    side = "kron" #default side
    mynt_side_image = cv2.imread("/home/andreas/python/pythonCoinFlip/resources/mynt.png")
    kron_side_image = cv2.imread("/home/andreas/python/pythonCoinFlip/resources/kron.png")

    def printside(self):
        if self.side == 1:
            self.side = "kron"
            cv2.imshow('image',self.kron_side_image)
            cv2.waitKey()
        else:
            self.side = "mynt"
            cv2.imshow('image2',self.kron_side_image)
            cv2.waitKey()

def flipCoin(coin):
    coin.side = random.randint(1,2)
    print(coin.printside())


coin = Coin()
flipCoin(coin)
print("success")
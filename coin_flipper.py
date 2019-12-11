"""dang lint"""
import random
import cv2

print("Flip a coin")

class Coin:
    """Coin class"""
    side = "kron" #default side
    mynt_side_image = cv2.imread("/home/andreas/python/pythonCoinFlip/resources/mynt.png")
    kron_side_image = cv2.imread("/home/andreas/python/pythonCoinFlip/resources/kron.png")

    def printside(self):
        """print the side with an image"""
        if self.side == 1:
            self.side = "kron"
            cv2.imshow('image',self.kron_side_image)
            cv2.waitKey()
        else:
            self.side = "mynt"
            cv2.imshow('image2',self.kron_side_image)
            cv2.waitKey()

def flip_coin(coin):
    """FLIP IT"""
    coin.side = random.randint(1,2)
    print(coin.printside())


COIN = Coin()
flip_coin(COIN)

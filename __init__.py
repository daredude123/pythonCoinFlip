"""dang lint"""

import random
import sys
import os
from PIL import Image

data_path = os.path.dirname(os.path.abspath(__file__))+"/data"

class Coin:
    """Coin class"""
    side = "kron" #default side
    mynt_side_image = Image.open(data_path+"/mynt.png")
    kron_side_image = Image.open(data_path+"/kron.png")

    def printside(self):
        """print the side with an image"""
        if self.side == 1:
            self.side = "kron"
            self.kron_side_image.show()
            print(self.side)
        else:
            self.side = "mynt"
            self.mynt_side_image.show()
            print(self.side)


def flip_coin(coin):
    """FLIP IT"""
    coin.side = random.randint(1, 2)
    coin.printside()


COIN = Coin()
flip_coin(COIN)
print("test")
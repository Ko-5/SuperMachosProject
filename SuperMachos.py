from random import shuffle, choice

class trunfo:
    def __init__(self,name,life,money,reign) -> None:
        self.name = name
        self.life = life
        self.money = money
        self.reign = reign

    def setPack(cartas):
        shuffle(cartas)
        return cartas
    
#A1 = 
A2 = trunfo('Napoleão Bonaparte', 52, 160000000000, 10)
#A3 = 
A4 = trunfo('Cleópata', 39, 9800000000000,21)
#A5 = 
#A6 =
#A7 =
#A8 =

cartas = [A2, A4]

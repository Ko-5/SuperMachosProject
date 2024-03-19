from random import shuffle, choice

class trunfo:
    def __init__(self,id,name,life,money,reign) -> None:
        self.id = id
        self.name = name
        self.life = life
        self.money = money
        self.reign = reign

    def setPack(cartas):
        shuffle(cartas)
        return cartas
    

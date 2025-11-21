class Wallet:
    def __init__(self,color :str,size :int):
        self.color = color
        self.size = size
        self.amountVola = 0
    def open(self):
        if self.amountVola == 0:
            return "Wallet opened ,no money inside"
        return "Wallet opened, still poor"
    def add_vola(self,amount : float):
        self.amountVola+=amount
        return "You added "+amount+"Ariary"
    def withdrawVola(self,amount : float):
        self.amountVola-=amount
        return "You withdrawed "+amount+"Ariary"
    def close(self):
        return "Poor wallet closed"
    def isLost(self):
        return "Your wallet with no money is lost"
    def checkVola(self):
        return self.amountVola

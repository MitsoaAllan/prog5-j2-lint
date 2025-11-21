class Wallet:
    def __init__(self,color :str,size :int):
        self.color = color
        self.size = size
        self.amount_vola = 0
    def open(self):
        if self.amount_vola == 0:
            return "Wallet opened ,no money inside"
        return "Wallet opened, still poor"
    def addVola(self,amount : float):
        self.amount_vola+=amount
        return "You added "+amount+"Ariary"
    def withdrawVola(self,amount : float):
        self.amount_vola-=amount
        return "You withdrawed "+amount+"Ariary"
    def close(self):
        return "Poor wallet closed"
    def isLost(self):
        return "Your wallet with no money is lost"
    def checkVola(self):
        return self.amount_vola

class Skin:

    def __init__(self, float_, price):
        self.float_ = float_    
        self.price = price        
    
    def print_(self):
        print(self.float_, "   ", self.price)


class SkinFloat:
    def __init__(self, Skin, Maxfloat,Price):
        self.Skin = Skin    
        self.Maxfloat = Maxfloat
        self.Price = Price      
    def print_(self):
        print(self.Skin, "   ", self.Maxfloat, "  ", self.Price)

    
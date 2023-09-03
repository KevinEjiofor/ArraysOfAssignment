class Flyer:
    def fly(self,bird):
        self.bird.fly()
    
class Bird:
    def fly(self):
            print("flying")

class chicken:
    def fly(self):
        print("chicken flying")





flyer1 = flyer()
bird1 = Bird()
chicken = chicken()
flyer1.fly(bird1)
flyer1.fly(chicken)
    
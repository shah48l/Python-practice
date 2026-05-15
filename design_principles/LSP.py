class Bird:
    def fly(self):
        print("flying")
        
class Penguin:
    def fly(self):
        raise Exception("Can't Fly")
    
class Bird:
    pass

class FlyingBird:
    def fly(self):
        print("Flying")
        
class Penguin(Bird):
    def swin(self):
        print("Swimming")




def add_sprinkes(func):
    def wrapper():
        print("You have added sprinkles")
        func()
    return wrapper

def add_fudge(func):
    def wrapper():
        print("You have added Fudge")
        func()
    return wrapper 

@add_sprinkes
@add_fudge
def get_ice_cream():
    print("Here is your Ice cream ")
    
get_ice_cream()
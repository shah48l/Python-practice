from typing import Callable

#closure with a nested func

def f(x:int) -> Callable[[int],int]:
    def g(y:int) -> int:
        return x + y 
    return g


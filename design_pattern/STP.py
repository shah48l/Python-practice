''' Basic Singleton Patten '''

class Singleton:
    _instance = None # A class attribute to hold a single instance

    def __new__(cls): #  __new__ Controls the object creation 
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

''' The major problem in the above is that it has race condition init 
    where _instance = None is the race condition in it to solve 
    that Threading is introduces'''

''' Thread Safe Singleton Pattern '''
import threading
class Singleton:
    _instance = None 
    _lock = threading.lock()
    
    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance
''' The above code prevents multiple instances in multithreading '''

''' Decorator Singleton'''
def singleton(cls):
    instances = {}
    
    def wrapper(*args,**kwargs):
        if cls not in instances:
            instances[cls] = cls(*args,**kwargs)
        return instances[cls]
    return wrapper
@singleton
class Database:
    pass

            
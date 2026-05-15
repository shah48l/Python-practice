class UserProfile:
    def __init__(self,name,age):
        self.__age = age
        self.name = name
        
        # Getter method for age
        @property
        def age(self):
            return self.__age
        
        #Setter method for age validation
        @age.setter
        def age(self,value):
            if isinstance(value,int) and 0 < value < 150:
                self.__age = value
            else:
                raise ValueError(" Age must be an integer between 1 to 149 ")
            
        
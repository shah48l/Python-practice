'''Write a function that reads a file called "data.txt", catches 
a FileNotFoundError, and returns an empty list if the file 
doesn't exist. Otherwise return the lines as a list.'''

def read_file():
    try:
        with open('data.txt',"r") as file:
            return file.readline()
        
    except FileNotFoundError:
        return []
    
    pass

print(read_file)
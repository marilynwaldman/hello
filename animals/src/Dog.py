class Dog:
       
    # Class Variable
    animal = 'dog'     
       
    # The init method or constructor
    def __init__(self, name):
           
        # Instance Variable
        self.name = name            
   
    # Adds an instance variable 
    def bark(self):
        print('Woof from', self.name)

if __name__ == "__main__":
        mydog = Dog("Fluffy")
        mydog.bark()

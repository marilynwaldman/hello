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
        return self.name

if __name__ == "__main__":
        mydog = Dog("Fluffy")
        name = mydog.bark()
        print(name)
        assert name == "Fluffy1"
        assert name == "Fluffy"



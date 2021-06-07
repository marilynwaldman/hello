class Cat:
       
    # Class Variable
    animal = 'cat'     
       
    # The init method or constructor
    def __init__(self, name):
           
        # Instance Variable
        self.name = name            
   
    # Adds an instance variable 
    def meow(self):
        print('Meow from', self.name)
        return self.name

if __name__ == "__main__":
        print("I'm called from Cat.py")
        mycat = Cat("Felix")
        name = mycat.meow()
        print(name)
        #assert name == "Felix"
        assert name == "Felix"
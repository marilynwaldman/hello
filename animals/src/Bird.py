class Bird:
       
    # Class Variable
    animal = 'bird'     
       
    # The init method or constructor
    def __init__(self, name):
           
        # Instance Variable
        self.name = name            
   
    # Adds an instance variable 
    def tweet(self):
        print('Tweet from', self.name)
        return self.name

if __name__ == "__main__":
        print("I'm called from Bird.py")
        mybird = Bird("Tweetie")
        name = mybird.tweet()
        print(name)
        #assert name == "Felix"
        assert name == "Tweetie"
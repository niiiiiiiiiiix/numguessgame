class GuessNumber:
   
    def __init__ (self, number, mn=0, mx=100):
        self.number = number
        self.min = mn
        self.max = mx
        self.guesses = 0

    def get_guess(self):
        guess = input(f"Please guess a number between {self.min} and {self.max}: ")

        if self.valid_number(guess):
            # if True, then this will execute
            return int(guess)
        else:
            # if False, then this will execute
            print("Please enter a valid number.")
            return self.get_guess()
    
    def valid_number(self, str_number):
        try:
            number = int(str_number)
        except:
            return False
        
        return self.min <= number <= self.max 
        # if value entered is not in the min max range, the above line will return False

        # both False entries in "valid_number" is to prompt the 'else' statement in get_guess

    def play(self):
        while True:
            self.guesses += 1
            
            guess = self.get_guess()

            if guess < self.number:
                print("Your guess was under.")
            elif guess > self.number:
                print("Your guess was over.")
            else: #they guessed it
                break        
        print(f"You guessed it in {self.guesses} guesses.")

from random import randint
a = randint(0,100)
game = GuessNumber(a)
game.play()



"""    
@@@ assignment – create a def object for a random number

such that

from random import randint
a = randint(0,100)
game = GuessNumber(a)
game.play()

works

    def rand_number():
        from random import randint
        rand_num = (0,100)
        
"""
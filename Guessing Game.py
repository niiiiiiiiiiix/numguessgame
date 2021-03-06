from random import randint

class GuessNumber:

    def __init__ (self, mn=0, mx=100):
        self.min = mn
        self.max = mx
        self.number = randint(self.min, self.max)
        self.guesses = 0

    def get_guess(self):
        guess = input(f"Please guess a number between {self.min} and {self.max}: ")

        if self.valid_number(guess):
            # if True, then this will execute
            return int(guess)
        else:
            # if False, then this will execute
            print("Please enter a valid guess.")
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

game = GuessNumber(1000,10000)
print(game.__dict__) # to know the number to guess
game.play()

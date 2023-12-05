class Woof:
    answer = "" # The dog breed to be guessed
    tries = 5 # Amount of tries available
    letters_guessed = "" # String of letters already guessed; Append each try

    def __init__(self, breed: str): # Create new answer to guess, resetting tries
        self.answer: str = breed.lower()
        self.tries = 5

    def display_word(self, answer): # Print prompt + current word status
        print("The word is: ", end = "")
        for i in range(len(self.answer)):
                    if self.letters_guessed.find(self.answer[i]) != -1:
                        print(self.answer[i], end = "") 
                    else: 
                        print('*', end = "")
        print(f"\n{self.tries} tries remaining!")
    def guess_word(self): # Guess word
        while self.tries > 0:
            self.display_word("")
            print("Enter a guess: ", end = "")
            guess = input().lower()
            if guess == self.answer:  
                print(f"Congrats! The word was {self.answer}")
                break
            else:
                self.tries = self.tries - 1
                self.letters_guessed = self.letters_guessed + guess
                if self.tries < 5: print()
        print(f"Oh no! The word was {self.answer}")
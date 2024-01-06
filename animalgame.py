class AnimalGame:
    def _init_(self):
        self.animal = "giraffe"  # Changed the default animal to "giraffe"

    def play(self):
        print("Welcome to the Animal Guessing Game!")
        print("Think of an animal, and I'll try to guess it.")
        input("Press Enter when you're ready...")

        while True:
            question = input("Is it a mammal? (yes/no) ")
            if question.lower() == "yes":
                question = input("Is it a herbivore? (yes/no) ")
                if question.lower() == "yes":
                    print(f"I guess it's a {self.animal}!")  # Used the chosen animal in the guess
                    break
                elif question.lower() == "no":
                    print("I don't know the animal.")
                    break
                else:
                    print("Please answer with 'yes' or 'no'.")
            elif question.lower() == "no":
                question = input("Is it a bird? (yes/no) ")
                if question.lower() == "yes":
                    print("I don't know the animal.")
                    break
                elif question.lower() == "no":
                    print("I don't know the animal.")
                    break
                else:
                    print("Please answer with 'yes' or 'no'.")
            else:
                print("Please answer with 'yes' or 'no'.")

# Example of using the AnimalGame with the changed animal
game = AnimalGame()
game.play()
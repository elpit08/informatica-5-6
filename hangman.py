import random
def start_game():
    with open("corpus_for_hangman.txt") as word_list:
        content = word_list.read().splitlines()

    repeated_guess = []
    attempts = 10
    the_one =random.choice(content).lower()
    the_ones_secret = ["_"] * len(the_one)
    word_counter = the_ones_secret.copy()

    print(" ".join(the_ones_secret))

    print("Guess the word")
    while True:
        while True:
            guess = input("take a guess: ")

            if guess in repeated_guess:
                print("Already selected that character")

            if len(guess) == 1:
                break
            else:
                print("not a valid guess. Try again")

        index_replacement = 0
        for _ in the_one:
            if guess == _:

                word_counter[index_replacement] = guess
            index_replacement += 1

        if guess in word_counter:
            attempts -= 0
        else:
            attempts -= 1
        print(f"attempts remaining: {attempts} ")

        print(" ".join(word_counter))
        if attempts == 0:
            print("You lost, bartholomew died :(")
            break
        if word_counter == list(the_one):
            print("Congratulations you WON !!!!")
            break
        repeated_guess.append(guess)
        print("Used words: ")
        print(" ".join(repeated_guess))



def main():
    start_game()
if __name__=="__main__":
    main()










#def the main function
#write a print to say welcome to the game
#create a txt file with all the words
#then create another function to get a word from the txt file
#then create a loop in the main function
#in the main function give the user a list of how many letters the word has
#ask for an input from the user
#do a if so we only accept an character or exit
#then make a list with wich letter he had guessed
#create a if that doesnt accept an previusly typed character
#make a counter with how many tries he has
#make an if statement
#if he gets it right
#if he gets it wrong
#write congratulations for the first one
#repeat with another word if the user fails
#give the option to exit the game
# end the main function


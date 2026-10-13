import random
def start_game():
    with open("corpus_for_hangman.txt") as word_list:
        content = word_list.read().splitlines()

        the_one =random.choice(content)
        print(the_one)

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


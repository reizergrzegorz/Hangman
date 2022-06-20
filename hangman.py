import random

countries = []
capitals = []
picked_letters_list = [] 

def main():
    while True:  
                  
        difficulty_level = choose_difficulty_level(["1", "2", "3"], "Choose difficulty level: " )
        lives = get_number_of_lives(difficulty_level)
        secret_word = get_word_to_guess()
        so_far = check_space(secret_word)
        print(so_far)
        print(picked_letters_list)
        
        while lives > 0:
            
            picked_letter = ask_if_provides_a_letter()
            if picked_letter not in picked_letters_list:
                picked_letters_list.append(picked_letter)              
            if picked_letter in secret_word:
                print("Correct!")
                print()
                new_so_far = ""
                
                for i in range(len(secret_word)):
                    if picked_letter == secret_word[i]:
                        new_so_far += picked_letter
                    else:
                        new_so_far += so_far[i]
                so_far = new_so_far
                if so_far == secret_word:
                    print("Congratulations, you win! Secret word was: " + secret_word)
                    print()
                    break
            elif picked_letter not in secret_word:
                print("Wrong!")
                print()
                lives -= 1
                print_hangman(lives)
            print("Lives remains:")
            print(lives)
            print(so_far)
            print(picked_letters_list)
            
        if lives == 0:
            print("Sorry, you have lost. Secret word was: " + secret_word)
            print()
        
        picked_letters_list.clear() 
        
        next_game = input("Press 'y' to play again, else quit: ").upper()
        if next_game == "Y":   
           continue     
        else:
            print("See you soon")
            break
                    
def choose_difficulty_level(options, message):
    
    user_input = input(message)
    while user_input not in options:
        user_input = input("Try again: ") 
    return user_input

def get_number_of_lives(user_input):
    
    if user_input == "1":
        lives = 9
    elif user_input == "2":
        lives = 8
    elif user_input == "3":
        lives = 7
    return lives

def get_word_to_guess():
                   
    file = open("countries-and-capitals.txt", "r")          
    c_and_c_list = file.read()
    whole_list = c_and_c_list.split("\n")  
    for x in whole_list:
        split = x.split(" | ")    
        if len(split) == 2:
            countries.append(split[0])
            capitals.append(split[1])
    secret_word = random.choice(countries)
    return secret_word.upper()
    
def ask_if_provides_a_letter():
    
    while True:
        picked_letter = input("Choose a letter: ").upper() 
        
        if len(picked_letter) == 1 and picked_letter.isalpha():
            if picked_letter in picked_letters_list:
                print("Letter was chosen, pick different one!")
                print()
                continue
            if picked_letter not in picked_letters_list:
                break   
        else:
            print("Try again, please choose a single letter!") 
            print()
            continue
    return picked_letter

def check_space(secret_word):
     
    so_far = ""
    for i in range(len(secret_word)):
        if secret_word[i] == " ":
            so_far += " "
        else:
            so_far += "_"
    return so_far

def print_hangman(lives):
    if lives == 8:
        print("           ")
        print("           ")
        print("          |")
        print("          |")
    elif lives == 7:
        print("           ")
        print("          |")
        print("          |")
        print("          |")
        print("          |")
    elif lives == 6:
        print("    _______ ")
        print("          |")
        print("          |")
        print("          |")
        print("          |")
    elif lives == 5:
        print("    _______ ")
        print("     O    |")
        print("          |")
        print("          |")
        print("          |") 
    elif lives == 4:
        print("    _______ ")
        print("     O    |")
        print("     |    |")
        print("          |")
        print("          |") 
    elif lives == 3:
        print("    _______ ")
        print("     O    |")
        print("    /|    |")
        print("          |")
        print("          |")
    elif lives == 2:
        print("    _______ ")
        print("     O    |")
        print("    /|\   |")
        print("          |")
        print("          |") 
    elif lives == 1:
        print("    _______ ")
        print("     O    |")
        print("    /|\   |")
        print("    /     |")
        print("          |")
    elif lives == 0:
        print("    _______ ")
        print("     O    |")
        print("    /|\   |")
        print("    / \   |")
        print("  YOU LOST|")
         
if __name__ == "__main__":
    main()
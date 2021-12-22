## generate random word for guess
import random
word_list = ['rooster', 'wicca', 'parsnip']
#take word list from file here instead of hard code
#start while loop here
word_to_guess = random.choices(word_list)
word_string= list(''.join(word_to_guess))
#print(word_string)

## initialize variables
total_guess = 7

word_to_solve = []
for i in range(0,len(word_string)):
    word_to_solve.append('_')    

## get and check user guess
while total_guess != 0:
    print(word_to_solve)
    user_guess = input('Guess a letter or word: ')
    #hprint(user_guess)
    if user_guess.isalpha() == False:
        print('Invalid input. Please guess again')
    elif len(user_guess) > 1:
        user_guess = user_guess.lower()
        if user_guess == ''.join(word_to_guess):
            print("Congrats, you've guessed correctly! The word was " + ''.join(word_to_guess) + '.')
            total_guess = 0
        else:
            if total_guess == 1:
                print("Gameover. You've guessed incorrectly. The word was " + ''.join(word_to_guess))
                total_guess = 0
            else:
                total_guess -= 1
                print("That is incorrect. You have " + str(total_guess) + " guess(es) remaining.")
    else:
        user_guess = user_guess.lower()
        if (user_guess in word_string) == False:
            if total_guess == 1:
                print("Gameover. You've guessed incorrectly. The word was " + ''.join(word_to_guess) + '.')
                total_guess = 0
            else:
                total_guess -= 1
                print("You've guessed incorrectly. You have " + str(total_guess) + " guess(es) remaining.")
        else:
            for i in range(0, len(word_string)):
                if user_guess == word_string[i]:
                    word_to_solve[i] = user_guess
                    i += 1
                else:
                    i += 1
            if ''.join(word_to_solve) == ''.join(word_to_guess):
                print("Congrats, you've completed the word! The word was " + ''.join(word_to_guess) + '.')
                total_guess = 0
            else:
                print("You've guessed a letter!")
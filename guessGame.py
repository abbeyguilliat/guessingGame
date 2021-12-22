import csv;
import random;

file = open('4000-most-common-english-words-csv.csv','r');
read_file = csv.reader(file);

word_list = [];

for line in read_file:
    word_list.append(line[0]);

num_wins = 0
num_losses = 0

while len(word_list) > 0:
    word_to_guess = random.choices(word_list)
    word_to_remove = word_to_guess[0]
    word_list.remove(word_to_remove)
    word_string= list(''.join(word_to_guess))
    
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
                num_wins += 1
                total_guess = 0
            else:
                if total_guess == 1:
                    print("Gameover. You've guessed incorrectly. The word was " + ''.join(word_to_guess))
                    num_losses += 1
                    total_guess = 0
                else:
                    total_guess -= 1
                    print("That is incorrect. You have %i guess(es) remaining." % (total_guess))
        else:
            user_guess = user_guess.lower()
            if (user_guess in word_string) == False:
                if total_guess == 1:
                    print("Gameover. You've guessed incorrectly. The word was " + ''.join(word_to_guess) + '.')
                    num_losses += 1
                    total_guess = 0
                else:
                    total_guess -= 1
                    print("You've guessed incorrectly. You have %i guess(es) remaining." % (total_guess))
            else:
                for i in range(0, len(word_string)):
                    if user_guess == word_string[i]:
                        word_to_solve[i] = user_guess
                        i += 1
                    else:
                        i += 1
                if ''.join(word_to_solve) == ''.join(word_to_guess):
                    print("Congrats, you've completed the word! The word was " + ''.join(word_to_guess) + '.')
                    num_wins += 1
                    total_guess = 0
                else:
                    print("You've guessed a letter!")
    
    input_is_valid = False;
    while input_is_valid == False:
        continue_result = input('Continue? Y/N: ');
        if continue_result.lower() == 'y':
            input_is_valid = True;
        elif continue_result.lower() == 'n':
            word_list = []
            #print results from games played
            print('W: %i, L: %i' % (num_wins, num_losses));
            input_is_valid = True;
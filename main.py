start = input('Send anything to start the game! \n \n')

def gamestart(start):
    print(
        'Welcome To The Number Guessing Game \n I will try to guess your \n Whole number by asking a couple of questions')

    name = input('Before we start what is your name? \n ')
    print('\n \n \n Hello ' + name + '... ')

    print('  _____ \n (* ᴗ *) \n |_🍞_|' + "     < My name is TOAST, and I will be your HOST!!! )")


    difficulty = input('\n \n Please choose your difficulty, \n P.S the higher the difficulty. The more I will be asking!' + '\n  \n Type one of the following: \n \'easy\' (1-100)\n \'medium\' (1-1000)      \n \'hard\' (1-1000000)\n \'custom\' (choose any range)\n \n')

    if difficulty == 'easy':
        print(
            'Alright, You chose the easy difficulty... Taking the cowards way out arent you? \n  _____ \n (* < *) \n |_🍞_|')

        return guess(1, 100, 0)
    elif difficulty == 'medium':
        print(
            'Alright, You chose the medium difficulty... up for a challenge eh? \n _____ \n (^ o ^) \n  |_🍞_|')
        return guess(1, 1000, 0)
    elif difficulty == 'custom':
        max_num = int(input('What is the maximum the number can be?\n'))
        min_num = int(input('What is the minimum the number can be?\n'))
        return guess(min_num, max_num, 0)

    elif difficulty != 'hard':
        print('Invalid response, try again')
        return gamestart(0)


    else:
        print(
            'OOPS, You chose the hard difficulty... I think I put that as a mistake... Be easy on me please  \n _____ \n (- _ -) \n  |_🍞_|')

        return guess(1, 1000000, 0)




def guess(min_num, max_num, question_num):
    print('If at any point, you want to restart the game, type \'restart\'')
    # 1-100
    toast_guess = (max_num + min_num) // 2
    question_num += 1
    print('GUESS ATTEMPT # ' + str(question_num)  + '\n \n guess: ' + str(toast_guess))


    answer = input('\n \n if I am correct say \'yes\' if i am NOT CORRECT say \'no\' ): \n ______\n (O ^ O) \n  |_🍞_| \n')
    if answer == 'yes':
        print('And the winner is........ ME, the greatest toast\n \n \n')
        print('(^ ᴗ ^) \n |_🍞_|')
        print('Practice another 100 years to beat me!\n \n' + 'Amount of guesses it took:' + str(question_num) + '\n \n')
        return gamestart(0)


    max_response = input('\n \n  \n Is your number \'lower\' or \'higher\' than ' + str(toast_guess) +  '???\n')
    if max_response == 'lower':
        # lower
        max_num = toast_guess
        return guess(min_num, max_num, question_num)

    elif max_response == 'higher':
        # higher
        min_num = toast_guess
        return guess(min_num, max_num, question_num)

    elif max_response == 'restart':
        return gamestart(0)
    else:
        'you wrote an invalid response! \n restarting the game'
        print('(.\  /.) \n |_O_|')
        question_num = 0
        return gamestart(100)


print(gamestart(start))

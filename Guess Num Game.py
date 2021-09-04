import random
print('Hello! Whats Your Name?')
name = input()
secretnum = random.randint(1, 100)
print('Well '+name+', I am Thinking Of A Number Between 1 To 100')

for GuessesTaken in range(1, 11):
    print('Take A Guess. (' + str(GuessesTaken) + '/10)')
    guess = int(input())
    if guess < secretnum:
        if secretnum-guess > 20:
            print('Your guess is too low.')
        else:
            print('Your guess is a little low.')
    elif guess > secretnum:
        if guess-secretnum > 20:
            print('Your guess is too high.')
        else:
            print('Your guess is a little high.')
    else:
        break

if guess == secretnum:
    print('Great Job ' + name + '! Your Guess Was Correct!!')
else:
    print('Sorry, You ran out of guesses. The No. I was Thinking was' +
          str(secretnum) + './n Better Luck next Time!')

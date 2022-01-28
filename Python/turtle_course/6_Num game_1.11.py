print('----------PYTHON SAVE THE WORLD----------')
temp=input('Guess which number that I am thinking?')
guess=int(temp)
while guess != 8:
    temp=input('TRY AGAIN?')
    guess=int(temp)
    if guess == 8:
        print('THAT IS RIGHT!')
        print('BUT I WILL NOT GIVE A GIFT TO YOU.')
    else:
        if guess > 8:
            print('TOO BIG!')
        else:
            print('TOO SMALL!')
print('----------------GAME OVER----------------')

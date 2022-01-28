import random
secret = random.randint(1,9)
print('----------PYTHON SAVE THE WORLD----------')
temp=input('Guess which number that I am thinking[1-9]?')
guess=int(temp)
while guess != secret:
    temp=input('TRY AGAIN?')
    guess=int(temp)
    if guess == secret:
        print('THAT IS RIGHT!')
        print('BUT I WILL NOT GIVE A GIFT TO YOU.')
    else:
        if guess > secret:
            print('TOO BIG!')
        else:
            print('TOO SMALL!')
print('----------------GAME OVER----------------')

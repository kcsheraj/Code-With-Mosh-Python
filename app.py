ans = 9
gues_count = 3

while gues_count > 0:
    guess = int(input('make guess '))
    if guess == ans: 
        print('correct')
        break
    gues_count -= 1
else:
        print('\nyou louse')
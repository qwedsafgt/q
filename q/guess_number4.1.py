import random
numbers=random.sample(range(1,100),5)
A_couple=(numbers)
the_number=max(A_couple)

def judgement_input(guess_number):
    if the_number < guess_number:
        print("It's too large!")
    elif the_number > guess_number:
        print("It's too small!")
    elif the_number == guess_number:
        print("Congratulation!")
        return True

while True :
    input_number=input()
    if input_number.isnumeric():
        guess_number=int(input_number)
        if judgement_input(guess_number):
            exit(0)
        else:
            continue
    else:
        print("You must type an integer!")

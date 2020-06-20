import random

if __name__ == "__main__":
    a = 0
    b = 100
    answer = 0
    random_number = 0
    T = False
    random_number = random.randint(0,100)
    print("Hello, Welcome to the Random Number Game!\nYou need to keep choosing number until you reach the right number\n")
    while T == False:
        answer = int(input("Please input a number: "))
        if answer < random_number:
            print("Number guessed is too low, please guess again higher!\n")
        elif answer > random_number:
            print("Number guessed is too high, please guess again lower!\n")
        else:
            print(f"Congratulations you are right!\nThe answer is indeed {random_number}")
            T = True
        
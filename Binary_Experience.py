# A Binary Conversion Game
# Originally Scripted on September 10, 2026
# Includes a binary to decimal converter,
# a decimal to binary converter,
# and a conversion game.
# In the game, the score is based off of whether or not you are correct, and how fast you answer.
# Regardless of how fast you answer, an incorrect answer is a guaranteed score of 0.


from time import sleep, perf_counter
from random import randint
from sys import exit


print("Welcome to a binary experience\n")
sleep(0.5)
print("Please select a program\n")
sleep(0.2)
print("1 - Decimal to binary converter\n")
print("2 - Binary to Decimal converter\n")
print("3 - Speed Conversion Game\n")


program = input("> ")


if program == "1":
   print("\nDecimal to binary converter selected\n")
   print("Please select enter a number to convert to binary\n")
   while True:
       try:
           number = int(input("> "))
           b2number = bin(number)[2:]
           print("\nIn binary form:",b2number,"\n")
       except ValueError:
           print("Must be a positive integer")

    
elif program == "2":
    print("\nBinary to decimal converter selected\n")
    print("Please select enter a base 2 (binary) number to convert to decimal form\n")
    while True:
        try:
            number = input("> ")
            b10number = int(number, 2)
            print("\nIn decimal form:",b10number,"\n")
        except ValueError:
            print("\nMust be a binary number (1s and 0s)\n")
elif program == "3":
    print("\nSpeed Conversion Game selected\n")
    print("The purpose of this game is to convert a given decimal number between 0 and 255 to binary as fast as possible.\n")
    print("The faster you enter the correct answer the faster the higher your score.\n")
    print("Press enter to start.\n")
    sleep(0.2)
    input("")
    while True:
        target_num = randint(0, 255)
        bin_target = bin(target_num) [2:]
        sleep(0.5)
        print("Starting in:\n")
        print("3...\n")
        sleep(1)
        print("2...\n")
        sleep(1)
        print("1...\n")
        sleep(1)
        print(bin_target)
        print(f"\nConvert {target_num} to binary\n")
        start = perf_counter()
        number = input("> ")
        end = perf_counter()
        if number == bin_target:
            time = end - start
            score = max(20, min(100, round(100 - ((time - 9) * 3))))
            print(f"\nScore is {score}.")
        else:
            print("\nscore is 0")
        while True:
            print("\nplay again?(y/N)\n")
            play = input("> ").casefold().strip()
            if play == "y" or play == "yes":
                print("\n")
                break
            elif play == "n" or play == "no":
                exit()
            else:
                print("\nInvalid option, options are y (Yes) and n (No)")
else:
    print("Not a valid program")

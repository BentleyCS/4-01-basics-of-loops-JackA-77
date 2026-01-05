#All questions must use a loop for full points.
import random

def oddNumbers(n:int) -> str:
    out = ""
    for n in range(1,n+1,2):
        out += str(n)+ " "
    return out[:-1]
    """
    Print out all odd numbers from 1 to n(inclusive) in a single string separated by spaces.
    example oddNumbers(5) -> "1 3 5"
    example oddNumbers(8) -> "1 3 5 7"
    example oddNumbers(-8) -> ""
    """
print(oddNumbers(5))

def backwards(n)-> str:
    out = ""
    for n in range(n, 0, -1):
        out += str(n) + " "
    return out[:-1]
print(backwards(20))

"""
    modify the below function such that it prints out all the numbers from n to 1
    inclusive starting at n and counting down to 1
    example backwards(5) -> "5 4 3 2 1"
    example backwards(8) -> "8 7 6 5 4 3 2 1"
    example backwards(-2) -> ""
    """

def randomRepeating():
    RandNum = 0
    tries = 0
    while RandNum < 10:
        RandNum = random.randint(1,10)
        tries += 1
    """
    Print out a random number from 1-10 until you get a 10. Then print out how many
    times it took to roll a 10
    NOTE: Given randomness no test for this question
    :return:
    """
    print(f"it took {tries} tries to get a 10")

def randomRange(n):
    RandNumHigh = random.randint(1,100)
    RandNumLow = RandNumHigh
    TempRand = 0
    for i in range(n - 1):
        TempRand = random.randint(1,100)
        if TempRand > RandNumHigh:
            RandNumHigh = TempRand
        if TempRand < RandNumLow:
            RandNumLow = TempRand
    return(RandNumHigh, RandNumLow)

"""
    Generate a random number from 1 to 100 n number of times. Then after that is
    done print out what the highest number and the lowers number was from the rolled numbers.
    NOTE: Given randomness no test for this question
    :param n:
    :return:
    """
def reverse(word:str)->str:
    out = ""
    n = len(word) - 1
    while len(out) < len(word):
        out += word[n]
        n += -1
    return out




    """
    Takes in a string as an argument and return the given string in reverse.
    example reverse("cat") -> "tac"
    example reverse("Hello") -> "olleH"
    """

def fizzBuzzContinuous(n):
    x = 1
    out = ""
    while x < n + 1:
        if x % 5 == 0 and x % 3 == 0:
            out += ("fizzbuzz ")
            x += 1
        elif x % 5 == 0:
            out += ("buzz ")
            x += 1
        elif x % 3 == 0:
            out += ("fizz ")
            x += 1
        else:
            out += str(x) + " "
            x += 1
    return out[0:-1]
    """
    Modify the function such that it does the fizzbuzz operation on all numbers
    from 1 to n(inclusive).
    Fizz buzz is defined as
    if the number is divisble by 3 print fizz
    if the number is divisible by 5 print buzz
    if the number is divisible by both 3 and 5 print fizzbuzz
    if none of the above apply print the number.

    As with above questions add each anseer to a string and return the final string.
    :param n:
    :return:
    """

def collatz(n):
    out = str(n) + " "
    while n != 1:
        if n % 2 == 0:
            n = int(n/2)
            out+=str(n)+ " "
        else:
            n = (n*3) + 1
            out+=str(n) + " "
    return out[0:-1]

    """
    Modify this function such that it mimics the collatz conjecture starting at n
    and prints out each number.
    The collatz conjecture is that if n is an even number divide it by 2. if n is
    an odd number multiply it by 3 and add 1.
    Repeat this process until n == 1.
    :param n:
    :return:
    """


def fibonacci(n):
    Fib = ""
    first = 0
    second = 1
    for i in range(n):
        if i <= 1:
            Fib += str(i) + " "
        else:
            add  =  first + second
            Fib +=f"{add} "
            first  = second
            second = add
    return Fib[0:-1]

    """
    for the given argument n print out the first n numbers of the fibonacci
    sequence in a single string separated by spaces.
    The fibonacci sequence is defined as a sequence that starts with 0 then 1 as
    the first two numbers. Every subsequent number is the prior two numbers added together.
    Example fibonacci(6) -> "0 1 1 2 3 5"
    Example fibonacci(10) -> "0 1 1 2 3 5 8 13 21 34"
    Example fibonacci(1) -> "0"
    :param n:
    :return:
    """


print(fibonacci(300))